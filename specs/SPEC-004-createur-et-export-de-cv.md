---
id: SPEC-004
titre: Créateur et export de CV
statut: brouillon
version: 0.1
jalon: M2
priorite: P0
exigences: [EXI-CV-07, EXI-CV-08]
depend_de: [SPEC-002]
auteur: ""
derniere_maj: 2026-09-23
---

# SPEC-004 — Créateur et export de CV

> **Brouillon.** Les règles et critères ci-dessous sont des amorces issues du cahier des charges
> et de l'analyse. Ils doivent être complétés et revus avant approbation.

## 1. Objectif

Permettre à un candidat qui n'a pas de CV, ou dont le CV est mauvais, d'en produire un lisible par un humain comme par une machine.

## 2. Hors périmètre

Import (`SPEC-003`) · adaptation à une offre (`SPEC-017`).

## 3. Règles métier pressenties

- **RG-1** — L'aperçu à l'écran et le PDF exporté sont produits par le même moteur de rendu : ce que le candidat voit est ce qu'il télécharge.
- **RG-2** — La pagination ne coupe jamais une ligne ni n'isole un titre de section en bas de page.
- **RG-3** — Les accents français sont rendus à l'identique à l'écran et au PDF.
- **RG-4** — Les CV produits sont structurés pour être relus correctement par un système de tri automatique — à commencer par celui de TalVo.
- **RG-5** — Une bibliothèque de formulations par métier, localisée, est proposée au candidat ; elle ne remplit jamais un champ à sa place sans action de sa part.

## 4. Critères d'acceptation amorcés

- **CA-1** — Étant donné un CV créé dans TalVo, quand il est exporté puis réimporté, alors l'extraction retrouve l'intégralité des champs sans champ à valider.
- **CA-2** — Étant donné une expérience dont la description atteint le bas d'une page, quand le PDF est produit, alors elle n'est pas coupée en milieu de ligne.
- **CA-3** — Étant donné un nom comportant des accents, quand le PDF est produit, alors ils s'affichent correctement dans un lecteur standard.

## 5. À compléter avant revue

Acteurs et déclencheurs · parcours nominal détaillé · modèle de données touché · interfaces et
écrans concernés · cas limites et erreurs · exigences non fonctionnelles applicables · télémétrie.

## 6. Questions ouvertes

| # | Question | Bloquante | Responsable | Échéance |
|---|---|---|---|---|
| 1 | Combien de modèles proposons-nous à la V1 ? | Non | Produit et design | M2 |
| 2 | Qui produit la bibliothèque de formulations et selon quel calendrier ? | **Oui** | Direction | M1 |

## 7. Historique

| Version | Date | Changement |
|---|---|---|
| 0.1 | 2026-09-23 | Création |
