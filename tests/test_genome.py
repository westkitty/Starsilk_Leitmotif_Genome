from __future__ import annotations

import copy
import json
import unittest
from pathlib import Path

from leitmotif_genome.conformance import evaluate_candidate
from leitmotif_genome.holdout import deterministic_holdout
from leitmotif_genome.validate import validate_genome

ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / "tests" / "fixtures"


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


class GenomeValidationTests(unittest.TestCase):
    def setUp(self):
        self.demo_genome = load(FIXTURES / "demo_genome.json")
        self.demo_corpus = load(FIXTURES / "demo_corpus.json")

    def test_seed_registry_asserts_no_unearned_genes(self):
        seed = load(ROOT / "data" / "genome" / "starsilk_genome.json")
        corpus = load(ROOT / "data" / "corpus" / "corpus_manifest.json")
        issues = validate_genome(seed, corpus)
        self.assertFalse([issue for issue in issues if issue.level == "error"])
        self.assertEqual(seed["genes"], [])

    def test_demo_genome_is_valid(self):
        issues = validate_genome(self.demo_genome, self.demo_corpus)
        self.assertFalse([issue.as_dict() for issue in issues if issue.level == "error"])

    def test_strong_support_requires_independent_families(self):
        genome = copy.deepcopy(self.demo_genome)
        gene = genome["genes"][0]
        gene["evidence"][1]["source_family_id"] = "DEMO-FAMILY-A"
        issues = validate_genome(genome, self.demo_corpus)
        self.assertIn("genome.pseudoreplication", {issue.code for issue in issues})

    def test_canonical_gene_requires_canonical_evidence(self):
        genome = copy.deepcopy(self.demo_genome)
        genome["genes"][0]["status"] = "canonical"
        issues = validate_genome(genome, self.demo_corpus)
        self.assertIn("genome.canonical_without_authority", {issue.code for issue in issues})

    def test_production_alone_cannot_define_identity(self):
        genome = copy.deepcopy(self.demo_genome)
        gene = genome["genes"][0]
        gene["carriers"] = ["production"]
        issues = validate_genome(genome, self.demo_corpus)
        self.assertIn("genome.production_only_identity", {issue.code for issue in issues})


class ConformanceTests(unittest.TestCase):
    def setUp(self):
        self.genome = load(FIXTURES / "demo_genome.json")

    def test_genuine_descendant_conforms_without_literal_repetition(self):
        candidate = load(FIXTURES / "demo_candidate_descendant.json")
        result = evaluate_candidate(self.genome, candidate, "DEMO")
        self.assertEqual(result.classification, "conforming")
        self.assertEqual(result.score, 1.0)

    def test_surface_counterfeit_scores_zero(self):
        candidate = load(FIXTURES / "demo_candidate_counterfeit.json")
        result = evaluate_candidate(self.genome, candidate, "DEMO")
        self.assertEqual(result.classification, "counterfeit")
        self.assertEqual(result.score, 0.0)
        self.assertTrue(any("Surface/production resemblance" in note for note in result.notes))

    def test_forbidden_mutation_fails_even_when_gene_is_recognizable(self):
        candidate = load(FIXTURES / "demo_candidate_drift.json")
        result = evaluate_candidate(self.genome, candidate, "DEMO")
        self.assertEqual(result.classification, "nonconforming")
        self.assertTrue(result.forbidden_drift)

    def test_empty_starsilk_registry_refuses_fake_classification(self):
        seed = load(ROOT / "data" / "genome" / "starsilk_genome.json")
        result = evaluate_candidate(seed, {"candidate_id": "X", "surface_traits": ["ominous"]}, "TIGER")
        self.assertEqual(result.classification, "insufficient-evidence")


class HoldoutTests(unittest.TestCase):
    def test_holdout_is_deterministic_and_family_level(self):
        corpus = load(FIXTURES / "demo_corpus.json")
        first = deterministic_holdout(corpus, 0.34)
        second = deterministic_holdout(corpus, 0.34)
        self.assertEqual(first, second)
        self.assertTrue(first["training_family_ids"])
        self.assertTrue(first["holdout_family_ids"])
        self.assertFalse(set(first["training_family_ids"]) & set(first["holdout_family_ids"]))


if __name__ == "__main__":
    unittest.main()
