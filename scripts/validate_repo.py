#!/usr/bin/env python3
"""Deterministically validate the Stage-first Reality and Human Execution V0.

This optional development tool checks repository contracts, provenance, and
workspace shape. It does not access the web, run Codex, or claim to evaluate
LLM behavior or market-research quality.
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
EVIDENCE_SKILLS = {"market-reality-researcher"}
ORCHESTRATOR_SKILLS = {"monetization-orchestrator"}
ALL_SKILLS = set(THINKING_SKILLS) | EVIDENCE_SKILLS | ORCHESTRATOR_SKILLS

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
    Path("stage-model.md"),
    Path("object-protocol.md"),
    Path("review-protocol.md"),
    Path("workspace-protocol.md"),
    Path("source-mapping.md"),
    Path("integrations/agent-reach.md"),
    Path("purchase-trigger-protocol.md"),
    Path("human-execution-protocol.md"),
    Path("evaluation-strategy.md"),
}
RESEARCHER_FILES = {
    Path("SKILL.md"),
    Path("agents/openai.yaml"),
    Path("references/research-workflow.md"),
    Path("references/source-strategy.md"),
    Path("references/query-playbook.md"),
    Path("references/case-reconstruction.md"),
    Path("references/transferability-check.md"),
    Path("references/trigger-event-search.md"),
    Path("references/deadline-signal-search.md"),
    Path("examples/local/digital-human-commerce.md"),
    Path("examples/local/adjacent-case-trap.md"),
    Path("examples/local/vendor-claim-trap.md"),
    Path("examples/local/policy-conflict.md"),
    Path("examples/local/no-exact-precedent.md"),
    Path("examples/local/deadline-opportunity.md"),
    Path("examples/local/fake-urgency.md"),
    Path("examples/local/urgent-but-unbuyable.md"),
    Path("examples/local/digital-human-deadline.md"),
}
EXPECTED_EVALS = {
    "01-new-project-auto-bootstrap.md",
    "02-premature-build.md",
    "03-first-payment.md",
    "04-repeat-payment-and-leverage.md",
    "05-large-bet.md",
    "06-stage-regression.md",
    "07-market-research-required.md",
    "08-exact-vs-adjacent.md",
    "09-vendor-claim.md",
    "10-policy-freshness.md",
    "11-success-case-non-transferable.md",
    "12-agent-reach-unavailable.md",
    "13-no-search-needed.md",
    "14-successful-pattern-first.md",
    "15-real-deadline.md",
    "16-deadline-without-consequence.md",
    "17-urgent-but-low-trust.md",
    "18-recurring-deadline.md",
    "19-one-off-deadline.md",
    "20-manufactured-urgency.md",
    "21-valid-business-without-deadline.md",
    "22-high-urgency-high-liability.md",
    "23-no-project-no-write.md",
    "24-existing-project-resume.md",
    "25-project-conflict-no-wrong-write.md",
    "26-unseen-outreach-is-not-demand-failure.md",
    "27-wrong-buyer-is-not-market-failure.md",
    "28-compliments-without-payment.md",
    "29-problem-evidence-is-not-business-evidence.md",
    "30-friend-payment-has-limited-transfer.md",
    "31-executable-customer-sourcing.md",
    "32-more-research-will-not-test-payment.md",
    "33-building-will-not-test-payment.md",
    "34-payment-with-negative-delivery-economics.md",
    "35-buyer-feedback-reroutes-the-hypothesis.md",
    "36-reachable-sample-is-not-representative.md",
    "37-content-audience-is-not-automatically-payer.md",
    "38-content-platform-can-be-market-evidence.md",
    "39-execution-does-not-validate-candidate.md",
    "40-founder-fit-is-not-market-priority.md",
    "41-content-direction-is-not-a-service-offer.md",
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
MARKET_STATE_HEADINGS = {
    "## 当前外部市场证据",
    "## 最近一次市场调查",
    "## 最接近的已验证模式",
    "## 当前政策状态",
    "## 研究覆盖缺口",
}
RESEARCH_FIELDS = {
    "Research question",
    "Scope",
    "Market / geography",
    "Target platforms",
    "Content type",
    "Started / checked date",
    "Research depth",
    "Queries used",
    "Channels actually accessed",
    "Coverage gaps",
    "Sources",
    "Supporting evidence",
    "Contradicting evidence",
    "Exact cases",
    "Adjacent cases",
    "Negative cases",
    "Policy findings",
    "User acceptance signals",
    "Competitor and pricing signals",
    "Verdict",
    "Remaining unknowns",
    "Recheck condition",
}
CASE_FIELDS = {
    "Actor",
    "Date range",
    "Market",
    "Platform",
    "Content format",
    "Scope match",
    "Target customer",
    "Payer",
    "Offer",
    "Bought result",
    "Acquisition channel",
    "Delivery model",
    "Price or revenue evidence",
    "Repeatability evidence",
    "Reported outcome",
    "Verification status",
    "Source IDs",
    "Required resources",
    "Platform dependency",
    "What appears to work",
    "Failure or risk signals",
    "Copyable components",
    "Context-dependent components",
    "Non-transferable advantages",
    "Relevance to current project",
}
SOURCE_FIELDS = {
    "id",
    "title",
    "url",
    "publisher",
    "platform",
    "source_type",
    "published_at",
    "accessed_at",
    "market",
    "claim",
    "supports",
    "contradicts",
    "authority",
    "verification",
    "freshness",
    "scope_match",
    "direction",
    "notes",
}
MARKET_EVIDENCE_FIELDS = {
    "status",
    "scope",
    "primary_market",
    "platforms",
    "content_type",
    "last_checked_at",
    "latest_research",
    "exact_precedent",
    "policy_status",
    "coverage_gaps",
}
MARKET_EVIDENCE_STATUSES = {"not_started", "partial", "current", "stale", "blocked"}
RESEARCH_VERDICTS = {
    "exact_precedent_verified",
    "exact_precedent_reported",
    "adjacent_precedent_only",
    "market_signal_exists",
    "insufficient_evidence",
    "contradicted_by_evidence",
    "policy_conditional",
    "policy_blocked",
    "research_blocked",
    "stale_research",
}
RESEARCH_DEPTHS = {"quick", "standard", "deep"}
CASE_STATUSES = {
    "exact_verified",
    "exact_corroborated",
    "exact_reported",
    "adjacent_verified",
    "adjacent_reported",
    "vendor_claim_only",
    "stale_case",
    "contradicted",
    "insufficient_evidence",
}
BUYING_SITUATION_FIELDS = {
    "Status",
    "Trigger event",
    "Deadline type",
    "Deadline source",
    "Deadline date/window",
    "Buyer",
    "Payer",
    "Beneficiary",
    "Required result",
    "Cost of delay",
    "Consequence owner",
    "Current workaround",
    "Purchase window",
    "Trust requirement",
    "Low-trust entry",
    "Frequency",
    "Observability",
    "Reachability",
    "Budget path",
    "Delivery risk",
    "Linked facts",
    "Linked assumptions",
    "Linked research",
    "Linked cases",
    "Linked experiments",
    "Linked transactions",
}
BUYING_SITUATION_STATUSES = {
    "hypothesis",
    "observed",
    "supported",
    "paid",
    "repeated",
    "weakened",
    "invalidated",
}
DEADLINE_TYPES = {
    "hard_external",
    "hard_internal",
    "rolling_operational",
    "opportunity_window",
    "soft_social",
    "seller_created",
    "fabricated",
    "none",
    "unknown",
}
PURCHASE_TRIGGER_FIELDS = {
    "status",
    "active_buying_situation",
    "trigger_event",
    "deadline_type",
    "deadline_window",
    "cost_of_delay",
    "consequence_owner",
    "purchase_window",
    "trust_barrier",
    "low_trust_entry",
    "latest_evidence",
}
PURCHASE_TRIGGER_STATUSES = {
    "not_started",
    "hypothesis",
    "partial",
    "evidenced",
    "paid",
    "repeated",
    "invalidated",
}
TRANSACTION_STATUSES = {"completed", "refunded", "discounted", "barter", "promised"}
TRANSACTION_FIELDS = {
    "Status",
    "Amount",
    "Currency",
    "Paid at",
    "Payer",
    "Customer",
    "Payment evidence",
    "Linked fact",
    "Linked buying situation",
}
EXPERIMENT_RESULT_STATUSES = {"success", "demand_failure", "invalid", "inconclusive"}
EXPERIMENT_COMPLETION_FIELDS = {
    "Result",
    "Result basis",
    "Raw evidence",
    "Observed events",
    "First broken selected step",
    "First broken layer",
    "Diagnosis basis",
    "Competing explanations",
    "Material protocol deviations",
    "Assumption updates",
    "Facts created or updated",
    "Decision updates",
    "Stage after evidence review",
    "Next experiment or action",
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

    researcher = SKILLS_ROOT / "market-reality-researcher"
    missing_researcher = [
        str(path) for path in sorted(RESEARCHER_FILES) if not (researcher / path).is_file()
    ]
    if missing_researcher:
        raise ValidationFailure(f"market researcher files missing: {missing_researcher}")
    forbidden = [researcher / "SOURCE.md", researcher / "references" / "source"]
    if any(path.exists() for path in forbidden):
        raise ValidationFailure("market-reality-researcher must not claim Persona provenance")
    researcher_text = (researcher / "SKILL.md").read_text(encoding="utf-8")
    for phrase in (
        "Evidence-Producing",
        "Closest Proven Playbook",
        "vendor_claim_only",
        "02-problem-validation",
    ):
        if phrase not in researcher_text:
            raise ValidationFailure(f"market researcher missing core contract: {phrase}")


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


def missing_labels(text: str, labels: set[str]) -> list[str]:
    return sorted(label for label in labels if label not in text)


def field_value(text: str, field: str) -> str | None:
    match = re.search(
        rf"(?mi)^\s*(?:[-*]\s*)?(?:#+\s*)?{re.escape(field)}\s*:\s*[`\"']?([^\n`\"']+)",
        text,
    )
    if match:
        return match.group(1).strip()
    heading_match = re.search(
        rf"(?mi)^\s*#+\s*{re.escape(field)}\s*\n+\s*[`\"']?([^\n`\"']+)",
        text,
    )
    return heading_match.group(1).strip() if heading_match else None


def validate_research(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    missing = missing_labels(text, RESEARCH_FIELDS)
    if missing:
        raise ValidationFailure(f"{path}: missing Research fields {missing}")
    verdict = field_value(text, "Verdict")
    if verdict not in RESEARCH_VERDICTS:
        raise ValidationFailure(f"{path}: invalid Research verdict {verdict!r}")
    depth = (
        field_value(text, "Research depth")
        or field_value(text, "research_depth")
        or field_value(text, "depth")
    )
    if depth not in RESEARCH_DEPTHS:
        raise ValidationFailure(f"{path}: invalid Research depth {depth!r}")
    missing_source_fields = missing_labels(text, SOURCE_FIELDS)
    if missing_source_fields:
        raise ValidationFailure(f"{path}: Source records missing fields {missing_source_fields}")
    research_id = path.name[:4]
    if not re.search(rf"\b{re.escape(research_id)}-S\d{{2}}\b", text):
        raise ValidationFailure(f"{path}: no local Source ID for {research_id}")


def validate_case(path: Path, known_source_ids: set[str]) -> None:
    text = path.read_text(encoding="utf-8")
    missing = missing_labels(text, CASE_FIELDS)
    if missing:
        raise ValidationFailure(f"{path}: missing Case fields {missing}")
    status = field_value(text, "Verification status")
    if status not in CASE_STATUSES:
        raise ValidationFailure(f"{path}: invalid Case verification status {status!r}")
    source_ids = set(re.findall(r"\bR\d{3}-S\d{2}\b", text))
    if not source_ids:
        raise ValidationFailure(f"{path}: Case has no Research Source ID")
    unknown_source_ids = sorted(source_ids - known_source_ids)
    if unknown_source_ids:
        raise ValidationFailure(f"{path}: unknown Research Source IDs {unknown_source_ids}")


def validate_transaction(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    if not re.fullmatch(r"T\d{3}(?:-[a-z0-9]+(?:-[a-z0-9]+)*)?\.md", path.name):
        raise ValidationFailure(
            f"{path}: Transaction filename must contain exactly one stable Txxx ID"
        )
    missing = missing_labels(text, TRANSACTION_FIELDS)
    if missing:
        raise ValidationFailure(f"{path}: missing Transaction fields {missing}")
    transaction_id = path.name[:4]
    if not re.search(rf"(?m)^#{{1,6}}\s+{re.escape(transaction_id)}\b", text):
        raise ValidationFailure(f"{path}: Transaction heading must contain {transaction_id}")
    status = field_value(text, "Status")
    if status not in TRANSACTION_STATUSES:
        raise ValidationFailure(f"{path}: invalid Transaction status {status!r}")
    if status == "completed":
        amount = field_value(text, "Amount")
        if not amount or not re.fullmatch(r"\d+(?:\.\d+)?", amount):
            raise ValidationFailure(f"{path}: invalid Transaction amount {amount!r}")
        currency = field_value(text, "Currency")
        if not currency or currency == "unknown":
            raise ValidationFailure(f"{path}: Transaction currency must be known")
        paid_at = field_value(text, "Paid at")
        if not paid_at or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", paid_at):
            raise ValidationFailure(f"{path}: invalid Transaction paid date {paid_at!r}")
        for field in ("Payer", "Customer", "Payment evidence", "Linked fact"):
            value = field_value(text, field)
            if not value or value == "unknown":
                raise ValidationFailure(f"{path}: completed Transaction {field} must be known")
        payment_evidence = field_value(text, "Payment evidence") or ""
        if re.search(r"(?i)\b(?:user|oral|chat)\s+(?:report|statement)\b", payment_evidence) or re.search(
            r"用户(?:报告|陈述)|口述", payment_evidence
        ):
            raise ValidationFailure(
                f"{path}: user report is Fact provenance, not completed payment evidence"
            )
        if not re.search(r"\bF\d{3}\b", field_value(text, "Linked fact") or ""):
            raise ValidationFailure(f"{path}: completed Transaction must link a Fact ID")
    return status


def validate_buying_situation(path: Path, known_transaction_ids: set[str]) -> str:
    text = path.read_text(encoding="utf-8")
    missing = missing_labels(text, BUYING_SITUATION_FIELDS)
    if missing:
        raise ValidationFailure(f"{path}: missing Buying Situation fields {missing}")
    situation_id = path.name[:5]
    if not re.search(rf"(?m)^#{{1,6}}\s+{re.escape(situation_id)}\b", text):
        raise ValidationFailure(f"{path}: Buying Situation heading must contain {situation_id}")
    status = field_value(text, "Status")
    if status not in BUYING_SITUATION_STATUSES:
        raise ValidationFailure(f"{path}: invalid Buying Situation status {status!r}")
    deadline_type = field_value(text, "Deadline type")
    if deadline_type not in DEADLINE_TYPES:
        raise ValidationFailure(f"{path}: invalid Deadline type {deadline_type!r}")
    if status in {"paid", "repeated"}:
        transactions = field_value(text, "Linked transactions") or ""
        linked_transaction_ids = set(re.findall(r"\bT\d{3}\b", transactions))
        if not linked_transaction_ids:
            raise ValidationFailure(
                f"{path}: {status} Buying Situation must link a Transaction ID"
            )
        unknown_transaction_ids = sorted(linked_transaction_ids - known_transaction_ids)
        if unknown_transaction_ids:
            raise ValidationFailure(
                f"{path}: unknown linked Transaction IDs {unknown_transaction_ids}"
            )
        if status == "repeated" and len(linked_transaction_ids) < 2:
            raise ValidationFailure(
                f"{path}: repeated Buying Situation requires at least two Transaction IDs"
            )
    return status


def validate_experiment(path: Path) -> None:
    """Validate only completed/result sections; legacy plan-only Exxx stays valid."""
    text = path.read_text(encoding="utf-8")
    if not re.search(r"(?m)^#{2,6}\s+Completed result\s*$", text):
        return
    completed = re.split(r"(?m)^#{2,6}\s+Completed result\s*$", text, maxsplit=1)[1]
    missing = missing_labels(completed, EXPERIMENT_COMPLETION_FIELDS)
    if missing:
        raise ValidationFailure(f"{path}: completed Experiment missing fields {missing}")
    result = field_value(completed, "Result")
    if result not in EXPERIMENT_RESULT_STATUSES:
        raise ValidationFailure(f"{path}: invalid Experiment result {result!r}")
    if not re.search(r"(?m)^#{3,6}\s+Evidence Ledger\s*$", completed):
        raise ValidationFailure(f"{path}: completed Experiment missing Evidence Ledger")
    raw_evidence = field_value(completed, "Raw evidence")
    if not raw_evidence or raw_evidence.casefold() in {"none", "unknown", "n/a"}:
        raise ValidationFailure(f"{path}: completed Experiment must link or name raw evidence")


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
        for forbidden_name in (
            "MARKET.md",
            "RESEARCH.md",
            "CASES.md",
            "SOURCES.md",
            "DEADLINE.md",
            "HUMAN-NATURE.md",
            "URGENCY.md",
            "BUYING-SITUATIONS.md",
        ):
            if (project / forbidden_name).exists():
                raise ValidationFailure(f"forbidden project-root market file: {project / forbidden_name}")

        state_path = project / "STATE.md"
        validate_state(state_path)
        parse_frontmatter_keys(project / "IDEA.md")

        for directory in (path for path in project.rglob("*") if path.is_dir()):
            if not any(path.is_file() for path in directory.rglob("*")):
                raise ValidationFailure(f"empty workspace directory is forbidden: {directory}")

        research_files = sorted(project.glob("**/research/R[0-9][0-9][0-9]-*.md"))
        case_files = sorted(project.glob("**/cases/C[0-9][0-9][0-9]-*.md"))
        buying_situation_files = sorted(
            project.glob("**/buying-situations/BS[0-9][0-9][0-9]-*.md")
        )
        experiment_files = sorted(project.glob("04-experiments/**/E[0-9][0-9][0-9]-*.md")) + sorted(
            project.glob("04-experiments/E[0-9][0-9][0-9].md")
        )
        all_research_like = sorted(project.glob("**/R[0-9][0-9][0-9]-*.md"))
        all_case_like = sorted(project.glob("**/C[0-9][0-9][0-9]-*.md"))
        all_buying_situation_like = sorted(project.glob("**/BS[0-9][0-9][0-9]-*.md"))
        all_experiment_like = sorted(
            path for path in project.rglob("*.md") if re.match(r"^E\d{3}(?:-|\.md$)", path.name)
        )
        transaction_files = sorted(
            project.glob("05-transactions/**/T[0-9][0-9][0-9]-*.md")
        ) + sorted(project.glob("05-transactions/T[0-9][0-9][0-9].md"))
        all_transaction_like = sorted(
            path for path in project.rglob("*.md") if re.match(r"^T\d{3}(?:-|\.md$)", path.name)
        )
        if research_files != all_research_like:
            raise ValidationFailure(f"{project}: Research objects must live in a research directory")
        if case_files != all_case_like:
            raise ValidationFailure(f"{project}: Case objects must live in a cases directory")
        if buying_situation_files != all_buying_situation_like:
            raise ValidationFailure(
                f"{project}: Buying Situation objects must live in a buying-situations directory"
            )
        if sorted(experiment_files) != all_experiment_like:
            raise ValidationFailure(f"{project}: Experiment objects must live under 04-experiments")
        if sorted(transaction_files) != all_transaction_like:
            raise ValidationFailure(
                f"{project}: Transaction objects must live under 05-transactions"
            )

        research_ids = [path.name[:4] for path in research_files]
        case_ids = [path.name[:4] for path in case_files]
        buying_situation_ids = [path.name[:5] for path in buying_situation_files]
        experiment_ids = [path.name[:4] for path in experiment_files]
        if (
            len(research_ids) != len(set(research_ids))
            or len(case_ids) != len(set(case_ids))
            or len(buying_situation_ids) != len(set(buying_situation_ids))
            or len(experiment_ids) != len(set(experiment_ids))
        ):
            raise ValidationFailure(
                f"{project}: duplicate Research, Case, Buying Situation, or Experiment ID"
            )
        for research in research_files:
            validate_research(research)
        known_source_ids = {
            source_id
            for research in research_files
            for source_id in re.findall(r"\bR\d{3}-S\d{2}\b", research.read_text(encoding="utf-8"))
        }
        for case in case_files:
            validate_case(case, known_source_ids)
        for experiment in experiment_files:
            validate_experiment(experiment)
        transaction_statuses = {
            path.name[:4]: validate_transaction(path) for path in transaction_files
        }
        known_transaction_ids = {
            transaction_id
            for transaction_id, status in transaction_statuses.items()
            if status == "completed"
        }
        buying_situation_statuses = {
            path.name[:5]: validate_buying_situation(path, known_transaction_ids)
            for path in buying_situation_files
        }

        state_text = state_path.read_text(encoding="utf-8")
        has_market_state = "market_evidence:" in state_text
        if has_market_state and not research_files:
            raise ValidationFailure(f"{state_path}: market_evidence exists without a Research object")
        if has_market_state:
            market_block = state_text.split("market_evidence:", 1)[1].split("---", 1)[0]
            missing_market_fields = missing_labels(market_block, MARKET_EVIDENCE_FIELDS)
            if missing_market_fields:
                raise ValidationFailure(
                    f"{state_path}: market_evidence missing fields {missing_market_fields}"
                )
            status = field_value(market_block, "status")
            if status not in MARKET_EVIDENCE_STATUSES:
                raise ValidationFailure(f"{state_path}: invalid market_evidence status {status!r}")
            latest_research = field_value(market_block, "latest_research")
            if not latest_research:
                raise ValidationFailure(f"{state_path}: market_evidence latest_research is empty")
            research_target = (project / latest_research).resolve()
            if research_target not in {path.resolve() for path in research_files}:
                raise ValidationFailure(
                    f"{state_path}: latest_research does not identify a project Research artifact"
                )
            missing = missing_labels(state_text, MARKET_STATE_HEADINGS)
            if missing:
                raise ValidationFailure(f"{state_path}: missing market evidence headings {missing}")

        has_purchase_trigger_state = "purchase_trigger:" in state_text
        if has_purchase_trigger_state and not buying_situation_files:
            raise ValidationFailure(
                f"{state_path}: purchase_trigger exists without a Buying Situation object"
            )
        if has_purchase_trigger_state:
            trigger_block = state_text.split("purchase_trigger:", 1)[1].split("---", 1)[0]
            missing_trigger_fields = missing_labels(trigger_block, PURCHASE_TRIGGER_FIELDS)
            if missing_trigger_fields:
                raise ValidationFailure(
                    f"{state_path}: purchase_trigger missing fields {missing_trigger_fields}"
                )
            trigger_status = field_value(trigger_block, "status")
            if trigger_status not in PURCHASE_TRIGGER_STATUSES:
                raise ValidationFailure(
                    f"{state_path}: invalid purchase_trigger status {trigger_status!r}"
                )
            trigger_deadline_type = field_value(trigger_block, "deadline_type")
            if trigger_deadline_type not in DEADLINE_TYPES:
                raise ValidationFailure(
                    f"{state_path}: invalid purchase_trigger deadline_type "
                    f"{trigger_deadline_type!r}"
                )
            active_id = field_value(trigger_block, "active_buying_situation")
            if active_id not in set(buying_situation_ids):
                raise ValidationFailure(
                    f"{state_path}: active_buying_situation does not identify a project BS artifact"
                )
            active_status = buying_situation_statuses[active_id]
            if trigger_status == "paid" and active_status not in {"paid", "repeated"}:
                raise ValidationFailure(
                    f"{state_path}: paid purchase_trigger requires a paid or repeated active BS"
                )
            if trigger_status == "repeated" and active_status != "repeated":
                raise ValidationFailure(
                    f"{state_path}: repeated purchase_trigger requires a repeated active BS"
                )


def validate_evals() -> None:
    readme = EVALS / "README.md"
    if not readme.is_file():
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

    required_headings = [
        "## Preconditions",
        "## User message",
        "## Expected observable behavior",
        "## Failure conditions",
    ]
    for path in cases_dir.glob("*.md"):
        text = path.read_text(encoding="utf-8")
        headings = [line for line in text.splitlines() if line.startswith("## ")]
        if headings != required_headings:
            raise ValidationFailure(
                f"{path}: behavior scenario headings must be exactly {required_headings}, found {headings}"
            )

    bootstrap = (cases_dir / "01-new-project-auto-bootstrap.md").read_text(encoding="utf-8")
    for phrase in (
        "creates exactly `IDEA.md` and `STATE.md`",
        "separate durable mutation",
        "no empty stage directory",
    ):
        if phrase not in bootstrap:
            raise ValidationFailure(f"auto-bootstrap scenario missing lazy-growth assertion: {phrase}")

    required_market_contracts = {
        "07-market-research-required.md": ("market-reality-researcher", "R001", "15."),
        "08-exact-vs-adjacent.md": ("adjacent_precedent_only", "livestream"),
        "09-vendor-claim.md": ("vendor_claim_only", "verified market FACT"),
        "10-policy-freshness.md": ("official", "checked_at"),
        "11-success-case-non-transferable.md": ("market exists", "copyable"),
        "12-agent-reach-unavailable.md": ("coverage_gap", "Web"),
        "13-no-search-needed.md": ("fresh", "E001"),
        "14-successful-pattern-first.md": ("proven", "SaaS"),
        "15-real-deadline.md": (
            "recurring_deadline_opportunity",
            "BS001",
            "Deadline Replication Experiment",
        ),
        "16-deadline-without-consequence.md": (
            "deadline_without_consequence",
            "commercial value",
        ),
        "17-urgent-but-low-trust.md": ("urgent_but_low_trust", "low-trust entry"),
        "18-recurring-deadline.md": ("rolling_operational", "leverage-designer"),
        "19-one-off-deadline.md": ("one_off_rush_service", "sustainable product"),
        "20-manufactured-urgency.md": ("fabricated", "seller_created"),
        "21-valid-business-without-deadline.md": ("deadline_type", "none"),
        "22-high-urgency-high-liability.md": (
            "high_liability_opportunity",
            "human expert review",
        ),
    }
    for name, phrases in required_market_contracts.items():
        text = (cases_dir / name).read_text(encoding="utf-8")
        for phrase in phrases:
            if phrase not in text:
                raise ValidationFailure(f"{name}: missing Market Reality assertion {phrase}")

    required_evidence_fit_contracts = {
        "36-reachable-sample-is-not-representative.md": (
            "reachability",
            "decision relevance",
            "selection bias",
            "small samples",
        ),
        "37-content-audience-is-not-automatically-payer.md": (
            "audience",
            "payer",
            "`unknown`",
            "same actor",
        ),
        "38-content-platform-can-be-market-evidence.md": (
            "market observation",
            "Reality Evidence",
            "web-first",
            "platform popularity metrics",
        ),
        "39-execution-does-not-validate-candidate.md": (
            "model-derived hypothesis",
            "founder/domain fit",
            "`market validated: false`",
            "exploratory test",
        ),
        "40-founder-fit-is-not-market-priority.md": (
            "Opportunity Evidence",
            "Investigation Advantage",
            "Market Priority #1",
            "Market Priority: unknown",
            "first exploratory test",
            "decision-capped Reality Scan",
            "universal Web First",
        ),
        "41-content-direction-is-not-a-service-offer.md": (
            "content/media archetype",
            "Candidate Monetization Mechanism",
            "service payment",
            "Market Observation Environment",
            "silent conversion",
        ),
    }
    for name, phrases in required_evidence_fit_contracts.items():
        text = (cases_dir / name).read_text(encoding="utf-8")
        for phrase in phrases:
            if phrase.casefold() not in text.casefold():
                raise ValidationFailure(
                    f"{name}: missing Evidence Fit assertion {phrase}"
                )

    required_lifecycle_contracts = {
        "23-no-project-no-write.md": (
            "Naval 和 Taleb",
            "SaaS",
            "Deadline",
            "No Project",
            "workspace/_index.md",
            "long-term project memory",
            "chat log",
            "workspace/naval-taleb/",
            "workspace/saas-pricing/",
            "workspace/deadline-business/",
        ),
        "24-existing-project-resume.md": (
            "workspace/ai-commerce-short-video/",
            "IDEA.md",
            "STATE.md",
            "resumes that stable project",
            "semantic",
            "BS001",
            "workspace/sku-video/",
            "workspace/batch-video/",
            "workspace/commerce-video-2/",
            "workspace/ai-video-new/",
        ),
        "25-project-conflict-no-wrong-write.md": (
            "workspace/ai-commerce-short-video/",
            "workspace/ai-ad-creative/",
            "Project Conflict",
            "temporary no-write",
            "FACT",
            "ASSUMPTION",
            "BSxxx",
            "RESEARCH",
            "STATE",
            "stage artifact",
            "workspace/deadline-material/",
        ),
    }
    for name, phrases in required_lifecycle_contracts.items():
        text = (cases_dir / name).read_text(encoding="utf-8")
        for phrase in phrases:
            if phrase not in text:
                raise ValidationFailure(
                    f"{name}: missing Project Lifecycle assertion {phrase}"
                )

    conflict = (cases_dir / "25-project-conflict-no-wrong-write.md").read_text(
        encoding="utf-8"
    )
    conflict_follow_ups = {
        "商品带货短视频": "ai-commerce-short-video",
        "广告投放素材": "ai-ad-creative",
    }
    for clarification, target in conflict_follow_ups.items():
        if clarification not in conflict or target not in conflict:
            raise ValidationFailure(
                "25-project-conflict-no-wrong-write.md: missing deterministic "
                f"clarification mapping {clarification!r} -> {target!r}"
            )

    eval_readme = readme.read_text(encoding="utf-8")
    describes_non_runtime = (
        "does not run Codex" in eval_readme
        or "not an automated LLM evaluation framework" in eval_readme
    )
    describes_count = "41" in eval_readme or "forty-one" in eval_readme
    if not describes_non_runtime or not describes_count:
        raise ValidationFailure("evals README must describe 41 human-auditable, non-runtime scenarios")
    for phrase in (
        "Project Lifecycle",
        "New Project Bootstrap",
        "No Project / No Write",
        "Existing Project Resume",
        "Project Conflict / No Wrong Write",
    ):
        if phrase.casefold() not in eval_readme.casefold():
            raise ValidationFailure(
                f"evals README missing Project Lifecycle classification: {phrase}"
            )
    for phrase in (
        "Human Execution and Experiment Diagnosis",
        "invalid",
        "inconclusive",
        "demand failure",
        "evaluation-strategy.md",
        "Evidence Fit and Content-Market Roles",
    ):
        if phrase.casefold() not in eval_readme.casefold():
            raise ValidationFailure(f"evals README missing VNext behavior category: {phrase}")


def validate_vnext_contracts() -> None:
    required_phrases = {
        REPO_ROOT / "README.md": (
            "Evidence-derived Stage → earliest unresolved uncertainty",
            "Reality Evidence First 不等于 Web First",
            "docs/human-execution-protocol.md",
            "保存 41 个核心 Harness Behavior Acceptance Scenarios",
            "Investigation Advantage",
            "Market Observation Environment",
        ),
        REPO_ROOT / "AGENTS.md": (
            "Why-Now Gate",
            "Stage-applicable primary Thinking Skill",
            "human-execution-protocol.md",
            "implementation_revisit_trigger",
            "Market Priority",
            "business archetype",
        ),
        SKILLS_ROOT / "monetization-orchestrator" / "SKILL.md": (
            "The full gate is conditional",
            "not a universal first lens",
            "human-execution-protocol.md",
            "claim-level evidence budget",
            "buying-situations/",
            "Opportunity Candidate comparison",
            "Market Observation Environment",
        ),
        SKILLS_ROOT / "monetization-orchestrator" / "references" / "routing-rules.md": (
            "## Canonical Stage routes",
            "opportunity_discovery",
            "scaling",
            "person-supervised Reality Contact",
            "Investigation Advantage",
            "Reachability is",
            "Market Priority: unknown",
            "first exploratory test",
        ),
        SKILLS_ROOT / "monetization-orchestrator" / "references" / "state-assessment.md": (
            "participant/audience",
            "reality-grounded repeated problem, value, consumption, or transaction pattern",
            "Reachability affects evidence acquisition",
        ),
        SKILLS_ROOT / "opportunity-finder" / "SKILL.md": (
            "light trigger",
            "observable pull",
            "Opportunity Evidence",
            "Investigation Advantage",
            "model-derived",
            "content/media Candidate",
            "Market Priority: unknown",
            "first exploratory test",
        ),
        SKILLS_ROOT / "market-reality-researcher" / "SKILL.md": (
            "Case First -> Pattern First -> Replication First",
            "Market Observation Environment",
            "Distribution Channel or dependency",
            "mainly on model synthesis",
            "insufficient_evidence",
            "Market Priority: unknown",
        ),
        SKILLS_ROOT / "assumption-challenger" / "SKILL.md": (
            "seller-created urgency",
            "purchase timing is material",
            "reachable sample",
            "Execution Packet",
        ),
        SKILLS_ROOT / "business-filter" / "SKILL.md": (
            "recurring_non_deadline_purchase",
            "observed repeat payment/usage",
            "audience value/attention flow",
            "silently convert",
        ),
        SKILLS_ROOT / "experiment-designer" / "SKILL.md": (
            "Evidence Ledger",
            "demand_failure",
            "implementation_revisit_trigger",
            "claim-level total evidence budget",
        ),
        REPO_ROOT / "docs" / "purchase-trigger-protocol.md": (
            "hard_external",
            "fabricated",
            "recurring_non_deadline_purchase",
        ),
        REPO_ROOT / "docs" / "object-protocol.md": (
            "success | demand_failure | invalid | inconclusive",
            "### Evidence Ledger",
            "Portfolio stop",
            "## OPPORTUNITY",
            "Investigation Advantage",
            "incomplete oral or chat report",
            "exactly one stable `Txxx`",
        ),
        REPO_ROOT / "docs" / "stage-model.md": (
            "repeated value pattern",
            "stable compatibility",
            "Do not force the pattern into a service problem",
        ),
        REPO_ROOT / "docs" / "workspace-protocol.md": (
            "completed result",
            "aggregate Evidence Ledger",
            "plan-only experiments require no migration",
        ),
        REPO_ROOT / "docs" / "human-execution-protocol.md": (
            "Reality Evidence First is not Web First",
            "Micro Packet",
            "implementation_revisit_trigger",
            "max_repair_reviews",
            "EPxxx",
            "## Evidence fit before contact",
            "candidate_basis_and_evidence_status",
            "does not upgrade Candidate credibility",
        ),
        REPO_ROOT / "docs" / "review-protocol.md": (
            "Candidate origin",
            "Opportunity Evidence",
            "Investigation Advantage",
            "cannot raise Market Priority",
            "first exploratory test",
        ),
        REPO_ROOT / "docs" / "evaluation-strategy.md": (
            "Arm A — Baseline",
            "Arm B — Harness",
            "Outcome-first decision rule",
            "Over-constraint penalty",
            "Baseline wins",
        ),
        SKILLS_ROOT / "market-reality-researcher" / "references" / "query-playbook.md": (
            "## Content and creator observation",
            "Market Observation Environments",
        ),
        SKILLS_ROOT / "market-reality-researcher" / "references" / "source-strategy.md": (
            "Market Observation Environment",
            "audience/value claim",
        ),
    }
    for path, phrases in required_phrases.items():
        text = path.read_text(encoding="utf-8")
        missing = [phrase for phrase in phrases if phrase not in text]
        if missing:
            raise ValidationFailure(f"{path}: missing VNext contract {missing}")

    obsolete_phrases = {
        REPO_ROOT / "README.md": (
            "business-filter（计入总共 1～2 个 Lens）+",
            "保存 22 个核心 Harness Behavior Acceptance Scenarios",
            "保存 35 个核心 Harness Behavior Acceptance Scenarios",
            "保存 39 个核心 Harness Behavior Acceptance Scenarios",
        ),
        REPO_ROOT / "AGENTS.md": (
            "Run `business-filter` for each leading concrete Opportunity",
            "business-filter` is the mandatory first",
        ),
        SKILLS_ROOT / "monetization-orchestrator" / "SKILL.md": (
            "mandatory first lens",
            "For each leading concrete Opportunity, run `business-filter` immediately",
        ),
        SKILLS_ROOT / "monetization-orchestrator" / "references" / "routing-rules.md": (
            "business-filter + assumption-challenger + experiment-designer",
            "business-filter` is the mandatory first lens",
        ),
    }
    for path, phrases in obsolete_phrases.items():
        text = path.read_text(encoding="utf-8")
        found = [phrase for phrase in phrases if phrase in text]
        if found:
            raise ValidationFailure(f"{path}: obsolete universal routing contract {found}")


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


def validate_removed_cli_and_infrastructure() -> None:
    forbidden = [
        REPO_ROOT / "scripts" / "new_project.py",
        WORKSPACE / "_templates",
        REPO_ROOT / "evals" / "run_evals.py",
    ]
    existing = [str(path.relative_to(REPO_ROOT)) for path in forbidden if path.exists()]
    if existing:
        raise ValidationFailure(f"forbidden Conversation-First artifacts still exist: {existing}")
    user_docs = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
    if "scripts/new_project.py" in user_docs or "--goal" in user_docs:
        raise ValidationFailure("README still requires manual project initialization")


def main() -> int:
    try:
        if not (REPO_ROOT / "AGENTS.md").is_file():
            raise ValidationFailure("AGENTS.md missing")
        docs_root = REPO_ROOT / "docs"
        missing_docs = sorted(str(path) for path in REQUIRED_DOCS if not (docs_root / path).is_file())
        if missing_docs:
            raise ValidationFailure(f"required docs missing: {missing_docs}")
        validate_skills()
        print("[PASS] five Thinking Skills, one evidence Skill, orchestrator, and Persona snapshots")
        validate_removed_cli_and_infrastructure()
        print("[PASS] Conversation-First V0 boundaries and removed manual initializer")
        validate_workspace()
        print("[PASS] lazy Workspace plus conditional Research/Case/Buying-Situation invariants")
        validate_vnext_contracts()
        print("[PASS] Stage-first, Reality-first Opportunity, Human Execution, and Experiment contracts")
        validate_evals()
        print("[PASS] 41 human-auditable behavior acceptance scenarios")
        validate_authored_links()
        print("[PASS] authored Markdown links")
    except (ValidationFailure, OSError) as exc:
        print(f"[FAIL] {exc}", file=sys.stderr)
        return 1
    print("PASS: deterministic development validation (no web or Codex runtime was executed)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
