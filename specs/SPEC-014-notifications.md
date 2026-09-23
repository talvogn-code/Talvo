---
id: SPEC-014
titre: Notifications
statut: brouillon
version: 0.1
jalon: M1
priorite: P0
exigences: [EXI-TST-01]
depend_de: [SPEC-001]
auteur: ""
derniere_maj: 2026-09-23
---

# SPEC-014 — Notifications

> **Brouillon.** Les règles et critères ci-dessous sont des amorces issues du cahier des charges
> et de l'analyse. Ils doivent être complétés et revus avant approbation.

## 1. Objectif

Faire parvenir à un candidat une information qui conditionne la suite de son parcours — au premier rang desquelles l'invitation à un test.

## 2. Hors périmètre

Messagerie entre recruteur et candidat (`SPEC-018`).

## 3. Règles métier pressenties

- **RG-1** — Chaque notification a un canal préféré et un canal de repli.
- **RG-2** — Les notifications dont dépend la poursuite du parcours — code de connexion, invitation à un test, rappel avant échéance — passent par le canal le plus fiable, quel qu'en soit le coût.
- **RG-3** — Les notifications d'information peuvent être groupées et différées.
- **RG-4** — Chaque envoi est tracé avec son canal, son statut de remise et son coût unitaire.
- **RG-5** — Le candidat choisit ses canaux et se désabonne des notifications non essentielles.

## 4. Critères d'acceptation amorcés

- **CA-1** — Étant donné une invitation à un test, quand elle est envoyée, alors son canal, sa remise et son coût sont enregistrés.
- **CA-2** — Étant donné un candidat désabonné des notifications d'information, quand une invitation à un test est déclenchée, alors elle lui parvient malgré tout.
- **CA-3** — Étant donné un échec de remise sur le canal préféré, quand le repli existe, alors il est utilisé et l'événement tracé.

## 5. À compléter avant revue

Acteurs et déclencheurs · parcours nominal détaillé · modèle de données touché · interfaces et
écrans concernés · cas limites et erreurs · exigences non fonctionnelles applicables · télémétrie.

## 6. Questions ouvertes

| # | Question | Bloquante | Responsable | Échéance |
|---|---|---|---|---|
| 1 | Canal retenu pour les invitations aux tests — `ADR-007` | **Oui** | Direction | M4 |
| 2 | Budget mensuel plafond pour les envois, et comportement à l'approche du plafond | **Oui** | Direction | M3 |

## 7. Historique

| Version | Date | Changement |
|---|---|---|
| 0.1 | 2026-09-23 | Création |
