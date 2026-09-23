---
id: SPEC-018
titre: Messagerie
statut: brouillon
version: 0.1
jalon: M7
priorite: P1
exigences: [EXI-MON-02, EXI-MON-04]
depend_de: [SPEC-007, SPEC-017]
auteur: ""
derniere_maj: 2026-09-23
---

# SPEC-018 — Messagerie

> **Brouillon.** Les règles et critères ci-dessous sont des amorces issues du cahier des charges
> et de l'analyse. Ils doivent être complétés et revus avant approbation.

## 1. Objectif

Permettre un échange encadré entre un recruteur et un candidat, rattaché à un recrutement précis.

## 2. Hors périmètre

Notifications système (`SPEC-014`).

## 3. Règles métier pressenties

- **RG-1** — Une conversation est toujours rattachée à une offre et à une candidature ou à une proposition de sourcing.
- **RG-2** — Les coordonnées personnelles ne sont pas exposées tant que les deux parties n'ont pas échangé.
- **RG-3** — Les notes internes du recruteur ne peuvent jamais être envoyées par erreur dans une conversation.
- **RG-4** — Un candidat signale un message abusif, et le signalement rejoint la file de modération.
- **RG-5** — Aucun message ne peut demander un paiement au candidat ; ce motif est explicitement surveillé.

## 4. Critères d'acceptation amorcés

- **CA-1** — Étant donné une note interne, quand le recruteur compose un message, alors la note n'est pas insérable dans la conversation.
- **CA-2** — Étant donné une conversation, quand elle est ouverte, alors elle affiche l'offre à laquelle elle se rattache.

## 5. À compléter avant revue

Acteurs et déclencheurs · parcours nominal détaillé · modèle de données touché · interfaces et
écrans concernés · cas limites et erreurs · exigences non fonctionnelles applicables · télémétrie.

## 6. Questions ouvertes

| # | Question | Bloquante | Responsable | Échéance |
|---|---|---|---|---|
| 1 | Un candidat gratuit peut-il répondre à un recruteur qui l'a contacté ? | **Oui** | Produit | M7 |

## 7. Historique

| Version | Date | Changement |
|---|---|---|
| 0.1 | 2026-09-23 | Création |
