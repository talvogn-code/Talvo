---
id: ADR-004
titre: Chaîne de lecture des CV
statut: proposée
jalon_de_decision: M0
date: 2026-09-23
---

# ADR-004 — Chaîne de lecture des CV

**Statut** : `proposée` · **À trancher avant la fin du jalon** `M0`

## Contexte

Le produit repose sur la capacité à comprendre un document déposé par un inconnu. Les parseurs du marché, les plateformes de traitement documentaire et les approches multimodales sont tous bons sur leurs démonstrations, faites sur des documents qui ne ressemblent pas à ceux que TalVo recevra.

## Options

### Chaîne classique

Reconnaissance optique commerciale puis extraction structurée par modèle de langage.

### Approche multimodale directe

La page image est donnée au modèle qui produit le résultat structuré, sans étape séparée.

### Parseur de CV du marché

Mature, mais calibré sur des CV occidentaux et contraint le schéma.

### Auto-hébergement

Modèles à poids ouverts sur infrastructure propre.

## Critères de décision

- Exactitude par champ mesurée sur le corpus TalVo, **le français étant le critère de premier rang**.
- Taux d'échec total sur les documents dégradés.
- Coût par CV, latence, effort de correction résiduel côté candidat.

## Conséquences et invariants

Quelle que soit l'option, les fournisseurs restent derrière `OcrProvider` et `ExtractionProvider`. `SPEC-003` est rédigée indépendamment du fournisseur et n'est pas bloquée par cette décision.

## Décision

*Non prise.* À compléter : option retenue, date, personnes, et justification au regard des critères ci-dessus.
