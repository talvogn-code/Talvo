# Décisions techniques

Une décision par fichier. Une décision porte un **statut** et un **jalon avant lequel elle doit
être tranchée**. Un jalon ne se ferme pas avec une décision de son périmètre encore `proposée`.

| Statut | Signification |
|---|---|
| `proposée` | Options posées, décision non prise |
| `acceptée` | Tranchée — elle engage le code |
| `remplacée` | Une décision ultérieure l'annule ; conservée pour l'historique |

| ADR | Titre | Statut | À trancher avant |
|---|---|---|---|
| [`ADR-001`](ADR-001-decoupage-de-l-application.md) | Découpage de l'application | `proposée` | `M0` |
| [`ADR-002`](ADR-002-hebergement-et-execution-des-traitements-longs.md) | Hébergement et exécution des traitements longs | `proposée` | `M1` |
| [`ADR-003`](ADR-003-identifiant-principal-d-un-compte.md) | Identifiant principal d'un compte | `proposée` | `M0` |
| [`ADR-004`](ADR-004-chaine-de-lecture-des-cv.md) | Chaîne de lecture des CV | `proposée` | `M0` |
| [`ADR-005`](ADR-005-modeles-a-poids-ouverts-ou-interfaces-fermees.md) | Modèles à poids ouverts ou interfaces fermées | `proposée` | `M0` |
| [`ADR-006`](ADR-006-localisation-et-conservation-des-donnees.md) | Localisation et conservation des données | `proposée` | `M1` |
| [`ADR-007`](ADR-007-canal-des-notifications-critiques.md) | Canal des notifications critiques | `proposée` | `M4` |
| [`ADR-008`](ADR-008-source-de-verite-du-profil-le-profil-ou-le-cv.md) | Source de vérité du profil : le profil ou le CV | `proposée` | `M2` |
| [`ADR-009`](ADR-009-encaissement-et-moyens-de-paiement.md) | Encaissement et moyens de paiement | `proposée` | `M7` |

Quatre décisions doivent tomber avant la fin de **M0** — `ADR-001`, `ADR-003`, `ADR-004` et
`ADR-005`. Trois d'entre elles dépendent des mesures faites sur le corpus de CV : c'est ce qui
fait du corpus le chemin critique de la phase de cadrage.

## Écrire une nouvelle décision

Copier `TEMPLATE.md`, numéroter à la suite, ouvrir une pull request. Une décision se discute
comme une spec : elle est revue, puis fusionnée avec son statut à jour.
