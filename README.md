# Starsilk Leitmotif Genome

**A compositional grammar for musical identity, transformation and historical recurrence.**

This repository is the working implementation of the Starsilk musical-heredity project. Its job is not to collect theme quotations. Its job is to discover and encode the reusable relationships that let entirely new music remain recognizably descended from Starsilk.

> relationships over notes  
> behavior over melodies  
> inheritance over repetition  
> transformation over quotation

## What v0.1 actually does

The initial engine provides:

- a machine-readable leitmotif genome registry
- a source-family model that prevents alternate generations from masquerading as independent evidence
- four distinct evidence channels: audio, structural, documentary and canonical
- promotion gates for `canonical`, `strongly-supported`, `tentative` and `unknown` claims
- a rule that production style alone cannot define identity
- deterministic family-level holdout splitting for blind validation
- a conformance engine that distinguishes descendants, boundary cases, counterfeits and forbidden drift
- JSON Schemas for corpus and genome records
- synthetic non-canon regression fixtures
- automated tests and GitHub Actions CI
- the complete founding specification preserved in `docs/FOUNDING_SPEC.md`

## What v0.1 deliberately does **not** claim

The real Starsilk corpus has not yet been ingested into this repository. The initial registry names the identities the founding specification requires us to investigate, but it asserts **zero musical genes**.

That is deliberate.

Tiger, Codec, Drakken, Starsilk, the Siege Wall, Blood Eclipse War recurrence and Mother are registered as research targets. Their interval cells, rhythmic behaviors, harmonic rules, timbres, vocal strategies, absence behaviors and transformation grammar remain evidence-pending.

A validator that invents the answer before looking at the corpus would be a very sophisticated horoscope.

## Core model

A `gene` is an identity-bearing musical behavior that can survive transformation.

A gene may be carried by one or more channels:

- interval
- rhythm
- harmony
- melody
- timbre
- vocal behavior
- structural behavior
- absence
- production

Each gene can define:

- a genotype: relative structural representation
- invariants: what must survive for recognition
- permitted mutations
- forbidden mutations
- phenotypic expressions
- evidence records
- confidence / canon status
- conformance weight

Production is allowed as a carrier, but a production-only gene cannot be required for identity recognition.

## Evidence discipline

Raw file count is not independent evidence.

If one composition has twenty Suno generations, three remasters and two instrumental renders, that may still represent **one source family**. Confidence promotion is based on independent `source_family_id` witnesses, not generation count.

A `strongly-supported` gene requires:

1. at least two independent source families, and
2. at least one realized `audio` or `structural` evidence channel.

A `canonical` gene requires explicit `canonical` evidence.

Prompt intent does not prove audible realization. Documentary evidence and realized evidence remain separate.

## Quick start

No runtime dependency is required beyond Python 3.11+.

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

Validate the current Starsilk registry:

```bash
PYTHONPATH=src python -m leitmotif_genome validate \
  --genome data/genome/starsilk_genome.json \
  --corpus data/corpus/corpus_manifest.json
```

Inspect evidence independence:

```bash
PYTHONPATH=src python -m leitmotif_genome audit \
  --genome data/genome/starsilk_genome.json
```

Create a deterministic family-level holdout:

```bash
PYTHONPATH=src python -m leitmotif_genome holdout \
  --corpus tests/fixtures/demo_corpus.json \
  --fraction 0.25
```

Test a candidate against an identity:

```bash
PYTHONPATH=src python -m leitmotif_genome conform \
  --genome tests/fixtures/demo_genome.json \
  --candidate tests/fixtures/demo_candidate_descendant.json \
  --identity DEMO
```

The demo files are synthetic regression fixtures. They are **not Starsilk canon**.

## The counterfeit test

The project is designed around a harder question than “does this sound similar?”

After real genes are extracted, new musical specifications should be tested in at least four classes:

1. genuine descendant — obeys the grammar without quoting old melodies
2. boundary case — preserves only part of the registered identity
3. counterfeit — imitates genre, mix or instrumentation without the deeper gene structure
4. forbidden drift — remains recognizable but breaks an identity-critical invariant

A useful genome must recognize its descendants and reject convincing fakes.

## Repository map

```text
.
├── data/
│   ├── corpus/       # source families and evidence inventory
│   ├── genome/       # canonical machine-readable registry
│   └── tests/        # real future conformance/holdout results
├── docs/
│   ├── FOUNDING_SPEC.md
│   ├── METHOD.md
│   ├── CORPUS_INGESTION.md
│   └── QUICK_REFERENCE.md
├── schemas/          # JSON contracts
├── src/leitmotif_genome/
│   ├── validate.py   # evidence and semantic gates
│   ├── conformance.py
│   ├── holdout.py
│   └── audit.py
├── tests/            # synthetic non-canon regression suite
└── OPERATIONAL_STATE.md
```

## Next substantive phase

Ingest the authoritative Starsilk musical source families, preserving ancestry and evidence channels. Only then begin gene extraction.

The corpus wins over the theory.
