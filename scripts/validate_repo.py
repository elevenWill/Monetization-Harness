#!/usr/bin/env python3
"""Validate the V0 repository, source snapshots, workspace, and evals."""

from __future__ import annotations

import hashlib
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = REPO_ROOT / ".agents" / "skills"
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
            f"source snapshot mismatch at {snapshot}; missing={missing}, extra={extra}, changed={changed}"
        )


def parse_skill_frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    if "[TODO" in text or "TODO:" in text:
        raise ValidationFailure(f"unfinished template marker in {path}")
    match = re.match(r"\A---\n(.*?)\n---\n", text, flags=re.DOTALL)
    if not match:
        raise ValidationFailure(f"invalid Skill front matter in {path}")
    lines = match.group(1).splitlines()
    data: dict[str, str] = {}
    active_key: str | None = None
    for line in lines:
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
        raise ValidationFailure(f"skill set mismatch: expected={sorted(ALL_SKILLS)}, found={sorted(found)}")

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
            pairs = [
                (original / "LICENSE", skill / "references" / "source" / "LICENSE"),
                (original / "README.md", skill / "references" / "source" / "original-README.md"),
                (original / "SKILL.md", skill / "references" / "source" / "original-SKILL.md"),
            ]
            for source, snapshot in pairs:
                if sha256(source) != sha256(snapshot):
                    raise ValidationFailure(f"{name}: modified source snapshot {snapshot}")
            compare_tree(original / "references", skill / "references" / "source" / "references")
            compare_tree(original / "examples", skill / "examples" / "source")


def validate_workspace_template() -> None:
    workspace = REPO_ROOT / "workspace"
    template = workspace / "_templates" / "project"
    if not (workspace / "_index.md").is_file():
        raise ValidationFailure("workspace/_index.md missing")
    root_files = {path.name for path in template.iterdir() if path.is_file()}
    root_dirs = {path.name for path in template.iterdir() if path.is_dir()}
    if root_files != {"IDEA.md", "STATE.md"} or root_dirs != STAGE_DIRS:
        raise ValidationFailure(
            f"template root invariant failed: files={sorted(root_files)}, dirs={sorted(root_dirs)}"
        )
    template_text = (template / "IDEA.md").read_text(encoding="utf-8") + (
        template / "STATE.md"
    ).read_text(encoding="utf-8")
    for token in ("{{PROJECT}}", "{{CREATED_AT}}", "{{GOAL}}"):
        if token not in template_text:
            raise ValidationFailure(f"workspace template missing token {token}")

    for project in workspace.iterdir():
        if not project.is_dir() or project.name.startswith("_"):
            continue
        files = {path.name for path in project.iterdir() if path.is_file()}
        dirs = {path.name for path in project.iterdir() if path.is_dir()}
        if files != {"IDEA.md", "STATE.md"} or dirs != STAGE_DIRS:
            raise ValidationFailure(f"workspace project root invariant failed: {project}")


def validate_project_script() -> None:
    with tempfile.TemporaryDirectory(prefix="monetization-harness-eval-") as temp:
        isolated = Path(temp)
        shutil.copytree(REPO_ROOT / "workspace", isolated / "workspace")
        (isolated / "scripts").mkdir()
        shutil.copy2(REPO_ROOT / "scripts" / "new_project.py", isolated / "scripts" / "new_project.py")
        command = [
            sys.executable,
            str(isolated / "scripts" / "new_project.py"),
            "eval-project",
            "--goal",
            "Validate a repeatable paid outcome",
        ]
        completed = subprocess.run(command, cwd=isolated, text=True, capture_output=True, check=False)
        if completed.returncode != 0:
            raise ValidationFailure(f"new_project.py failed: {completed.stderr.strip()}")
        project = isolated / "workspace" / "eval-project"
        files = {path.name for path in project.iterdir() if path.is_file()}
        dirs = {path.name for path in project.iterdir() if path.is_dir()}
        if files != {"IDEA.md", "STATE.md"} or dirs != STAGE_DIRS:
            raise ValidationFailure("new_project.py produced an invalid project root")
        generated = (project / "IDEA.md").read_text(encoding="utf-8") + (
            project / "STATE.md"
        ).read_text(encoding="utf-8")
        if "{{" in generated or "eval-project" not in generated:
            raise ValidationFailure("new_project.py did not replace template tokens")
        index = (isolated / "workspace" / "_index.md").read_text(encoding="utf-8")
        if "[eval-project](eval-project/STATE.md)" not in index:
            raise ValidationFailure("new_project.py did not update the workspace index")

        duplicate = subprocess.run(command, cwd=isolated, text=True, capture_output=True, check=False)
        if duplicate.returncode == 0 or "refusing to overwrite" not in duplicate.stderr:
            raise ValidationFailure("new_project.py failed to reject overwrite")


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


def run_evals() -> None:
    completed = subprocess.run(
        [sys.executable, str(REPO_ROOT / "evals" / "run_evals.py")],
        cwd=REPO_ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    if completed.returncode != 0:
        raise ValidationFailure(completed.stderr.strip() or completed.stdout.strip())
    print(completed.stdout.rstrip())


def main() -> int:
    try:
        if not (REPO_ROOT / "AGENTS.md").is_file():
            raise ValidationFailure("AGENTS.md missing")
        docs = {path.name for path in (REPO_ROOT / "docs").glob("*.md")}
        if not REQUIRED_DOCS <= docs:
            raise ValidationFailure(f"required docs missing: {sorted(REQUIRED_DOCS - docs)}")
        validate_skills()
        print("[PASS] six repo-level Skills and source snapshots")
        validate_workspace_template()
        print("[PASS] workspace template and root invariants")
        validate_project_script()
        print("[PASS] isolated new-project creation and overwrite protection")
        validate_authored_links()
        print("[PASS] authored Markdown links")
        run_evals()
    except (ValidationFailure, OSError) as exc:
        print(f"[FAIL] {exc}", file=sys.stderr)
        return 1
    print("PASS: Monetization Decision Harness V0 repository validation")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
