---
id: SPEC-017
titre: Premium et visibilité
statut: brouillon
version: 0.1
jalon: M7
priorite: P1
exigences: [EXI-CPT-06, EXI-CV-09, EXI-CV-10, EXI-CV-11, EXI-OFF-06, EXI-MON-01, EXI-MON-03]
depend_de: [SPEC-004, SPEC-008]
auteur: ""
derniere_maj: 2026-09-23
---

# SPEC-017 — Premium et visibilité

> **Brouillon.** Les règles et critères ci-dessous sont des amorces issues du cahier des charges
> et de l'analyse. Ils doivent être complétés et revus avant approbation.

## 1. Objectif

Ouvrir au candidat abonné ce qui lui manque pour agir : le nom de l'entreprise, des offres qui lui correspondent, et un CV adapté à chaque offre — sans jamais inventer une ligne.

## 2. Hors périmètre

Messagerie et contact RH (`SPEC-018`) · encaissement (`ADR-009`).

## 3. Règles métier pressenties

- **RG-1** — Le statut Premium découle d'un abonnement actif, jamais d'un rôle attribué à la main.
- **RG-2** — Un CV adapté ne contient **que** des informations présentes dans le profil ou le CV source. Chaque affirmation produite doit être rattachable à un élément de la source ; ce qui ne l'est pas est supprimé ou signalé.
- **RG-3** — Les éléments manquants au regard de l'offre sont signalés au candidat — c'est la soupape qui évite l'invention.
- **RG-4** — Les prix sont affichés clairement, la reconduction est explicite, la résiliation prend effet immédiatement.
- **RG-5** — La perte du statut Premium remasque le nom des entreprises sans supprimer l'historique du candidat.

## 4. Critères d'acceptation amorcés

- **CA-1** — Étant donné un CV adapté, quand chaque affirmation est confrontée à la source, alors aucune compétence, aucun diplôme et aucune expérience absents de la source n'y figurent.
- **CA-2** — Étant donné un abonnement résilié, quand le candidat consulte une offre, alors le nom de l'entreprise est à nouveau masqué.
- **CA-3** — Étant donné une souscription, quand le candidat demande la résiliation, alors elle est effective sans intervention humaine.

## 5. À compléter avant revue

Acteurs et déclencheurs · parcours nominal détaillé · modèle de données touché · interfaces et
écrans concernés · cas limites et erreurs · exigences non fonctionnelles applicables · télémétrie.

## 6. Questions ouvertes

| # | Question | Bloquante | Responsable | Échéance |
|---|---|---|---|---|
| 1 | Prix en monnaie locale et périodicité | **Oui** | Direction | M7 |
| 2 | Moyen de paiement — `ADR-009` | **Oui** | Direction | M7 |

## 7. Historique

| Version | Date | Changement |
|---|---|---|
| 0.1 | 2026-09-23 | Création |
