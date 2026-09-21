# Operational State
<!-- operational-state:metadata
{
  "schema_version": 1,
  "project_id": "starsilk-leitmotif-genome",
  "project_name": "Starsilk Leitmotif Genome",
  "project_root": "/mnt/data/Starsilk_Leitmotif_Genome",
  "artifact_path": "",
  "state_revision": 4,
  "last_updated": "2026-09-21T21:43:27Z",
  "current_baseline": {
    "identity": "main@ca9f678d117b5d9431a8ba610ee53ca73682b4af",
    "state": "verified",
    "last_verified": "2026-09-21T21:43:27Z"
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
v0.1.0 is published on GitHub at `main@1e50b1723536d026787c1f53cb5776cfad06d59e`. The `Genome validation` workflow completed successfully on that commit. The authoritative Starsilk corpus has not yet been ingested.

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

<!-- operational-state:entry
{
  "id": "VER-004",
  "title": "Remote publication and CI are verified",
  "state": "verified",
  "capability": "The complete v0.1.0 repository is published on main and GitHub Actions validates the pushed tree successfully.",
  "scope": "Repository publication and CI",
  "verification_method": "GitHub commit/tree inspection plus workflow run 35649733013",
  "evidence": "Commit 1e50b1723536d026787c1f53cb5776cfad06d59e exists on main; Genome validation run 35649733013 completed with conclusion success.",
  "artifact_revision": "main@1e50b1723536d026787c1f53cb5776cfad06d59e",
  "last_verified": "2026-09-21T20:13:48Z",
  "dependencies": ["GitHub Actions"],
  "freshness": "current",
  "recheck_trigger": "Any push to main or CI workflow change"
}
-->
### VER-004 — Remote publication and CI are verified
- **State:** `verified`
- **Capability:** The complete v0.1.0 repository is published on `main` and GitHub Actions validates the pushed tree successfully.
- **Verification method:** GitHub commit/tree inspection plus workflow run `35649733013`
- **Evidence:** Commit `1e50b1723536d026787c1f53cb5776cfad06d59e`; workflow conclusion `success`.
- **Recheck trigger:** Any push to `main` or CI workflow change
<!-- /operational-state:entry -->

<!-- operational-state:entry
{
  "id": "VER-005",
  "title": "Evidence Observatory is deployed on GitHub Pages",
  "state": "verified",
  "capability": "The interactive Evidence Observatory is publicly deployed and serves the current genome and corpus JSON alongside clearly separated synthetic proof fixtures.",
  "scope": "GitHub Pages evidence interface",
  "verification_method": "GitHub Pages workflow run 35658508867 attempt 2 plus direct HTTPS checks",
  "evidence": "Pages run 35658508867 completed with conclusion success; HTML, genome JSON, and corpus JSON each returned HTTP 200 from https://westkitty.github.io/Starsilk_Leitmotif_Genome/.",
  "artifact_revision": "main@ca9f678d117b5d9431a8ba610ee53ca73682b4af",
  "last_verified": "2026-09-21T21:43:27Z",
  "dependencies": ["GitHub Pages", "GitHub Actions"],
  "freshness": "current",
  "recheck_trigger": "Any change to site/, data/, tests/fixtures/, Pages settings, or the Pages workflow"
}
-->
### VER-005 — Evidence Observatory is deployed on GitHub Pages
- **State:** `verified`
- **Capability:** The interactive Evidence Observatory is publicly deployed and serves the current genome and corpus JSON alongside clearly separated synthetic proof fixtures.
- **Verification method:** Pages workflow run `35658508867` attempt 2 plus direct HTTPS checks
- **Evidence:** HTML, genome JSON, and corpus JSON each returned HTTP `200` from `https://westkitty.github.io/Starsilk_Leitmotif_Genome/`.
- **Recheck trigger:** Any change to `site/`, `data/`, `tests/fixtures/`, Pages settings, or the Pages workflow
<!-- /operational-state:entry -->

## 6. Known Not Working
None established.

## 7. Implemented but Unverified
None currently.

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
| VER-004 | Remote publication + CI | verified | GitHub commit + workflow run | remote inspection | Any push/CI change |\n| VER-005 | Evidence Observatory on Pages | verified | Pages run 35658508867 + HTTP 200 checks | deployed-site inspection | Site/data/Pages change |

## 12. Current Change Scope and Impact Radius
v0.1 initialization, evidence interface, and GitHub Pages publication are complete. The next bounded work is authoritative corpus ingestion; no musical gene promotion is permitted before source-family and evidence classification.

## 13. Compact Revision Log
- Revision 1 — Bootstrapped greenfield operational state before implementation.
- Revision 2 — Implemented and locally verified the v0.1 engine; 10/10 tests pass. GitHub CI remains implemented-unverified until remote execution.
- Revision 3 — Verified remote publication at `1e50b172...` and successful GitHub Actions run `35649733013`; CI is promoted to verified.\n- Revision 4 — Added the interactive Evidence Observatory at `ca9f678d...`, enabled GitHub Pages with workflow publishing, and verified Pages run `35658508867` plus HTTP 200 responses for the HTML, genome JSON, and corpus JSON.
