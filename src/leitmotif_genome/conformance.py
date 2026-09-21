from __future__ import annotations

from typing import Any

from .model import ConformanceResult

COUNTABLE_STATUSES = {"canonical", "strongly-supported", "tentative"}


def _index_genes(genome: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {
        gene["gene_id"]: gene
        for gene in genome.get("genes", [])
        if isinstance(gene, dict) and gene.get("gene_id")
    }


def evaluate_candidate(genome: dict[str, Any], candidate: dict[str, Any], target_identity: str) -> ConformanceResult:
    genes = _index_genes(genome)
    target_genes = [
        gene
        for gene in genes.values()
        if gene.get("identity_id") == target_identity
        and gene.get("status") in COUNTABLE_STATUSES
        and gene.get("count_for_conformance", True)
    ]

    candidate_id = candidate.get("candidate_id", "unnamed-candidate")
    expressed = {
        item.get("gene_id"): item
        for item in candidate.get("expressed_genes", [])
        if isinstance(item, dict) and item.get("gene_id")
    }

    if not target_genes:
        return ConformanceResult(
            candidate_id=candidate_id,
            target_identity=target_identity,
            classification="insufficient-evidence",
            score=0.0,
            possible_weight=0.0,
            earned_weight=0.0,
            notes=["The registry has no evidence-bearing genes for this identity. Surface resemblance is not scored."],
        )

    possible_weight = 0.0
    earned_weight = 0.0
    missing_required: list[str] = []
    forbidden_drift: list[str] = []
    notes: list[str] = []

    target_gene_ids = {gene["gene_id"] for gene in target_genes}
    unknown_genes = sorted(set(expressed) - set(genes))

    for gene in target_genes:
        gene_id = gene["gene_id"]
        weight = float(gene.get("weight", 1.0))
        possible_weight += weight
        expression = expressed.get(gene_id)
        if expression is None:
            if gene.get("required_for_recognition", False):
                missing_required.append(gene_id)
            continue

        required_invariants = set(gene.get("invariants", []))
        preserved = set(expression.get("preserved_invariants", []))
        if required_invariants:
            coverage = len(required_invariants & preserved) / len(required_invariants)
        else:
            coverage = 1.0

        mutations = set(expression.get("mutations", []))
        forbidden = mutations & set(gene.get("forbidden_mutations", []))
        if forbidden:
            forbidden_drift.extend(f"{gene_id}:{mutation}" for mutation in sorted(forbidden))
            notes.append(f"{gene_id} expresses forbidden drift; its weight is not earned.")
            continue

        earned_weight += weight * coverage
        if coverage < 1.0:
            notes.append(f"{gene_id} preserves {coverage:.0%} of registered invariants.")

    score = earned_weight / possible_weight if possible_weight else 0.0
    expressed_target_count = len(target_gene_ids & set(expressed))

    if expressed_target_count == 0:
        classification = "counterfeit"
    elif forbidden_drift or missing_required:
        classification = "nonconforming"
    elif score >= 0.75:
        classification = "conforming"
    elif score >= 0.45:
        classification = "boundary"
    else:
        classification = "counterfeit"

    if candidate.get("surface_traits") and expressed_target_count == 0:
        notes.append("Surface/production resemblance was present but correctly contributed no identity score.")

    return ConformanceResult(
        candidate_id=candidate_id,
        target_identity=target_identity,
        classification=classification,
        score=score,
        possible_weight=possible_weight,
        earned_weight=earned_weight,
        missing_required_genes=sorted(missing_required),
        forbidden_drift=sorted(set(forbidden_drift)),
        unknown_genes=unknown_genes,
        notes=notes,
    )
