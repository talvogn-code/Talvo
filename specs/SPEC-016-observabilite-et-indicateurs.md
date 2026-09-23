---
id: SPEC-016
titre: Observabilité et indicateurs
statut: brouillon
version: 0.1
jalon: M1
priorite: P0
exigences: [NFR-08, NFR-09, NFR-10, NFR-12, NFR-17]
depend_de: []
auteur: ""
derniere_maj: 2026-09-23
---

# SPEC-016 — Observabilité et indicateurs

> **Brouillon.** Les règles et critères ci-dessous sont des amorces issues du cahier des charges
> et de l'analyse. Ils doivent être complétés et revus avant approbation.

## 1. Objectif

Savoir ce qui se passe en production, être averti avant les utilisateurs, et pouvoir mesurer au pilote ce que le cahier des charges promet de mesurer.

## 2. Hors périmètre

Tableaux de bord destinés aux utilisateurs (`SPEC-012`).

## 3. Règles métier pressenties

- **RG-1** — Le signal principal n'est pas le taux d'erreur mais **la profondeur de la file et l'âge du plus vieux travail** : un document bloqué ne lève aucune erreur.
- **RG-2** — Les événements nécessaires au calcul des indicateurs du cadrage sont émis dès la V1 — une donnée non collectée en janvier est définitivement perdue.
- **RG-3** — Le temps réellement passé par un recruteur sur une offre est mesuré : c'est la preuve de la promesse commerciale.
- **RG-4** — Les sauvegardes sont automatiques et **leur restauration est testée périodiquement**, avec chronométrage.
- **RG-5** — Aucune donnée de production n'est copiée dans un autre environnement.
- **RG-6** — Les horodatages sont stockés en temps universel et affichés en heure locale.

## 4. Critères d'acceptation amorcés

- **CA-1** — Étant donné un travail bloqué en file depuis plus de dix minutes, quand la surveillance s'exécute, alors une alerte est émise.
- **CA-2** — Étant donné une sauvegarde, quand la procédure de restauration est jouée, alors la base est reconstituée et la durée est enregistrée.
- **CA-3** — Étant donné les quatorze indicateurs du cadrage, quand on les calcule, alors chacun s'appuie sur des événements réellement émis.

## 5. À compléter avant revue

Acteurs et déclencheurs · parcours nominal détaillé · modèle de données touché · interfaces et
écrans concernés · cas limites et erreurs · exigences non fonctionnelles applicables · télémétrie.

## 6. Questions ouvertes

| # | Question | Bloquante | Responsable | Échéance |
|---|---|---|---|---|
| 1 | Quelle perte de données maximale acceptable, et quelle durée d'interruption acceptable ? | **Oui** | Direction | M1 |
| 2 | À quelle fréquence la restauration est-elle testée ? | Non | CTO | M1 |

## 7. Historique

| Version | Date | Changement |
|---|---|---|
| 0.1 | 2026-09-23 | Création |
