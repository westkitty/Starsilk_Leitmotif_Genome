# Corpus Ingestion

## Purpose

Create a defensible inventory before extracting musical genes.

## Step 1 — Identify compositional ancestry

Group revisions, alternate Suno generations, remasters, instrumentals and reprises by actual ancestry rather than filename similarity.

A source family should answer:

> How many genuinely independent compositional decisions are represented here?

If ten outputs descend from one prompt/song skeleton, they normally remain one family even when their arrangements differ substantially.

## Step 2 — Create source records

Recommended fields:

- `source_id`
- `source_family_id`
- title
- version
- associated identity / event
- narrative context
- sanitized source location
- authority state
- whether audio was inspected
- lyric availability
- production-note availability
- symbolic material availability
- optional content hash

Do not commit credentials, expiring private download URLs or secrets.

## Step 3 — Record transformations within families

Useful relationship labels include:

- production-variation
- deliberate-thematic-transformation
- historical-development
- perspective-shift
- corruption
- memory
- reprise
- generation-variance

These labels explain why variants differ without making them independent witnesses.

## Step 4 — Preserve source authority

Use the founding evidence states:

- canonical
- strongly-supported
- tentative
- unknown

A filename such as `FINAL_CANON_REAL.mp3` is not authority evidence. Charming attempt, file system.

## Step 5 — Separate intent from realization

If a prompt says “descending tritone” but the audio does not clearly realize it:

- the prompt can support `documentary` evidence
- it cannot by itself support `audio` evidence

If a transcription or MIDI establishes the interval, add `structural` evidence.

## Step 6 — Hash where practical

A content hash can identify exact duplicates, but identical bytes are not the only duplication problem. Two different generated files can still descend from one source family.

Hashing supports identity. Human/analytical lineage classification establishes ancestry.

## Step 7 — Run validation before extraction

```bash
PYTHONPATH=src python -m leitmotif_genome validate \
  --genome data/genome/starsilk_genome.json \
  --corpus data/corpus/corpus_manifest.json
```

Warnings about family membership drift should be resolved before confidence calculations.

## Step 8 — Freeze a holdout

Once enough independent families exist:

```bash
PYTHONPATH=src python -m leitmotif_genome holdout \
  --corpus data/corpus/corpus_manifest.json \
  --fraction 0.25
```

Do not inspect the holdout for rule discovery. Use it to test whether rules discovered elsewhere survive contact with unseen material.