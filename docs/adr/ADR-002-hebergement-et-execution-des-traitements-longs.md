---
id: ADR-002
titre: Hébergement et exécution des traitements longs
statut: proposée
jalon_de_decision: M1
date: 2026-09-23
---

# ADR-002 — Hébergement et exécution des traitements longs

**Statut** : `proposée` · **À trancher avant la fin du jalon** `M1`

## Contexte

La chaîne documentaire impose des traitements longs, par rafales, avec des workers élastiques. C'est cette charge, et non les préférences de framework, qui contraint l'hébergement. Une plateforme entièrement sans serveur orientée requête et réponse ne convient pas comme point de départ.

## Options

### Conteneurs orchestrés en région choisie

Calcul maîtrisé, coût prévisible, région explicite. Un peu d'exploitation à assumer.

### Plateforme managée applicative

Moins d'exploitation, mais contraintes de durée d'exécution et dépendance forte.

### Mixte

Application et workers en conteneurs, dépendances managées pour la base et le stockage.

## Critères de décision

- Exigences de localisation des données exprimées par les entreprises pilotes.
- Coût au volume du pilote puis à maturité sur Conakry.
- Capacité à faire monter les workers indépendamment du site.

## Conséquences et invariants

Le répartiteur de charge est mis en place dès le début, non pour la charge mais pour les mises à jour sans coupure.

## Décision

*Non prise.* À compléter : option retenue, date, personnes, et justification au regard des critères ci-dessus.
