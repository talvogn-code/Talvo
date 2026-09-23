# TalVo

Plateforme guinéenne de recrutement : sourcing, présélection et évaluation des talents.

> Trouver les bons talents. Trouver les bonnes opportunités.

TalVo ne se limite pas à publier des offres. Une entreprise décrit son besoin, TalVo analyse les
profils disponibles, classe les candidats selon leurs compétences et expériences, organise si
nécessaire des tests en ligne, puis présente au recruteur une sélection de profils pertinents.

**Objectif V1 (janvier 2027)** — une version réellement utilisable par 5 à 10 entreprises pilotes
à Conakry, démontrant la valeur du tri automatique des CV et des tests en ligne.

## Ce projet est conduit par les specs

Aucune ligne de code applicatif n'est écrite avant qu'une spécification approuvée ne la décrive.
La méthode est dans **[`CONTRIBUTING.md`](CONTRIBUTING.md)**.

```
Exigence (EXI-xxx) → Spec (SPEC-0xx) → Critère (CA-x) → Test → Code
     registre           specs/          dans la spec    suite    PR
```

| Point d'entrée | Contenu |
|---|---|
| [`specs/`](specs/) | Les spécifications et leur index |
| [`docs/10-registre-exigences.md`](docs/10-registre-exigences.md) | 90 exigences identifiées, dont 72 en P0 |
| [`docs/09-jalons.md`](docs/09-jalons.md) | Huit jalons et leurs critères de sortie |
| [`docs/adr/`](docs/adr/) | Neuf décisions techniques, toutes encore à trancher |
| [`CONTRIBUTING.md`](CONTRIBUTING.md) | Comment une spec naît, est revue et implémentée |
| [`CLAUDE.md`](CLAUDE.md) | Règles invariantes du domaine et conventions |

## Analyses de cadrage

| Document | Contenu |
|---|---|
| [`docs/00-cadrage-mvp.md`](docs/00-cadrage-mvp.md) | Cahier des charges fonctionnel — source de vérité produit |
| [`docs/01-modele-donnees.md`](docs/01-modele-donnees.md) | Modèle de données V1 |
| [`docs/02-moteur-matching.md`](docs/02-moteur-matching.md) | Spécification du moteur de classement |
| [`docs/03-decisions-techniques.md`](docs/03-decisions-techniques.md) | Options d'architecture — arbitrage suspendu |
| [`docs/04-ia-traitement-documentaire.md`](docs/04-ia-traitement-documentaire.md) | Chaîne de lecture des CV et architecture d'échelle |
| [`docs/05-strategie-modeles-ia.md`](docs/05-strategie-modeles-ia.md) | Choix de modèles, coûts, garde-fous anti-hallucination |
| [`docs/06-analyse-zety.md`](docs/06-analyse-zety.md) | Analyse d'un produit de référence |
| [`docs/07-angles-morts.md`](docs/07-angles-morts.md) | Sujets absents du cahier des charges, par criticité |
| [`docs/08-note-operations.md`](docs/08-note-operations.md) | Note non technique : besoins, coûts, risques |
| [`docs/presentation/architecture.html`](docs/presentation/architecture.html) | Carte technique de bout en bout |
| [`docs/presentation/pipeline.html`](docs/presentation/pipeline.html) | Pipeline de livraison |

## Contrôle de cohérence

```bash
python3 scripts/check_specs.py          # vérifie exigences, specs et décisions
python3 scripts/check_specs.py --index  # régénère specs/README.md
```

Ce contrôle tourne en intégration continue. Il vérifie notamment qu'aucune exigence n'est
orpheline et qu'aucune spec approuvée ne conserve une question ouverte bloquante.

## État

Phase **M0 — cadrage et décisions**. Aucun code applicatif.

Les quatre décisions qui conditionnent la suite — découpage applicatif, identifiant de compte,
chaîne de lecture des CV, modèles ouverts ou fermés — dépendent des mesures à faire sur un corpus
de CV réels. **C'est le chemin critique de la phase.**
