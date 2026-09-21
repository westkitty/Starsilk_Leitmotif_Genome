# Method

## 1. Research object

The system models **musical heredity** rather than theme quotation.

A recurring melody can be evidence, but the target object is smaller and more portable: interval relationships, rhythmic cells, harmonic behavior, timbral identity, vocal behavior, structural gestures, silence/absence rules and interactions among those carriers.

## 2. Source families before motifs

Every source belongs to a `source_family_id` representing its compositional ancestry.

The family boundary matters because repeated generations of one composition are not independent witnesses. Alternate arrangements can still be analytically valuable — they may reveal which features survive mutation — but they cannot inflate independent recurrence counts.

The first corpus task is therefore lineage classification, not motif extraction.

## 3. Four evidence channels

Every claim should distinguish:

- **audio** — directly audible in inspected audio
- **structural** — derived from notation, MIDI, transcription, interval/rhythm extraction or equivalent representation
- **documentary** — prompt, lyric directive, arrangement note, metadata or production description
- **canonical** — explicit controlling Starsilk musical canon

These channels answer different questions. Documentary intent is not proof of audible realization.

## 4. Gene anatomy

A gene is an identity-bearing behavior with at least one carrier.

Recommended fields:

```json
{
  "gene_id": "CODEC-I03",
  "identity_id": "CODEC",
  "status": "tentative",
  "carriers": ["interval"],
  "genotype": {"relative_intervals": [0, 3, 2, -1]},
  "invariants": ["example-only"],
  "permitted_mutations": ["transposition"],
  "forbidden_mutations": [],
  "evidence": []
}
```

The example shape above demonstrates the data form only. It is **not** a claim about Codec.

### Genotype

The minimum structural relationship that can survive transposition, orchestration or other phenotype changes.

### Phenotype

A concrete realization: melody, bass skeleton, harmonic upper voice, vocal gesture, silence pattern, orchestration, etc.

### Invariants

Properties that must survive for the gene to remain recognizably itself.

### Mutations

Named transformations. Permitted mutations preserve identity. Forbidden mutations cause drift.

## 5. Promotion gates

### Unknown

The corpus does not establish the claim.

### Tentative

There is evidence, but independent recurrence or realization evidence is not yet strong enough.

### Strongly supported

The repository enforces two minimum conditions:

1. two independent source families
2. at least one audio or structural realization channel

This threshold is intentionally conservative and can be strengthened later.

### Canonical

Requires explicit canonical-channel evidence. Repetition alone does not create canon.

## 6. Blind holdout validation

Do not derive the grammar from the entire corpus and then congratulate it for explaining the same material.

Split independent source families into training and holdout groups. Derive candidate genes from training evidence. Then inspect whether the same relationships recur in the hidden families.

The provided `holdout` command performs a deterministic family-level split so repeated runs use the same partition.

## 7. Negative controls

A feature is not distinctive merely because Starsilk contains it.

The eventual analysis should include plausible non-Starsilk controls and near-misses where possible. Common cinematic gestures, generic genre markers and platform-generation habits should be treated as contamination risks.

## 8. Counterfeit testing

After a registry has evidence-bearing genes, test three deliberately confusing cases plus a genuine descendant:

- genuine descendant: deep grammar preserved, surface changed
- boundary case: partial inheritance
- counterfeit: surface style copied, genome absent
- forbidden drift: deep material present but a protected invariant broken

The conformance engine intentionally ignores `surface_traits` for scoring.

## 9. Absence as a carrier

`absence` is a first-class carrier because missing expected events can themselves encode identity.

The founding hypothesis for the Siege Wall is especially important: the Wall may eventually be represented not by a conventional theme but by systematic deletion of learned expectations — missing resolutions, absent frequency bands, interrupted phrases or withheld responses.

That remains a **hypothesis** until corpus evidence supports it.

## 10. Symbolic interoperability

The registry is intentionally independent of any one notation or MIR package.

Two mature precedents informed that choice:

- music21 exposes interval objects and local corpus/search infrastructure, supporting the use of structural musical representations and project-specific corpora.
- Humdrum explicitly supports motif searches defined through interval, relative-duration, contour and metric patterns, including transformations such as transposition and augmentation.

Useful external references:

- https://music21.org/music21docs/usersGuide/usersGuide_18_intervals.html
- https://music21.org/music21docs/usersGuide/usersGuide_11_corpusSearching.html
- https://www.humdrum.org/Humdrum/FAQ.html
- https://www.humdrum.org/guide/

Future adapters may use MusicXML, MIDI, Humdrum or transcription-derived data without changing the core Starsilk genome format.

## 11. Stop rule

If a proposed rule becomes elegant only by ignoring contradictory source material, reject the rule.

The corpus wins.