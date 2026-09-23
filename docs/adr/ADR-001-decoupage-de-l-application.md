---
id: ADR-001
titre: Découpage de l'application
statut: proposée
jalon_de_decision: M0
date: 2026-09-23
---

# ADR-001 — Découpage de l'application

**Statut** : `proposée` · **À trancher avant la fin du jalon** `M0`

## Contexte

Le cahier des charges recommande une interface React et une API NestJS séparées. Le découpage réel n'engage ni le modèle de données, ni le moteur de classement, ni la chaîne documentaire — les trois pièces coûteuses à refaire. Il engage en revanche le référencement des pages d'offres, qui est le canal d'acquisition des candidats.

## Options

### Application unique rendue serveur

Un dépôt, un déploiement, référencement natif sur les pages publiques. S'écarte de la lettre du cahier des charges.

### Interface et API séparées

Conforme au cahier des charges, API réutilisable par une future application mobile. Deux déploiements, référencement à traiter à part, plus lent à livrer.

## Critères de décision

- Les pages publiques d'offres doivent être indexables sans exécution de script.
- Qui maintiendra la plateforme après la V1.
- Délai jusqu'au pilote de janvier 2027.

## Conséquences et invariants

Quelle que soit l'option, l'API est organisée en modules aux frontières explicites, pour qu'une extraction ultérieure soit mécanique.

## Décision

*Non prise.* À compléter : option retenue, date, personnes, et justification au regard des critères ci-dessus.
