#!/usr/bin/env python3
"""Deterministically validate the Conversation-First V0 repository.

This development tool checks file contracts and provenance. It does not run
Codex or claim to evaluate LLM behavior.
"""

from __future__ import annotations

import hashlib
import re
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = REPO_ROOT / ".agents" / "skills"
WORKSPACE = REPO_ROOT / "workspace"
EVALS = REPO_ROOT / "evals"
THINKING_SKILLS = {
    "opportunity-finder": Path("/Users/lei/Downloads/0813/paul-graham-skill"),
    "assumption-challenger": Path("/Users/lei/Downloads/0813/zizek-skill"),
    "business-filter": Path("/Users/lei/Downloads/0813/duan-yongping-skill"),
    "experiment-designer": Path("/Users/lei/Downloads/0813/taleb-skill"),
    "leverage-designer": Path("/Users/lei/Downloads/0813/naval-skill"),
}
ALL_SKILLS = set(THINKING_SKILLS) | {"monetization-orchestrator"}
STAGE_DIRS = {
    "01-opportunity",
    "02-problem-validation",
    "03-business-validation",
    "04-experiments",
    "05-transactions",
    "06-leverage",
    "07-productization",
    "08-scaling",
    "99-archive",
}
REQUIRED_DOCS = {
    "stage-model.md",
    "object-protocol.md",
    "review-protocol.md",
    "workspace-protocol.md",
    "source-mapping.md",
}
EXPECTED_EVALS = {
    "01-new-project-auto-bootstrap.md",
    "02-premature-build.md",
    "03-first-payment.md",
    "04-repeat-payment-and-leverage.md",
    "05-large-bet.md",
    "06-stage-regression.md",
}
REQUIRED_STATE_HEADINGS = {
    "## 当前目标",
    "## 已确认事实 FACTS",
    "## 当前假设 ASSUMPTIONS",
    "## 最大未知量",
    "## 当前最大风险",
    "## 当前实验",
    "## 当前下一步",
    "## 为什么这是下一步",
    "## 最近一次状态变化",
    "## 相关材料",
}


class ValidationFailure(Exception):
    pass


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def compare_tree(source: Path, snapshot: Path) -> None:
    source_files = {
        path.relative_to(source): sha256(path)
        for path in source.rglob("*")
        if path.is_file()
    }
    snapshot_files = {
        path.relative_to(snapshot): sha256(path)
        for path in snapshot.rglob("*")
        if path.is_file()
    }
    if source_files != snapshot_files:
        missing = sorted(str(path) for path in source_files.keys() - snapshot_files.keys())
        extra = sorted(str(path) for path in snapshot_files.keys() - source_files.keys())
        changed = sorted(
            str(path)
            for path in source_files.keys() & snapshot_files.keys()
            if source_files[path] != snapshot_files[path]
        )
        raise ValidationFailure(
            f"source snapshot mismatch at {snapshot}; "
            f"missing={missing}, extra={extra}, changed={changed}"
        )


def parse_skill_frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    if "[TODO" in text or "TODO:" in text:
        raise ValidationFailure(f"unfinished template marker in {path}")
    match = re.match(r"\A---\n(.*?)\n---\n", text, flags=re.DOTALL)
    if not match:
        raise ValidationFailure(f"invalid Skill front matter in {path}")
    data: dict[str, str] = {}
    active_key: str | None = None
    for line in match.group(1).splitlines():
        if line.startswith("  ") and active_key:
            data[active_key] += " " + line.strip()
            continue
        if ":" not in line:
            raise ValidationFailure(f"invalid Skill front matter line in {path}: {line}")
        key, value = line.split(":", 1)
        active_key = key.strip()
        data[active_key] = value.strip()
    if set(data) != {"name", "description"}:
        raise ValidationFailure(f"{path}: front matter must contain only name and description")
    return data


def validate_skills() -> None:
    found = {path.name for path in SKILLS_ROOT.iterdir() if path.is_dir()}
    if found != ALL_SKILLS:
        raise ValidationFailure(
            f"skill set mismatch: expected={sorted(ALL_SKILLS)}, found={sorted(found)}"
        )

    for name in sorted(ALL_SKILLS):
        skill = SKILLS_ROOT / name
        data = parse_skill_frontmatter(skill / "SKILL.md")
        if data["name"] != name or len(data["description"]) < 80:
            raise ValidationFailure(f"{name}: invalid name or insufficient trigger description")
        if not (skill / "agents" / "openai.yaml").is_file():
            raise ValidationFailure(f"{name}: agents/openai.yaml missing")
        if not (skill / "references").is_dir():
            raise ValidationFailure(f"{name}: references directory missing")

    for name, original in THINKING_SKILLS.items():
        skill = SKILLS_ROOT / name
        required = {
            skill / "SOURCE.md",
            skill / "references" / "domain-core.md",
            skill / "references" / "source" / "LICENSE",
            skill / "references" / "source" / "original-README.md",
            skill / "references" / "source" / "original-SKILL.md",
            skill / "examples" / "local" / "monetization-cases.md",
        }
        missing = [str(path) for path in required if not path.is_file()]
        if missing:
            raise ValidationFailure(f"{name}: missing source wrapper files {missing}")
        if not any((skill / "examples" / "source").rglob("*.md")):
            raise ValidationFailure(f"{name}: source examples missing")
        if not any((skill / "references" / "source" / "references").rglob("*.md")):
            raise ValidationFailure(f"{name}: source references missing")

        if original.is_dir():
            file_pairs = [
                (original / "LICENSE", skill / "references" / "source" / "LICENSE"),
                (original / "README.md", skill / "references" / "source" / "original-README.md"),
                (original / "SKILL.md", skill / "references" / "source" / "original-SKILL.md"),
            ]
            if name == "business-filter":
                file_pairs.append(
                    (
                        original / "README_EN.md",
                        skill / "references" / "source" / "original-README_EN.md",
                    )
                )
            for source, snapshot in file_pairs:
                if not snapshot.is_file() or sha256(source) != sha256(snapshot):
                    raise ValidationFailure(f"{name}: modified or missing source snapshot {snapshot}")
            compare_tree(original / "references", skill / "references" / "source" / "references")
            compare_tree(original / "examples", skill / "examples" / "source")


def parse_frontmatter_keys(path: Path) -> set[str]:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---\n", text, flags=re.DOTALL)
    if not match:
        raise ValidationFailure(f"missing YAML front matter in {path}")
    return {
        line.split(":", 1)[0].strip()
        for line in match.group(1).splitlines()
        if line and not line.startswith((" ", "\t")) and ":" in line
    }


def validate_state(path: Path) -> None:
    keys = parse_frontmatter_keys(path)
    required_keys = {"project", "stage", "status", "updated_at", "transactions", "next_gate"}
    if not required_keys <= keys:
        raise ValidationFailure(f"{path}: missing STATE front matter keys {sorted(required_keys - keys)}")
    text = path.read_text(encoding="utf-8")
    missing_headings = sorted(heading for heading in REQUIRED_STATE_HEADINGS if heading not in text)
    if missing_headings:
        raise ValidationFailure(f"{path}: missing STATE headings {missing_headings}")


def validate_workspace() -> None:
    if not (WORKSPACE / "_index.md").is_file():
        raise ValidationFailure("workspace/_index.md missing")
    if (WORKSPACE / "_templates").exists():
        raise ValidationFailure("workspace/_templates must not exist in Conversation-First V0")

    unexpected_root_files = {
        path.name for path in WORKSPACE.iterdir() if path.is_file() and path.name != "_index.md"
    }
    if unexpected_root_files:
        raise ValidationFailure(f"unexpected workspace root files: {sorted(unexpected_root_files)}")

    for project in WORKSPACE.iterdir():
        if not project.is_dir() or project.name.startswith("_"):
            continue
        files = {path.name for path in project.iterdir() if path.is_file()}
        directories = {path.name for path in project.iterdir() if path.is_dir()}
        if files != {"IDEA.md", "STATE.md"}:
            raise ValidationFailure(
                f"{project}: root files must be exactly IDEA.md and STATE.md, found {sorted(files)}"
            )
        if not directories <= STAGE_DIRS:
            raise ValidationFailure(
                f"{project}: unknown Stage directories {sorted(directories - STAGE_DIRS)}"
            )
        validate_state(project / "STATE.md")
        parse_frontmatter_keys(project / "IDEA.md")
        for directory in (path for path in project.rglob("*") if path.is_dir()):
            if not any(path.is_file() for path in directory.rglob("*")):
                raise ValidationFailure(f"empty workspace directory is forbidden: {directory}")


def validate_evals() -> None:
    if not (EVALS / "README.md").is_file():
        raise ValidationFailure("evals/README.md missing")
    cases_dir = EVALS / "cases"
    found = {path.name for path in cases_dir.glob("*.md")}
    if found != EXPECTED_EVALS:
        raise ValidationFailure(
            f"behavior scenario set mismatch: expected={sorted(EXPECTED_EVALS)}, found={sorted(found)}"
        )
    forbidden = [EVALS / "results", EVALS / "fixtures", EVALS / "run_evals.py"]
    existing = [str(path.relative_to(REPO_ROOT)) for path in forbidden if path.exists()]
    if existing:
        raise ValidationFailure(f"obsolete pseudo-eval artifacts still exist: {existing}")

    required_headings = {
        "## Preconditions",
        "## User message",
        "## Expected observable behavior",
        "## Failure conditions",
    }
    for path in cases_dir.glob("*.md"):
        text = path.read_text(encoding="utf-8")
        missing = sorted(heading for heading in required_headings if heading not in text)
        if missing:
            raise ValidationFailure(f"{path}: missing behavior scenario headings {missing}")

    bootstrap = (cases_dir / "01-new-project-auto-bootstrap.md").read_text(encoding="utf-8")
    for phrase in ("exactly `IDEA.md` and `STATE.md`", "no empty stage directory", "04-experiments"):
        if phrase not in bootstrap:
            raise ValidationFailure(f"auto-bootstrap scenario missing lazy-growth assertion: {phrase}")


def validate_authored_links() -> None:
    for path in REPO_ROOT.rglob("*.md"):
        relative = path.relative_to(REPO_ROOT)
        if "references/source" in str(relative) or "examples/source" in str(relative):
            continue
        text = path.read_text(encoding="utf-8")
        prose = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
        for raw_link in re.findall(r"\[[^]]+\]\(([^)]+)\)", prose):
            if "://" in raw_link or raw_link.startswith(("#", "mailto:")):
                continue
            link = raw_link.split("#", 1)[0]
            if not link or "{{" in link:
                continue
            target = (path.parent / link).resolve()
            if not target.exists():
                raise ValidationFailure(f"broken link in {relative}: {raw_link}")


def validate_removed_cli() -> None:
    forbidden = [REPO_ROOT / "scripts" / "new_project.py", WORKSPACE / "_templates"]
    existing = [str(path.relative_to(REPO_ROOT)) for path in forbidden if path.exists()]
    if existing:
        raise ValidationFailure(f"manual project-initialization artifacts still exist: {existing}")
    user_docs = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
    if "scripts/new_project.py" in user_docs or "--goal" in user_docs:
        raise ValidationFailure("README still requires manual project initialization")


def main() -> int:
    try:
        if not (REPO_ROOT / "AGENTS.md").is_file():
            raise ValidationFailure("AGENTS.md missing")
        docs = {path.name for path in (REPO_ROOT / "docs").glob("*.md")}
        if not REQUIRED_DOCS <= docs:
            raise ValidationFailure(f"required docs missing: {sorted(REQUIRED_DOCS - docs)}")
        validate_skills()
        print("[PASS] six repo-level Skills and unmodified Persona source snapshots")
        validate_removed_cli()
        print("[PASS] manual project initializer and template tree are absent")
        validate_workspace()
        print("[PASS] Conversation-First workspace and lazy materialization invariants")
        validate_evals()
        print("[PASS] six human-auditable behavior acceptance scenarios")
        validate_authored_links()
        print("[PASS] authored Markdown links")
    except (ValidationFailure, OSError) as exc:
        print(f"[FAIL] {exc}", file=sys.stderr)
        return 1
    print("PASS: deterministic V0 development validation (no Codex runtime was executed)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
