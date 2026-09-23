---
id: ADR-005
titre: Modèles à poids ouverts ou interfaces fermées
statut: proposée
jalon_de_decision: M0
date: 2026-09-23
---

# ADR-005 — Modèles à poids ouverts ou interfaces fermées

**Statut** : `proposée` · **À trancher avant la fin du jalon** `M0`

## Contexte

Le rapport performance sur prix des modèles à poids ouverts, notamment chinois, est aujourd'hui parmi les meilleurs. Mais la plupart sont optimisés pour le chinois et l'anglais ; le français et le vocabulaire des CV francophones d'Afrique de l'Ouest ne sont pas leur terrain par défaut, et une erreur d'accentuation dégrade le classement en silence.

## Options

### Interface fermée

Qualité de sortie structurée généralement supérieure, aucune exploitation, coût variable pur.

### Poids ouverts hébergés par un tiers

Coût plus bas, possibilité de bascule.

### Poids ouverts auto-hébergés

Souveraineté des données, indépendance tarifaire, et surtout possibilité d'affiner le modèle plus tard.

## Critères de décision

- Performance mesurée sur le français, sur le corpus TalVo.
- Volume mensuel à douze et trente-six mois — un GPU dédié se justifie mal face à une charge en rafales.
- Exigences de localisation des données exprimées par les clients.

## Conséquences et invariants

L'argument principal en faveur des poids ouverts n'est pas le prix mais l'option d'affinage, qu'une interface fermée referme définitivement. À performance égale sur le corpus, préférer les poids ouverts.

## Décision

*Non prise.* À compléter : option retenue, date, personnes, et justification au regard des critères ci-dessus.
