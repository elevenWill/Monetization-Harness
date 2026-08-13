#!/usr/bin/env python3
"""Create one workspace project from the V0 template."""

from __future__ import annotations

import argparse
import re
import shutil
import sys
from datetime import date
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
WORKSPACE = REPO_ROOT / "workspace"
TEMPLATE = WORKSPACE / "_templates" / "project"
INDEX = WORKSPACE / "_index.md"
PROJECT_PATTERN = re.compile(r"^[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?$")
ROOT_FILES = {"IDEA.md", "STATE.md"}
ROOT_DIRS = {
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


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Initialize workspace/<project> and add it to workspace/_index.md."
    )
    parser.add_argument(
        "project",
        help="lowercase slug using letters, digits, and hyphens (max 63 chars)",
    )
    parser.add_argument(
        "--goal",
        required=True,
        help="one-line outcome to place in IDEA.md, STATE.md, and the workspace index",
    )
    return parser.parse_args()


def validate_inputs(project: str, goal: str) -> None:
    if not PROJECT_PATTERN.fullmatch(project):
        raise ValueError(
            "project must be a lowercase 1-63 character slug using letters, digits, and hyphens"
        )
    if "\n" in goal or "\r" in goal or not goal.strip():
        raise ValueError("goal must be one non-empty line")
    if "{{" in goal or "}}" in goal:
        raise ValueError("goal cannot contain template delimiters")


def replace_template_tokens(project_dir: Path, project: str, goal: str) -> None:
    replacements = {
        "{{PROJECT}}": project,
        "{{CREATED_AT}}": date.today().isoformat(),
        "{{GOAL}}": goal.strip(),
    }
    for name in sorted(ROOT_FILES):
        path = project_dir / name
        content = path.read_text(encoding="utf-8")
        for token, value in replacements.items():
            content = content.replace(token, value)
        if "{{" in content or "}}" in content:
            raise RuntimeError(f"unresolved template token in {path}")
        path.write_text(content, encoding="utf-8")


def verify_root(project_dir: Path) -> None:
    files = {path.name for path in project_dir.iterdir() if path.is_file()}
    directories = {path.name for path in project_dir.iterdir() if path.is_dir()}
    if files != ROOT_FILES:
        raise RuntimeError(
            f"project root files must be {sorted(ROOT_FILES)}, found {sorted(files)}"
        )
    if directories != ROOT_DIRS:
        missing = sorted(ROOT_DIRS - directories)
        extra = sorted(directories - ROOT_DIRS)
        raise RuntimeError(f"project stage directories mismatch; missing={missing}, extra={extra}")


def escape_table_cell(value: str) -> str:
    return value.replace("|", "\\|")


def add_index_row(project: str, goal: str) -> None:
    content = INDEX.read_text(encoding="utf-8")
    project_link = f"[{project}]({project}/STATE.md)"
    if project_link in content:
        raise RuntimeError(f"workspace index already contains {project}")
    row = (
        f"| {project_link} | {escape_table_cell(goal.strip())} | "
        f"opportunity_discovery | active | defined_problem_and_customer | "
        f"{date.today().isoformat()} |\n"
    )
    INDEX.write_text(content.rstrip() + "\n" + row, encoding="utf-8")


def main() -> int:
    args = parse_args()
    try:
        validate_inputs(args.project, args.goal)
        if not TEMPLATE.is_dir() or not INDEX.is_file():
            raise RuntimeError("workspace template or index is missing")
        project_dir = WORKSPACE / args.project
        if project_dir.exists():
            raise FileExistsError(f"refusing to overwrite existing project: {project_dir}")

        shutil.copytree(TEMPLATE, project_dir)
        replace_template_tokens(project_dir, args.project, args.goal)
        verify_root(project_dir)
        add_index_row(args.project, args.goal)
    except (ValueError, RuntimeError, FileExistsError, OSError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    print(f"Created {project_dir.relative_to(REPO_ROOT)}")
    print(f"Next: tell Codex to resume workspace/{args.project} and read IDEA.md + STATE.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
