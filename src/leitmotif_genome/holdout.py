from __future__ import annotations

import hashlib
from typing import Any


def deterministic_holdout(corpus: dict[str, Any], fraction: float = 0.25) -> dict[str, Any]:
    if not 0 < fraction < 1:
        raise ValueError("fraction must be between 0 and 1")

    family_ids = sorted(
        family.get("family_id")
        for family in corpus.get("source_families", [])
        if isinstance(family, dict) and family.get("family_id")
    )
    if len(family_ids) < 2:
        return {
            "training_family_ids": family_ids,
            "holdout_family_ids": [],
            "warning": "At least two independent source families are required for a meaningful holdout.",
        }

    ranked = sorted(
        family_ids,
        key=lambda value: hashlib.sha256(value.encode("utf-8")).hexdigest(),
    )
    holdout_count = max(1, min(len(ranked) - 1, round(len(ranked) * fraction)))
    holdout = sorted(ranked[:holdout_count])
    training = sorted(set(family_ids) - set(holdout))
    return {
        "training_family_ids": training,
        "holdout_family_ids": holdout,
        "fraction_requested": fraction,
        "family_count": len(family_ids),
    }
