---
id: SPEC-011
titre: Shortlist et fiche candidat
statut: brouillon
version: 0.1
jalon: M4
priorite: P0
exigences: [EXI-PRS-01, EXI-PRS-02, EXI-PRS-03, EXI-CND-06, EXI-TST-08]
depend_de: [SPEC-008, SPEC-010]
auteur: ""
derniere_maj: 2026-09-23
---

# SPEC-011 — Shortlist et fiche candidat

> **Brouillon.** Les règles et critères ci-dessous sont des amorces issues du cahier des charges
> et de l'analyse. Ils doivent être complétés et revus avant approbation.

## 1. Objectif

Transmettre au recruteur une sélection courte et justifiée, et lui donner la fiche sur laquelle décider.

## 2. Hors périmètre

Calcul du score (`SPEC-008`) · messagerie (`SPEC-018`).

## 3. Règles métier pressenties

- **RG-1** — La fiche candidat présente le score **et le résumé en langage naturel des éléments qui l'ont produit**.
- **RG-2** — Les résultats de tests requis filtrent la shortlist ; ils ne modifient jamais le score de correspondance.
- **RG-3** — Un candidat n'ayant pas passé un test obligatoire est écarté de la shortlist, mais reste visible dans la liste des candidatures.
- **RG-4** — Une shortlist est un objet daté et traçable : on sait ce qui a été transmis, quand et par qui.
- **RG-5** — Les actions du recruteur — présélectionner, contacter, entretien, écarter — sont journalisées.

## 4. Critères d'acceptation amorcés

- **CA-1** — Étant donné une offre avec test obligatoire, quand la shortlist est produite, alors aucun candidat sous le seuil n'y figure.
- **CA-2** — Étant donné une fiche candidat, quand elle est ouverte, alors elle affiche pour chaque critère l'élément concret qui a produit le sous-score.
- **CA-3** — Étant donné une shortlist transmise, quand on la consulte un mois plus tard, alors on retrouve son contenu exact au moment de l'envoi.

## 5. À compléter avant revue

Acteurs et déclencheurs · parcours nominal détaillé · modèle de données touché · interfaces et
écrans concernés · cas limites et erreurs · exigences non fonctionnelles applicables · télémétrie.

## 6. Questions ouvertes

| # | Question | Bloquante | Responsable | Échéance |
|---|---|---|---|---|
| 1 | La shortlist est-elle produite automatiquement ou validée par TalVo avant envoi ? | **Oui** | Direction | M4 |
| 2 | Combien de profils par shortlist ? | Non | Produit | M4 |

## 7. Historique

| Version | Date | Changement |
|---|---|---|
| 0.1 | 2026-09-23 | Création |
