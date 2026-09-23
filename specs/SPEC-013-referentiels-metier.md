---
id: SPEC-013
titre: Référentiels métier
statut: brouillon
version: 0.1
jalon: M1
priorite: P0
exigences: [EXI-MCH-10, EXI-ADM-03, NFR-11]
depend_de: []
auteur: ""
derniere_maj: 2026-09-23
---

# SPEC-013 — Référentiels métier

> **Brouillon.** Les règles et critères ci-dessous sont des amorces issues du cahier des charges
> et de l'analyse. Ils doivent être complétés et revus avant approbation.

## 1. Objectif

Constituer et maintenir le dictionnaire qui rend le classement reproductible : compétences, fonctions, diplômes, secteurs, avec leurs alias et leurs équivalences locales.

## 2. Hors périmètre

Le moteur de classement lui-même (`SPEC-008`).

## 3. Règles métier pressenties

- **RG-1** — Chaque entrée porte un identifiant stable, un libellé, des alias, et son pays d'application quand elle est locale.
- **RG-2** — Les diplômes guinéens et régionaux sont ramenés à une échelle de niveaux comparables.
- **RG-3** — Un alias proposé par la similarité sémantique n'entre au référentiel qu'après validation humaine.
- **RG-4** — Toute modification du référentiel est versionnée et journalisée : elle change les scores.
- **RG-5** — Le référentiel est structuré par pays dès l'origine, même avec un seul pays ouvert.

## 4. Critères d'acceptation amorcés

- **CA-1** — Étant donné deux graphies d'une même compétence, quand elles sont normalisées, alors elles produisent le même identifiant.
- **CA-2** — Étant donné une modification du référentiel, quand elle est enregistrée, alors l'auteur, la date et l'ancienne valeur sont conservés.
- **CA-3** — Étant donné un diplôme local, quand il est normalisé, alors il porte un niveau comparable à un diplôme international équivalent.

## 5. À compléter avant revue

Acteurs et déclencheurs · parcours nominal détaillé · modèle de données touché · interfaces et
écrans concernés · cas limites et erreurs · exigences non fonctionnelles applicables · télémétrie.

## 6. Questions ouvertes

| # | Question | Bloquante | Responsable | Échéance |
|---|---|---|---|---|
| 1 | Qui est propriétaire du référentiel et le maintient dans la durée ? | **Oui** | Direction | M1 |
| 2 | Partons-nous d'une base existante à adapter, ou de zéro ? | **Oui** | CTO | M1 |

## 7. Historique

| Version | Date | Changement |
|---|---|---|
| 0.1 | 2026-09-23 | Création |
