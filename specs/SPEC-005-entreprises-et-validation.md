---
id: SPEC-005
titre: Entreprises et validation
statut: brouillon
version: 0.1
jalon: M3
priorite: P0
exigences: [EXI-CPT-03, EXI-CPT-04, EXI-PRF-04, EXI-ADM-01]
depend_de: [SPEC-001]
auteur: ""
derniere_maj: 2026-09-23
---

# SPEC-005 — Entreprises et validation

> **Brouillon.** Les règles et critères ci-dessous sont des amorces issues du cahier des charges
> et de l'analyse. Ils doivent être complétés et revus avant approbation.

## 1. Objectif

Vérifier qu'une organisation est réelle avant de lui laisser publier une offre publique, et lui donner un espace à plusieurs utilisateurs.

## 2. Hors périmètre

Publication d'offres (`SPEC-006`) · facturation (`SPEC-017`).

## 3. Règles métier pressenties

- **RG-1** — Une organisation reste en statut `en attente` tant qu'un administrateur ne l'a pas validée. Elle peut préparer des offres en brouillon, jamais publier.
- **RG-2** — La validation s'appuie sur des pièces déclarées — registre du commerce, identifiant fiscal — et la décision est motivée et journalisée.
- **RG-3** — Un refus est notifié avec son motif et peut être contesté.
- **RG-4** — Un candidat peut signaler une offre en un geste depuis la page de l'offre.
- **RG-5** — Aucune offre ne demande de paiement au candidat ; une mention permanente le rappelle.

## 4. Critères d'acceptation amorcés

- **CA-1** — Étant donné une organisation non validée, quand elle tente de publier une offre, alors la publication est refusée avec un motif clair.
- **CA-2** — Étant donné une organisation validée, quand son administrateur invite un recruteur, alors celui-ci accède aux offres de cette organisation et à aucune autre.
- **CA-3** — Étant donné une offre signalée trois fois, quand le seuil est atteint, alors elle est portée en tête de la file de modération.

## 5. À compléter avant revue

Acteurs et déclencheurs · parcours nominal détaillé · modèle de données touché · interfaces et
écrans concernés · cas limites et erreurs · exigences non fonctionnelles applicables · télémétrie.

## 6. Questions ouvertes

| # | Question | Bloquante | Responsable | Échéance |
|---|---|---|---|---|
| 1 | Quelles pièces exigeons-nous, et qui les vérifie concrètement ? | **Oui** | Direction | M3 |
| 2 | Délai d'engagement pour valider une entreprise ? | Non | Opérations | M3 |

## 7. Historique

| Version | Date | Changement |
|---|---|---|
| 0.1 | 2026-09-23 | Création |
