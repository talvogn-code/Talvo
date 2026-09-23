---
id: SPEC-002
titre: Profil candidat
statut: brouillon
version: 0.1
jalon: M2
priorite: P0
exigences: [EXI-PRF-01, EXI-PRF-02, EXI-PRF-03]
depend_de: [SPEC-001, SPEC-003]
auteur: ""
derniere_maj: 2026-09-23
---

# SPEC-002 — Profil candidat

> **Brouillon.** Les règles et critères ci-dessous sont des amorces issues du cahier des charges
> et de l'analyse. Ils doivent être complétés et revus avant approbation.

## 1. Objectif

Donner au candidat un profil professionnel qu'il maîtrise : ce que TalVo a compris de lui, ce qu'il corrige, et ce qu'il accepte de rendre visible aux recruteurs.

## 2. Hors périmètre

Extraction du CV (`SPEC-003`) · créateur de CV (`SPEC-004`) · recommandations d'offres (`SPEC-017`).

## 3. Règles métier pressenties

- **RG-1** — Le profil est constitué des éléments validés par le candidat, jamais de données extraites non confirmées.
- **RG-2** — La complétude est calculée sur des critères explicites et affichée au candidat avec ce qui lui manque.
- **RG-3** — L'apparition dans le vivier proposé aux recruteurs exige un consentement explicite, révocable à tout moment.
- **RG-4** — La révocation du consentement retire immédiatement le profil des listes de sourcing, sans effacer les candidatures déjà envoyées.

## 4. Critères d'acceptation amorcés

- **CA-1** — Étant donné un profil dont le consentement au sourcing est retiré, quand un recruteur consulte les profils sourcés, alors ce profil n'y figure plus.
- **CA-2** — Étant donné un profil incomplet, quand le candidat l'ouvre, alors il voit précisément quels éléments manquent.
- **CA-3** — Étant donné une donnée extraite non validée, quand le profil est affiché à un recruteur, alors cette donnée n'apparaît pas.

## 5. À compléter avant revue

Acteurs et déclencheurs · parcours nominal détaillé · modèle de données touché · interfaces et
écrans concernés · cas limites et erreurs · exigences non fonctionnelles applicables · télémétrie.

## 6. Questions ouvertes

| # | Question | Bloquante | Responsable | Échéance |
|---|---|---|---|---|
| 1 | Quels critères entrent dans le calcul de complétude, et avec quel poids ? | Non | Produit | M2 |
| 2 | Le consentement au sourcing est-il global ou excluable par entreprise ? | Non | Produit et juridique | M4 |

## 7. Historique

| Version | Date | Changement |
|---|---|---|
| 0.1 | 2026-09-23 | Création |
