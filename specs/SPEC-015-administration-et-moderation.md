---
id: SPEC-015
titre: Administration et modération
statut: brouillon
version: 0.1
jalon: M5
priorite: P0
exigences: [EXI-CPT-05, EXI-ADM-02, EXI-ADM-04, EXI-ADM-05, NFR-18]
depend_de: [SPEC-005]
auteur: ""
derniere_maj: 2026-09-23
---

# SPEC-015 — Administration et modération

> **Brouillon.** Les règles et critères ci-dessous sont des amorces issues du cahier des charges
> et de l'analyse. Ils doivent être complétés et revus avant approbation.

## 1. Objectif

Donner à l'équipe TalVo les moyens de valider, corriger, modérer et rendre compte — avec une trace de chaque geste.

## 2. Hors périmètre

Validation des entreprises, décrite dans `SPEC-005`.

## 3. Règles métier pressenties

- **RG-1** — Toute action d'administration est journalisée avec son auteur, sa cible, l'état avant et après, et son motif.
- **RG-2** — La consultation d'un profil candidat par un administrateur est elle aussi journalisée.
- **RG-3** — La file de modération priorise les signalements portant sur des offres publiées.
- **RG-4** — Les documents juridiques — conditions générales, politique de confidentialité, registre des traitements — sont publiés avant l'ouverture au public.
- **RG-5** — Une demande d'accès, de rectification ou d'effacement d'un utilisateur est traitée par une procédure outillée, pas à la main dans la base.

## 4. Critères d'acceptation amorcés

- **CA-1** — Étant donné une action de modération, quand le journal est consulté, alors on retrouve l'auteur, la cible, le motif et l'horodatage.
- **CA-2** — Étant donné une demande d'effacement, quand elle est exécutée, alors les données personnelles sont supprimées et la trace de la demande conservée.

## 5. À compléter avant revue

Acteurs et déclencheurs · parcours nominal détaillé · modèle de données touché · interfaces et
écrans concernés · cas limites et erreurs · exigences non fonctionnelles applicables · télémétrie.

## 6. Questions ouvertes

| # | Question | Bloquante | Responsable | Échéance |
|---|---|---|---|---|
| 1 | Qui assure la modération au quotidien pendant le pilote ? | **Oui** | Opérations | M5 |
| 2 | Durée de conservation par catégorie de données | **Oui** | Juridique | M5 |

## 7. Historique

| Version | Date | Changement |
|---|---|---|
| 0.1 | 2026-09-23 | Création |
