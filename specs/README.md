# Spécifications

Index généré par `python3 scripts/check_specs.py --index`. Ne pas modifier à la main.

La méthode est décrite dans [`CONTRIBUTING.md`](../CONTRIBUTING.md), les exigences dans
[`docs/10-registre-exigences.md`](../docs/10-registre-exigences.md), les jalons dans
[`docs/09-jalons.md`](../docs/09-jalons.md) et les décisions dans [`docs/adr/`](../docs/adr/).

| Spec | Titre | Statut | Jalon | Prio | Exigences | Dépend de |
|---|---|---|---|---|---|---|
| [`SPEC-001`](SPEC-001-comptes-et-identite.md) | Comptes et identité | `brouillon` | `M1` | P0 | `EXI-CPT-01`, `EXI-CPT-02`, `EXI-CPT-07`, `NFR-01`, `NFR-02`, `NFR-05` | — |
| [`SPEC-002`](SPEC-002-profil-candidat.md) | Profil candidat | `brouillon` | `M2` | P0 | `EXI-PRF-01`, `EXI-PRF-02`, `EXI-PRF-03` | `SPEC-001`, `SPEC-003` |
| [`SPEC-003`](SPEC-003-cv-import-et-lecture.md) | Import et lecture des CV | `en revue` | `M2` | P0 | `EXI-CV-01`, `EXI-CV-02`, `EXI-CV-03`, `EXI-CV-04`, `EXI-CV-05`, `EXI-CV-06`, `NFR-03`, `NFR-04`, `NFR-07`, `NFR-15` | `SPEC-001`, `SPEC-013` |
| [`SPEC-004`](SPEC-004-createur-et-export-de-cv.md) | Créateur et export de CV | `brouillon` | `M2` | P0 | `EXI-CV-07`, `EXI-CV-08` | `SPEC-002` |
| [`SPEC-005`](SPEC-005-entreprises-et-validation.md) | Entreprises et validation | `brouillon` | `M3` | P0 | `EXI-CPT-03`, `EXI-CPT-04`, `EXI-PRF-04`, `EXI-ADM-01` | `SPEC-001` |
| [`SPEC-006`](SPEC-006-offres-d-emploi.md) | Offres d'emploi | `brouillon` | `M3` | P0 | `EXI-OFF-01`, `EXI-OFF-02`, `EXI-OFF-03`, `EXI-OFF-04`, `EXI-OFF-05`, `EXI-OFF-07`, `NFR-06` | `SPEC-005`, `SPEC-013` |
| [`SPEC-007`](SPEC-007-candidatures.md) | Candidatures | `brouillon` | `M3` | P0 | `EXI-CND-01`, `EXI-CND-02`, `EXI-CND-03`, `EXI-CND-04`, `EXI-CND-05` | `SPEC-002`, `SPEC-006` |
| [`SPEC-008`](SPEC-008-matching-et-scoring.md) | Matching et scoring | `en revue` | `M4` | P0 | `EXI-MCH-01`, `EXI-MCH-02`, `EXI-MCH-03`, `EXI-MCH-04`, `EXI-MCH-05`, `EXI-MCH-06`, `EXI-MCH-07`, `NFR-16` | `SPEC-003`, `SPEC-006`, `SPEC-013` |
| [`SPEC-009`](SPEC-009-sourcing-de-talents.md) | Sourcing de talents | `brouillon` | `M4` | P1 | `EXI-MCH-08`, `EXI-MCH-09` | `SPEC-008`, `SPEC-002` |
| [`SPEC-010`](SPEC-010-tests-en-ligne.md) | Tests en ligne | `en revue` | `M4` | P0 | `EXI-OFF-08`, `EXI-TST-01`, `EXI-TST-02`, `EXI-TST-03`, `EXI-TST-04`, `EXI-TST-05`, `EXI-TST-06`, `EXI-TST-07`, `EXI-TST-09`, `EXI-TST-10`, `EXI-TST-11`, `EXI-TST-12` | `SPEC-001`, `SPEC-006`, `SPEC-014` |
| [`SPEC-011`](SPEC-011-shortlist-et-fiche-candidat.md) | Shortlist et fiche candidat | `brouillon` | `M4` | P0 | `EXI-PRS-01`, `EXI-PRS-02`, `EXI-PRS-03`, `EXI-CND-06`, `EXI-TST-08` | `SPEC-008`, `SPEC-010` |
| [`SPEC-012`](SPEC-012-tableaux-de-bord.md) | Tableaux de bord | `brouillon` | `M4` | P0 | `EXI-DSH-01`, `EXI-DSH-02`, `NFR-13`, `NFR-14` | `SPEC-007`, `SPEC-011` |
| [`SPEC-013`](SPEC-013-referentiels-metier.md) | Référentiels métier | `en revue` | `M1` | P0 | `EXI-MCH-10`, `EXI-ADM-03`, `NFR-11` | — |
| [`SPEC-014`](SPEC-014-notifications.md) | Notifications | `brouillon` | `M1` | P0 | `EXI-TST-01` | `SPEC-001` |
| [`SPEC-015`](SPEC-015-administration-et-moderation.md) | Administration et modération | `brouillon` | `M5` | P0 | `EXI-CPT-05`, `EXI-ADM-02`, `EXI-ADM-04`, `EXI-ADM-05`, `NFR-18` | `SPEC-005` |
| [`SPEC-016`](SPEC-016-observabilite-et-indicateurs.md) | Observabilité et indicateurs | `en revue` | `M1` | P0 | `NFR-08`, `NFR-09`, `NFR-10`, `NFR-12`, `NFR-17` | — |
| [`SPEC-017`](SPEC-017-premium-et-visibilite.md) | Premium et visibilité | `brouillon` | `M7` | P1 | `EXI-CPT-06`, `EXI-CV-09`, `EXI-CV-10`, `EXI-CV-11`, `EXI-OFF-06`, `EXI-MON-01`, `EXI-MON-03` | `SPEC-004`, `SPEC-008` |
| [`SPEC-018`](SPEC-018-messagerie.md) | Messagerie | `brouillon` | `M7` | P1 | `EXI-MON-02`, `EXI-MON-04` | `SPEC-007`, `SPEC-017` |

## Statuts

| Statut | Signification |
|---|---|
| `brouillon` | En cours d'écriture, incomplète |
| `en revue` | Complète, soumise en pull request |
| `approuvée` | **L'implémentation peut commencer** |
| `implémentée` | Le code la satisfait, tous les critères passent |
| `obsolète` | Remplacée ou abandonnée |

Une spec ne passe pas en `approuvée` s'il lui reste une question ouverte bloquante ;
le contrôle ci-dessus le vérifie.
