from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

PROMOTED_STATUSES = {"canonical", "strongly-supported"}
ALL_STATUSES = {"canonical", "strongly-supported", "tentative", "unknown"}
EVIDENCE_CHANNELS = {"audio", "structural", "documentary", "canonical"}
CARRIERS = {
    "interval",
    "rhythm",
    "harmony",
    "melody",
    "timbre",
    "vocal",
    "structure",
    "absence",
    "production",
}


@dataclass(slots=True)
class ValidationIssue:
    level: str
    code: str
    message: str
    path: str = ""

    def as_dict(self) -> dict[str, str]:
        return {
            "level": self.level,
            "code": self.code,
            "message": self.message,
            "path": self.path,
        }


@dataclass(slots=True)
class ConformanceResult:
    candidate_id: str
    target_identity: str
    classification: str
    score: float
    possible_weight: float
    earned_weight: float
    missing_required_genes: list[str] = field(default_factory=list)
    forbidden_drift: list[str] = field(default_factory=list)
    unknown_genes: list[str] = field(default_factory=list)
    notes: list[str] = field(default_factory=list)

    def as_dict(self) -> dict[str, Any]:
        return {
            "candidate_id": self.candidate_id,
            "target_identity": self.target_identity,
            "classification": self.classification,
            "score": round(self.score, 4),
            "possible_weight": self.possible_weight,
            "earned_weight": self.earned_weight,
            "missing_required_genes": self.missing_required_genes,
            "forbidden_drift": self.forbidden_drift,
            "unknown_genes": self.unknown_genes,
            "notes": self.notes,
        }
