# TalVo

Plateforme guinéenne de recrutement : sourcing, présélection et évaluation des talents.

> Trouver les bons talents. Trouver les bonnes opportunités.

TalVo ne se limite pas à publier des offres. Une entreprise décrit son besoin, TalVo analyse les
profils disponibles, classe les candidats selon leurs compétences et expériences, organise si
nécessaire des tests en ligne, puis présente au recruteur une sélection de profils pertinents.

**Objectif V1 (janvier 2027)** : une version réellement utilisable par 5 à 10 entreprises pilotes,
démontrant la valeur du tri automatique des CV et des tests en ligne.

## Documentation

| Document | Contenu |
|---|---|
| [`docs/00-cadrage-mvp.md`](docs/00-cadrage-mvp.md) | Cahier des charges fonctionnel — **source de vérité** |
| [`docs/01-modele-donnees.md`](docs/01-modele-donnees.md) | Modèle de données V1 |
| [`docs/02-moteur-matching.md`](docs/02-moteur-matching.md) | Spécification du moteur de matching |
| [`docs/03-decisions-techniques.md`](docs/03-decisions-techniques.md) | Architecture — **arbitrage suspendu** |
| [`docs/04-ia-traitement-documentaire.md`](docs/04-ia-traitement-documentaire.md) | IA, chaîne IDP et architecture pour l'échelle |

## État

Phase **Cadrage** (septembre 2026). Aucun code applicatif à ce stade.

L'arbitrage technique est **volontairement suspendu** : la chaîne de traitement documentaire
(lecture et compréhension des CV déposés en PDF/Word) est la contrainte dimensionnante du
produit, et elle doit être mesurée sur des CV réels avant tout choix d'infrastructure.
Voir `docs/04-ia-traitement-documentaire.md`.
