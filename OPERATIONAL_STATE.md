# Operational State
<!-- operational-state:metadata
{
  "schema_version": 1,
  "project_id": "starsilk-leitmotif-genome",
  "project_name": "Starsilk Leitmotif Genome",
  "project_root": "/mnt/data/Starsilk_Leitmotif_Genome",
  "artifact_path": "",
  "state_revision": 2,
  "last_updated": "2026-09-21T20:12:00Z",
  "current_baseline": {
    "identity": "v0.1.0 initialization candidate",
    "state": "partially-verified",
    "last_verified": "2026-09-21T20:12:00Z"
  },
  "scope_boundaries": [
    "Starsilk musical-analysis toolkit and its documentation only",
    "Do not invent musical canon; source evidence must precede gene assertions"
  ],
  "linked_parent_state": null
}
-->

## 1. Project Identity and Scope
Starsilk Leitmotif Genome is a source-grounded musical-heredity toolkit for extracting, representing, testing and reusing leitmotif DNA without reducing identities to quoted melodies.

## 2. Current Baseline
The v0.1.0 initialization candidate is locally implemented and passes its standard-library test suite. The authoritative Starsilk corpus has not yet been ingested.

## 3. Artifact Contract
Deliver a usable repository containing a machine-readable genome model, source-family lineage model, evidence discipline, holdout/negative-control testing, conformance engine, validator, documentation and automated tests.

## 4. Active Invariants
<!-- operational-state:entry
{
  "id": "INV-001",
  "title": "No invented musical canon",
  "state": "requested",
  "rule": "No gene, allele, motif behavior or confidence claim may be promoted into the canonical registry without source evidence.",
  "scope": "Genome registry and analysis outputs",
  "authority": "Explicit user project direction plus founding specification",
  "evidence": "Founding specification requires unknowns to remain unknown and the corpus to win over elegant theory.",
  "validation_method": "Semantic validation rejects unsupported promoted statuses; seed registry contains no asserted genes.",
  "last_checked": "revision 1",
  "status": "active",
  "recheck_trigger": "Any corpus ingestion, gene promotion or canon export"
}
-->
### INV-001 — No invented musical canon
- **State:** `requested`
- **Rule:** No gene, allele, motif behavior or confidence claim may be promoted into the canonical registry without source evidence.
- **Scope:** Genome registry and analysis outputs
- **Authority:** Explicit user project direction plus founding specification
- **Evidence:** Founding specification requires unknowns to remain unknown and the corpus to win over elegant theory.
- **Validation method:** Semantic validation rejects unsupported promoted statuses; seed registry contains no asserted genes.
- **Last checked:** revision 1
- **Status:** active
- **Recheck trigger:** Any corpus ingestion, gene promotion or canon export
<!-- /operational-state:entry -->

<!-- operational-state:entry
{
  "id": "INV-002",
  "title": "Independent source families count as witnesses",
  "state": "requested",
  "rule": "Alternate generations, remixes and revisions from one ancestral composition family do not count as multiple independent witnesses.",
  "scope": "Evidence aggregation and confidence promotion",
  "authority": "Founding methodology",
  "evidence": "The founding specification explicitly warns against duplicate generations and alternate arrangements being counted as independent examples.",
  "validation_method": "Evidence audit counts unique source_family_id values rather than raw source records.",
  "last_checked": "revision 1",
  "status": "active",
  "recheck_trigger": "Any evidence or confidence algorithm change"
}
-->
### INV-002 — Independent source families count as witnesses
- **State:** `requested`
- **Rule:** Alternate generations, remixes and revisions from one ancestral composition family do not count as multiple independent witnesses.
- **Scope:** Evidence aggregation and confidence promotion
- **Authority:** Founding methodology
- **Evidence:** The founding specification explicitly warns against duplicate generations and alternate arrangements being counted as independent examples.
- **Validation method:** Evidence audit counts unique `source_family_id` values rather than raw source records.
- **Last checked:** revision 1
- **Status:** active
- **Recheck trigger:** Any evidence or confidence algorithm change
<!-- /operational-state:entry -->

## 5. Verified Working Behavior
<!-- operational-state:entry
{
  "id": "VER-001",
  "title": "Evidence promotion gates reject unsupported confidence",
  "state": "verified",
  "capability": "Validator rejects pseudoreplicated strongly-supported genes, canonical genes without canonical evidence, and production-only required identity genes.",
  "scope": "Semantic genome validation",
  "verification_method": "Python unittest suite",
  "evidence": "10/10 local tests passed on 2026-09-21.",
  "artifact_revision": "v0.1.0 initialization candidate",
  "last_verified": "2026-09-21T20:12:00Z",
  "dependencies": ["Python 3.11+ standard library"],
  "freshness": "current",
  "recheck_trigger": "Validator or genome schema changes"
}
-->
### VER-001 — Evidence promotion gates reject unsupported confidence
- **State:** `verified`
- **Capability:** Validator rejects pseudoreplicated strongly-supported genes, canonical genes without canonical evidence, and production-only required identity genes.
- **Verification method:** Python unittest suite
- **Evidence:** 10/10 local tests passed on 2026-09-21.
- **Recheck trigger:** Validator or genome schema changes
<!-- /operational-state:entry -->

<!-- operational-state:entry
{
  "id": "VER-002",
  "title": "Conformance distinguishes descendant, counterfeit and forbidden drift",
  "state": "verified",
  "capability": "Synthetic descendant conforms, pure surface counterfeit scores zero, forbidden mutation is nonconforming, and empty Starsilk registry returns insufficient-evidence.",
  "scope": "Conformance classifier",
  "verification_method": "Python unittest suite plus CLI spot checks",
  "evidence": "10/10 local tests passed; counterfeit CLI returned classification counterfeit with score 0.0.",
  "artifact_revision": "v0.1.0 initialization candidate",
  "last_verified": "2026-09-21T20:12:00Z",
  "dependencies": ["Python 3.11+ standard library"],
  "freshness": "current",
  "recheck_trigger": "Conformance thresholds, weights or mutation semantics change"
}
-->
### VER-002 — Conformance distinguishes descendant, counterfeit and forbidden drift
- **State:** `verified`
- **Capability:** Synthetic descendant conforms, pure surface counterfeit scores zero, forbidden mutation is nonconforming, and empty Starsilk registry returns insufficient-evidence.
- **Verification method:** Python unittest suite plus CLI spot checks
- **Evidence:** 10/10 local tests passed; counterfeit CLI returned classification `counterfeit` with score `0.0`.
- **Recheck trigger:** Conformance thresholds, weights or mutation semantics change
<!-- /operational-state:entry -->

<!-- operational-state:entry
{
  "id": "VER-003",
  "title": "Holdout split operates on source families",
  "state": "verified",
  "capability": "Deterministic holdout produces disjoint training and holdout family sets rather than splitting individual versions.",
  "scope": "Blind-validation preparation",
  "verification_method": "Python unittest suite and CLI spot check",
  "evidence": "Demo corpus split placed DEMO-FAMILY-C in holdout and A/B in training with no overlap.",
  "artifact_revision": "v0.1.0 initialization candidate",
  "last_verified": "2026-09-21T20:12:00Z",
  "dependencies": ["Python 3.11+ standard library"],
  "freshness": "current",
  "recheck_trigger": "Holdout algorithm or family model changes"
}
-->
### VER-003 — Holdout split operates on source families
- **State:** `verified`
- **Capability:** Deterministic holdout produces disjoint training and holdout family sets rather than splitting individual versions.
- **Verification method:** Python unittest suite and CLI spot check
- **Evidence:** Demo corpus split placed `DEMO-FAMILY-C` in holdout and A/B in training with no overlap.
- **Recheck trigger:** Holdout algorithm or family model changes
<!-- /operational-state:entry -->

## 6. Known Not Working
None established.

## 7. Implemented but Unverified
- GitHub Actions workflow is implemented but cannot be called verified until the pushed workflow runs successfully on GitHub.

## 8. Unknown or Evidence-Stale State
- Direct-audio corpus analysis remains unavailable until source material is ingested.
- No Starsilk gene claims are established by this repository initialization alone.

## 9. Pending Work
- Ingest authoritative corpus metadata and source families.
- Run blind holdout and negative-control analysis before canon promotion.

## 10. Active Decisions, Defaults, and Prohibitions
- Python standard library only for the initial engine.
- No external runtime dependency is required for validation or conformance testing.
- Production style alone must never count as leitmotif identity.
- Prompt intent and audible realization remain distinct evidence channels.

## 11. Validation and Evidence Matrix
| ID | Claim | State | Evidence | Validation | Recheck trigger |
|---|---|---|---|---|---|
| INV-001 | No invented musical canon | requested | Founding spec | Semantic validator + registry review | Gene promotion |
| INV-002 | Count source families, not versions | requested | Founding spec | Evidence audit | Evidence algorithm change |
| VER-001 | Evidence promotion gates | verified | 10/10 local tests | unittest | Validator/schema change |
| VER-002 | Conformance distinctions | verified | tests + CLI | unittest/CLI | Conformance change |
| VER-003 | Family-level holdout | verified | tests + CLI | unittest/CLI | Holdout/family change |

## 12. Current Change Scope and Impact Radius
Complete v0.1 initialization, stage and commit locally, then publish to the empty GitHub repository. No pre-existing target-repository files require preservation.

## 13. Compact Revision Log
- Revision 1 — Bootstrapped greenfield operational state before implementation.
- Revision 2 — Implemented and locally verified the v0.1 engine; 10/10 tests pass. GitHub CI remains implemented-unverified until remote execution.