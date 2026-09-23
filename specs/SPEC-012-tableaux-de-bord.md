---
id: SPEC-012
titre: Tableaux de bord
statut: brouillon
version: 0.1
jalon: M4
priorite: P0
exigences: [EXI-DSH-01, EXI-DSH-02, NFR-13, NFR-14]
depend_de: [SPEC-007, SPEC-011]
auteur: ""
derniere_maj: 2026-09-23
---

# SPEC-012 — Tableaux de bord

> **Brouillon.** Les règles et critères ci-dessous sont des amorces issues du cahier des charges
> et de l'analyse. Ils doivent être complétés et revus avant approbation.

## 1. Objectif

Donner à chaque acteur la vue d'ensemble dont il a besoin pour agir, en une page, sans chercher.

## 2. Hors périmètre

Tableau de bord d'administration (`SPEC-015`) · indicateurs internes (`SPEC-016`).

## 3. Règles métier pressenties

- **RG-1** — Le tableau de bord candidat expose profil et complétude, candidatures, CV, tests et scores, badges, notifications.
- **RG-2** — Le tableau de bord entreprise expose offres actives, candidatures, profils correspondants, présélections, tests, shortlists, pipeline.
- **RG-3** — Toute chaîne visible par l'utilisateur passe par le mécanisme de traduction, même avec une seule langue active.
- **RG-4** — Les vues sont utilisables sur téléphone en réseau contraint : pas de tableau qui déborde, pas de chargement bloquant.

## 4. Critères d'acceptation amorcés

- **CA-1** — Étant donné un tableau de bord, quand il est inspecté, alors aucune chaîne destinée à l'utilisateur n'est écrite en dur dans le code.
- **CA-2** — Étant donné un écran de tableau de bord, quand il est affiché à 400 pixels de large, alors aucun défilement horizontal de page n'apparaît.

## 5. À compléter avant revue

Acteurs et déclencheurs · parcours nominal détaillé · modèle de données touché · interfaces et
écrans concernés · cas limites et erreurs · exigences non fonctionnelles applicables · télémétrie.

## 6. Questions ouvertes

| # | Question | Bloquante | Responsable | Échéance |
|---|---|---|---|---|
| 1 | Quels indicateurs mettons-nous en tête pour l'entreprise ? | Non | Produit | M4 |

## 7. Historique

| Version | Date | Changement |
|---|---|---|
| 0.1 | 2026-09-23 | Création |
