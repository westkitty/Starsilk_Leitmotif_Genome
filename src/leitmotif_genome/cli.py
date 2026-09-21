from __future__ import annotations

import argparse
import json
import sys

from .audit import evidence_audit
from .conformance import evaluate_candidate
from .holdout import deterministic_holdout
from .io import load_json
from .validate import summarize_issues, validate_genome


def _print(data: object) -> None:
    print(json.dumps(data, indent=2, ensure_ascii=False, sort_keys=True))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="starsilk-genome", description="Evidence-gated Starsilk leitmotif heredity toolkit")
    sub = parser.add_subparsers(dest="command", required=True)

    validate = sub.add_parser("validate", help="Validate a genome and optional corpus manifest")
    validate.add_argument("--genome", required=True)
    validate.add_argument("--corpus")

    audit = sub.add_parser("audit", help="Summarize evidence independence and channels")
    audit.add_argument("--genome", required=True)

    conform = sub.add_parser("conform", help="Evaluate a candidate against one identity")
    conform.add_argument("--genome", required=True)
    conform.add_argument("--candidate", required=True)
    conform.add_argument("--identity", required=True)

    holdout = sub.add_parser("holdout", help="Create deterministic source-family train/holdout groups")
    holdout.add_argument("--corpus", required=True)
    holdout.add_argument("--fraction", type=float, default=0.25)

    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)

    if args.command == "validate":
        genome = load_json(args.genome)
        corpus = load_json(args.corpus) if args.corpus else None
        result = summarize_issues(validate_genome(genome, corpus))
        _print(result)
        return 0 if result["valid"] else 1

    if args.command == "audit":
        _print(evidence_audit(load_json(args.genome)))
        return 0

    if args.command == "conform":
        result = evaluate_candidate(load_json(args.genome), load_json(args.candidate), args.identity)
        _print(result.as_dict())
        return 0 if result.classification in {"conforming", "boundary", "insufficient-evidence"} else 2

    if args.command == "holdout":
        _print(deterministic_holdout(load_json(args.corpus), args.fraction))
        return 0

    return 3


if __name__ == "__main__":
    sys.exit(main())
