---
id: SPEC-007
titre: Candidatures
statut: brouillon
version: 0.1
jalon: M3
priorite: P0
exigences: [EXI-CND-01, EXI-CND-02, EXI-CND-03, EXI-CND-04, EXI-CND-05]
depend_de: [SPEC-002, SPEC-006]
auteur: ""
derniere_maj: 2026-09-23
---

# SPEC-007 — Candidatures

> **Brouillon.** Les règles et critères ci-dessous sont des amorces issues du cahier des charges
> et de l'analyse. Ils doivent être complétés et revus avant approbation.

## 1. Objectif

Relier un candidat à une offre, suivre l'avancement de cette relation, et garder privé ce qui doit l'être.

## 2. Hors périmètre

Classement (`SPEC-008`) · shortlist (`SPEC-011`) · messagerie (`SPEC-018`).

## 3. Règles métier pressenties

- **RG-1** — Un candidat postule une seule fois à une offre donnée.
- **RG-2** — Une candidature exige un profil validé et un CV exploitable.
- **RG-3** — L'état de la candidature suit une suite explicite, visible du candidat dans une formulation qui ne l'humilie pas.
- **RG-4** — Les notes internes du recruteur ne sont jamais visibles du candidat, ni exportées, ni incluses dans un message.
- **RG-5** — Un candidat retire sa candidature tant qu'aucune décision n'est prise.

## 4. Critères d'acceptation amorcés

- **CA-1** — Étant donné un candidat ayant déjà postulé, quand il postule à nouveau, alors le système renvoie sa candidature existante sans en créer une seconde.
- **CA-2** — Étant donné une note interne, quand le candidat consulte sa candidature, alors elle n'apparaît nulle part dans la réponse du serveur.
- **CA-3** — Étant donné une candidature écartée, quand le candidat consulte son suivi, alors la formulation est factuelle et respectueuse.

## 5. À compléter avant revue

Acteurs et déclencheurs · parcours nominal détaillé · modèle de données touché · interfaces et
écrans concernés · cas limites et erreurs · exigences non fonctionnelles applicables · télémétrie.

## 6. Questions ouvertes

| # | Question | Bloquante | Responsable | Échéance |
|---|---|---|---|---|
| 1 | Le candidat voit-il qu'il a été écarté, et à quel moment ? | **Oui** | Produit | M3 |
| 2 | Quelle formulation exacte pour chaque état côté candidat ? | Non | Produit | M3 |

## 7. Historique

| Version | Date | Changement |
|---|---|---|
| 0.1 | 2026-09-23 | Création |
