from __future__ import annotations

from collections import Counter
from typing import Any

from .model import ALL_STATUSES, CARRIERS, EVIDENCE_CHANNELS, PROMOTED_STATUSES, ValidationIssue


def _duplicates(values: list[str]) -> set[str]:
    counts = Counter(values)
    return {value for value, count in counts.items() if count > 1}


def validate_corpus(corpus: dict[str, Any]) -> list[ValidationIssue]:
    issues: list[ValidationIssue] = []
    if corpus.get("schema_version") != 1:
        issues.append(ValidationIssue("error", "corpus.schema_version", "schema_version must be 1", "schema_version"))

    families = corpus.get("source_families", [])
    records = corpus.get("sources", [])
    family_ids = [item.get("family_id", "") for item in families if isinstance(item, dict)]
    source_ids = [item.get("source_id", "") for item in records if isinstance(item, dict)]

    for duplicate in sorted(_duplicates([x for x in family_ids if x])):
        issues.append(ValidationIssue("error", "corpus.duplicate_family", f"Duplicate family_id: {duplicate}"))
    for duplicate in sorted(_duplicates([x for x in source_ids if x])):
        issues.append(ValidationIssue("error", "corpus.duplicate_source", f"Duplicate source_id: {duplicate}"))

    family_set = set(family_ids)
    record_members: dict[str, set[str]] = {family_id: set() for family_id in family_set}
    for index, record in enumerate(records):
        if not isinstance(record, dict):
            issues.append(ValidationIssue("error", "corpus.source_type", "Source must be an object", f"sources[{index}]"))
            continue
        source_id = record.get("source_id")
        family_id = record.get("source_family_id")
        if not source_id:
            issues.append(ValidationIssue("error", "corpus.source_id", "Source requires source_id", f"sources[{index}]"))
        if family_id not in family_set:
            issues.append(ValidationIssue("error", "corpus.unknown_family", f"Source {source_id!r} references unknown family {family_id!r}", f"sources[{index}].source_family_id"))
        else:
            record_members[family_id].add(source_id)
        authority = record.get("authority", "unknown")
        if authority not in ALL_STATUSES:
            issues.append(ValidationIssue("error", "corpus.authority", f"Invalid authority {authority!r}", f"sources[{index}].authority"))

    for index, family in enumerate(families):
        if not isinstance(family, dict):
            continue
        family_id = family.get("family_id")
        declared = set(family.get("member_source_ids", []))
        observed = record_members.get(family_id, set())
        if declared != observed:
            issues.append(
                ValidationIssue(
                    "warning",
                    "corpus.family_membership_drift",
                    f"Family {family_id!r} declares {sorted(declared)} but corpus records imply {sorted(observed)}",
                    f"source_families[{index}].member_source_ids",
                )
            )
    return issues


def validate_genome(genome: dict[str, Any], corpus: dict[str, Any] | None = None) -> list[ValidationIssue]:
    issues: list[ValidationIssue] = []
    if genome.get("schema_version") != 1:
        issues.append(ValidationIssue("error", "genome.schema_version", "schema_version must be 1", "schema_version"))

    identities = genome.get("identities", [])
    genes = genome.get("genes", [])
    identity_ids = [item.get("identity_id", "") for item in identities if isinstance(item, dict)]
    gene_ids = [item.get("gene_id", "") for item in genes if isinstance(item, dict)]

    for duplicate in sorted(_duplicates([x for x in identity_ids if x])):
        issues.append(ValidationIssue("error", "genome.duplicate_identity", f"Duplicate identity_id: {duplicate}"))
    for duplicate in sorted(_duplicates([x for x in gene_ids if x])):
        issues.append(ValidationIssue("error", "genome.duplicate_gene", f"Duplicate gene_id: {duplicate}"))

    identity_set = set(identity_ids)
    corpus_family_ids = set()
    corpus_source_ids = set()
    if corpus is not None:
        corpus_family_ids = {x.get("family_id") for x in corpus.get("source_families", []) if isinstance(x, dict)}
        corpus_source_ids = {x.get("source_id") for x in corpus.get("sources", []) if isinstance(x, dict)}
        issues.extend(validate_corpus(corpus))

    for index, gene in enumerate(genes):
        path = f"genes[{index}]"
        if not isinstance(gene, dict):
            issues.append(ValidationIssue("error", "genome.gene_type", "Gene must be an object", path))
            continue
        gene_id = gene.get("gene_id")
        identity_id = gene.get("identity_id")
        status = gene.get("status", "unknown")
        carriers = set(gene.get("carriers", []))
        weight = gene.get("weight", 1.0)
        evidence = gene.get("evidence", [])

        if not gene_id:
            issues.append(ValidationIssue("error", "genome.gene_id", "Gene requires gene_id", path))
        if identity_id not in identity_set:
            issues.append(ValidationIssue("error", "genome.unknown_identity", f"Gene {gene_id!r} references unknown identity {identity_id!r}", f"{path}.identity_id"))
        if status not in ALL_STATUSES:
            issues.append(ValidationIssue("error", "genome.status", f"Invalid gene status {status!r}", f"{path}.status"))
        if not carriers:
            issues.append(ValidationIssue("error", "genome.carriers", f"Gene {gene_id!r} requires at least one carrier", f"{path}.carriers"))
        for carrier in sorted(carriers - CARRIERS):
            issues.append(ValidationIssue("error", "genome.carrier", f"Unknown carrier {carrier!r}", f"{path}.carriers"))
        if not isinstance(weight, (int, float)) or weight <= 0:
            issues.append(ValidationIssue("error", "genome.weight", f"Gene {gene_id!r} weight must be positive", f"{path}.weight"))
        if gene.get("required_for_recognition") and carriers == {"production"}:
            issues.append(ValidationIssue("error", "genome.production_only_identity", f"Gene {gene_id!r} cannot make production style alone identity-bearing", path))

        evidence_families: set[str] = set()
        evidence_channels: set[str] = set()
        for evidence_index, item in enumerate(evidence):
            epath = f"{path}.evidence[{evidence_index}]"
            if not isinstance(item, dict):
                issues.append(ValidationIssue("error", "genome.evidence_type", "Evidence must be an object", epath))
                continue
            channel = item.get("channel")
            family_id = item.get("source_family_id")
            source_id = item.get("source_id")
            if channel not in EVIDENCE_CHANNELS:
                issues.append(ValidationIssue("error", "genome.evidence_channel", f"Invalid evidence channel {channel!r}", f"{epath}.channel"))
            else:
                evidence_channels.add(channel)
            if family_id:
                evidence_families.add(family_id)
                if corpus is not None and family_id not in corpus_family_ids:
                    issues.append(ValidationIssue("error", "genome.evidence_family", f"Evidence references unknown source family {family_id!r}", epath))
            if source_id and corpus is not None and source_id not in corpus_source_ids:
                issues.append(ValidationIssue("error", "genome.evidence_source", f"Evidence references unknown source {source_id!r}", epath))

        if status == "canonical" and "canonical" not in evidence_channels:
            issues.append(ValidationIssue("error", "genome.canonical_without_authority", f"Canonical gene {gene_id!r} requires canonical-channel evidence", path))
        if status == "strongly-supported":
            if len(evidence_families) < 2:
                issues.append(ValidationIssue("error", "genome.pseudoreplication", f"Strongly-supported gene {gene_id!r} requires at least two independent source families", path))
            if not ({"audio", "structural"} & evidence_channels):
                issues.append(ValidationIssue("error", "genome.no_realization_evidence", f"Strongly-supported gene {gene_id!r} requires audio or structural realization evidence", path))
        if status in PROMOTED_STATUSES and not evidence:
            issues.append(ValidationIssue("error", "genome.promoted_without_evidence", f"Promoted gene {gene_id!r} has no evidence", path))

    gene_set = set(gene_ids)
    for index, identity in enumerate(identities):
        if not isinstance(identity, dict):
            continue
        declared = set(identity.get("gene_ids", []))
        missing = declared - gene_set
        if missing:
            issues.append(ValidationIssue("error", "genome.identity_gene_missing", f"Identity {identity.get('identity_id')!r} references missing genes {sorted(missing)}", f"identities[{index}].gene_ids"))

    return issues


def summarize_issues(issues: list[ValidationIssue]) -> dict[str, Any]:
    return {
        "valid": not any(issue.level == "error" for issue in issues),
        "errors": sum(issue.level == "error" for issue in issues),
        "warnings": sum(issue.level == "warning" for issue in issues),
        "issues": [issue.as_dict() for issue in issues],
    }
