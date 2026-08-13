#!/usr/bin/env python3
"""Validate V0 scenario specifications and hand-simulated golden traces."""

from __future__ import annotations

import ast
import re
import sys
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
CASES_DIR = REPO_ROOT / "evals" / "cases"
RESULTS_DIR = REPO_ROOT / "evals" / "results"
ALLOWED_SKILLS = {
    "opportunity-finder",
    "assumption-challenger",
    "business-filter",
    "experiment-designer",
    "leverage-designer",
}
REQUIRED_RESULT_HEADINGS = {"## 当前判断", "## 依据", "## 下一步", "## Workspace 更新"}
REQUIRED_STATE_HEADINGS = {
    "## 当前目标",
    "## 当前阶段",
    "## 已确认事实 FACTS",
    "## 当前假设 ASSUMPTIONS",
    "## 当前正在考虑的决定",
    "## 已确认的决定",
    "## 最大未知量",
    "## 当前最大风险",
    "## 当前实验",
    "## 当前下一步",
    "## 为什么这是下一步",
    "## 最近一次状态变化",
    "## 相关材料",
}


class EvalFailure(Exception):
    pass


def parse_scalar(value: str) -> Any:
    if value == "true":
        return True
    if value == "false":
        return False
    if value in {"null", "~"}:
        return None
    if value.startswith(("\"", "'")):
        return ast.literal_eval(value)
    if re.fullmatch(r"-?\d+", value):
        return int(value)
    return value


def read_markdown(path: Path) -> tuple[dict[str, Any], str]:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines or lines[0] != "---":
        raise EvalFailure(f"{path}: missing YAML front matter")
    try:
        end = lines.index("---", 1)
    except ValueError as exc:
        raise EvalFailure(f"{path}: unterminated YAML front matter") from exc

    data: dict[str, Any] = {}
    active_list: str | None = None
    for number, line in enumerate(lines[1:end], start=2):
        if not line or line.lstrip().startswith("#"):
            continue
        if line.startswith("  - "):
            if active_list is None:
                raise EvalFailure(f"{path}:{number}: list item without key")
            data[active_list].append(parse_scalar(line[4:].strip()))
            continue
        if line.startswith((" ", "\t")):
            continue  # Nested state fields are not needed by the eval schema.
        if ":" not in line:
            raise EvalFailure(f"{path}:{number}: expected key: value")
        key, raw = line.split(":", 1)
        key = key.strip()
        raw = raw.strip()
        if not raw:
            data[key] = []
            active_list = key
        else:
            data[key] = parse_scalar(raw)
            active_list = None
    return data, "\n".join(lines[end + 1 :]).strip() + "\n"


def require_fields(path: Path, data: dict[str, Any], fields: set[str]) -> None:
    missing = sorted(fields - data.keys())
    if missing:
        raise EvalFailure(f"{path}: missing front matter fields {missing}")


def validate_fixture(case: dict[str, Any]) -> None:
    fixture_value = case.get("fixture")
    if not fixture_value:
        return
    fixture = REPO_ROOT / str(fixture_value)
    idea = fixture / "IDEA.md"
    state = fixture / "STATE.md"
    if not idea.is_file() or not state.is_file():
        raise EvalFailure(f"{case['id']}: fixture must contain IDEA.md and STATE.md")

    root_files = {path.name for path in fixture.iterdir() if path.is_file()}
    if root_files != {"IDEA.md", "STATE.md"}:
        raise EvalFailure(f"{case['id']}: fixture root has non-core files {sorted(root_files)}")

    state_data, state_body = read_markdown(state)
    if state_data.get("stage") != case["expected_stage"]:
        raise EvalFailure(f"{case['id']}: fixture stage does not match expected stage")
    missing_headings = sorted(
        heading for heading in REQUIRED_STATE_HEADINGS if heading not in state_body
    )
    if missing_headings:
        raise EvalFailure(f"{case['id']}: fixture STATE missing headings {missing_headings}")

    for raw_link in re.findall(r"\[[^]]+\]\(([^)]+)\)", state_body):
        if "://" in raw_link or raw_link.startswith("#"):
            continue
        target = (state.parent / raw_link.split("#", 1)[0]).resolve()
        if not target.exists():
            raise EvalFailure(f"{case['id']}: broken fixture link {raw_link}")


def validate_case(case_path: Path, result_path: Path) -> None:
    case, _ = read_markdown(case_path)
    result, result_body = read_markdown(result_path)
    require_fields(
        case_path,
        case,
        {
            "id",
            "title",
            "expected_stage",
            "expected_skills",
            "require_challenge",
            "require_evidence_split",
            "require_action",
            "require_correction",
            "require_persistence",
            "expected_stage_change",
        },
    )
    require_fields(
        result_path,
        result,
        {
            "id",
            "actual_stage",
            "actual_skills",
            "challenge_detected",
            "evidence_split",
            "actionable_next_step",
            "corrected_direction",
            "persistence_ok",
            "stage_changed",
        },
    )

    if case["id"] != result["id"]:
        raise EvalFailure(f"{case_path}: result id mismatch")
    if case["expected_stage"] != result["actual_stage"]:
        raise EvalFailure(
            f"{case['id']}: stage {result['actual_stage']} != {case['expected_stage']}"
        )
    expected_skills = case["expected_skills"]
    actual_skills = result["actual_skills"]
    if not isinstance(expected_skills, list) or not isinstance(actual_skills, list):
        raise EvalFailure(f"{case['id']}: skills must be YAML lists")
    if expected_skills != actual_skills:
        raise EvalFailure(
            f"{case['id']}: route {actual_skills} != expected {expected_skills}"
        )
    if not set(actual_skills) <= ALLOWED_SKILLS:
        raise EvalFailure(f"{case['id']}: unknown skill in route {actual_skills}")
    if not 1 <= len(actual_skills) <= 3:
        raise EvalFailure(f"{case['id']}: route must contain one to three skills")

    checks = {
        "require_challenge": "challenge_detected",
        "require_evidence_split": "evidence_split",
        "require_action": "actionable_next_step",
        "require_correction": "corrected_direction",
        "require_persistence": "persistence_ok",
        "expected_stage_change": "stage_changed",
    }
    for case_field, result_field in checks.items():
        if case[case_field] and result[result_field] is not True:
            raise EvalFailure(f"{case['id']}: required check failed: {result_field}")

    missing_headings = sorted(
        heading for heading in REQUIRED_RESULT_HEADINGS if heading not in result_body
    )
    if missing_headings:
        raise EvalFailure(f"{case['id']}: result missing headings {missing_headings}")
    if any(
        phrase in result_body
        for phrase in ("Paul Graham 说", "齐泽克说", "段永平说", "塔勒布说", "Naval 说")
    ):
        raise EvalFailure(f"{case['id']}: user-facing result exposes persona panel")

    validate_fixture(case)


def main() -> int:
    try:
        case_paths = sorted(CASES_DIR.glob("case-*.md"))
        result_paths = sorted(RESULTS_DIR.glob("case-*.md"))
        if len(case_paths) < 8:
            raise EvalFailure(f"expected at least 8 cases, found {len(case_paths)}")
        if len(case_paths) != len(result_paths):
            raise EvalFailure(
                f"case/result count mismatch: {len(case_paths)} != {len(result_paths)}"
            )

        result_by_id: dict[str, Path] = {}
        for path in result_paths:
            data, _ = read_markdown(path)
            result_id = str(data.get("id", ""))
            if not result_id or result_id in result_by_id:
                raise EvalFailure(f"{path}: missing or duplicate id {result_id!r}")
            result_by_id[result_id] = path

        for case_path in case_paths:
            case, _ = read_markdown(case_path)
            case_id = str(case.get("id", ""))
            result_path = result_by_id.get(case_id)
            if result_path is None:
                raise EvalFailure(f"{case_path}: no result for {case_id}")
            validate_case(case_path, result_path)
            print(f"[PASS] {case_id}: {case['title']}")
    except (EvalFailure, OSError, SyntaxError, ValueError) as exc:
        print(f"[FAIL] {exc}", file=sys.stderr)
        return 1

    print(f"PASS: {len(case_paths)} / {len(case_paths)} evaluation cases")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
