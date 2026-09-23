---
id: SPEC-000
titre: Titre court et parlant
statut: brouillon
version: 0.1
jalon: M0
priorite: P0
exigences: []
depend_de: []
auteur: ""
derniere_maj: 2026-09-23
---

# SPEC-000 — Titre

## 1. Objectif

Une à trois phrases. **Le problème résolu et pour qui**, pas la solution technique.

## 2. Hors périmètre

Ce que cette spec ne couvre volontairement pas, et où cela est traité.

## 3. Acteurs et déclencheurs

Qui déclenche, dans quel état du système.

## 4. Parcours nominal

Le chemin qui marche, étape par étape, du point de vue de l'utilisateur.

## 5. Règles métier

Numérotées `RG-1`, `RG-2`… Chaque règle est une affirmation vérifiable, sans « devrait ».

## 6. Modèle de données

Tables et champs touchés, créés ou modifiés. Renvoie à `docs/01-modele-donnees.md`.

## 7. Interfaces

Écrans concernés (numéros du cahier des charges), points d'entrée d'API, travaux asynchrones
publiés, événements émis.

## 8. Critères d'acceptation

Numérotés `CA-1`, `CA-2`… Format *étant donné / quand / alors*. **Chacun doit être vérifiable
automatiquement** — si un critère ne peut pas devenir un test, il est mal écrit.

## 9. Cas limites et erreurs

Ce qui arrive quand ça se passe mal : réseau coupé, fichier invalide, double soumission,
accès concurrent, droits insuffisants.

## 10. Exigences non fonctionnelles applicables

Performance, sécurité, données personnelles, accessibilité, journalisation. Renvoie aux
`NFR-xxx` du registre plutôt que de les recopier.

## 11. Télémétrie

Événements émis et indicateurs qu'ils alimentent. **Une donnée non collectée est perdue** :
ce qui n'est pas listé ici ne sera pas mesurable au pilote.

## 12. Questions ouvertes

| # | Question | Bloquante | Responsable | Échéance |
|---|---|---|---|---|

Une question **bloquante** non résolue interdit le passage en `approuvée`.

## 13. Historique

| Version | Date | Changement |
|---|---|---|
| 0.1 | 2026-09-23 | Création |
