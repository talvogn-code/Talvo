---
id: SPEC-009
titre: Sourcing de talents
statut: brouillon
version: 0.1
jalon: M4
priorite: P1
exigences: [EXI-MCH-08, EXI-MCH-09]
depend_de: [SPEC-008, SPEC-002]
auteur: ""
derniere_maj: 2026-09-23
---

# SPEC-009 — Sourcing de talents

> **Brouillon.** Les règles et critères ci-dessous sont des amorces issues du cahier des charges
> et de l'analyse. Ils doivent être complétés et revus avant approbation.

## 1. Objectif

Proposer au recruteur des profils pertinents qui n'ont pas postulé, sans trahir le consentement des candidats.

## 2. Hors périmètre

Calcul du score (`SPEC-008`) · prise de contact (`SPEC-018`).

## 3. Règles métier pressenties

- **RG-1** — Seuls les profils ayant consenti au sourcing et validés par leur candidat entrent dans la population examinée.
- **RG-2** — Les profils sourcés sont présentés dans un espace **distinct** des candidatures, sans confusion possible.
- **RG-3** — Un seuil de score et un nombre maximal de profils bornent la proposition.
- **RG-4** — Le candidat est informé qu'il a été proposé à une entreprise, et peut s'y opposer pour l'avenir.

## 4. Critères d'acceptation amorcés

- **CA-1** — Étant donné un candidat sans consentement, quand le sourcing s'exécute, alors il n'apparaît dans aucune proposition.
- **CA-2** — Étant donné un candidat ayant postulé à l'offre, quand le sourcing s'exécute, alors il n'apparaît pas en double dans les profils sourcés.

## 5. À compléter avant revue

Acteurs et déclencheurs · parcours nominal détaillé · modèle de données touché · interfaces et
écrans concernés · cas limites et erreurs · exigences non fonctionnelles applicables · télémétrie.

## 6. Questions ouvertes

| # | Question | Bloquante | Responsable | Échéance |
|---|---|---|---|---|
| 1 | Le candidat est-il notifié à chaque proposition ou de façon groupée ? | Non | Produit et juridique | M4 |
| 2 | Quel seuil de score et quel nombre maximal ? | Non | Produit | M4 |

## 7. Historique

| Version | Date | Changement |
|---|---|---|
| 0.1 | 2026-09-23 | Création |
