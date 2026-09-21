from __future__ import annotations

from collections import defaultdict
from typing import Any


def evidence_audit(genome: dict[str, Any]) -> dict[str, Any]:
    rows: list[dict[str, Any]] = []
    by_identity: dict[str, dict[str, int]] = defaultdict(lambda: defaultdict(int))

    for gene in genome.get("genes", []):
        if not isinstance(gene, dict):
            continue
        families = {item.get("source_family_id") for item in gene.get("evidence", []) if isinstance(item, dict) and item.get("source_family_id")}
        channels = {item.get("channel") for item in gene.get("evidence", []) if isinstance(item, dict) and item.get("channel")}
        row = {
            "gene_id": gene.get("gene_id"),
            "identity_id": gene.get("identity_id"),
            "status": gene.get("status", "unknown"),
            "independent_source_families": len(families),
            "evidence_channels": sorted(channels),
            "raw_evidence_items": len(gene.get("evidence", [])),
        }
        rows.append(row)
        by_identity[row["identity_id"]][row["status"]] += 1

    return {
        "genes": rows,
        "identity_status_counts": {identity: dict(counts) for identity, counts in sorted(by_identity.items())},
        "rule": "Independent witness count is based on unique source_family_id values, never raw generation count.",
    }
