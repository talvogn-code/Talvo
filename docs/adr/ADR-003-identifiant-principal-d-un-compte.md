---
id: ADR-003
titre: Identifiant principal d'un compte
statut: proposée
jalon_de_decision: M0
date: 2026-09-23
---

# ADR-003 — Identifiant principal d'un compte

**Statut** : `proposée` · **À trancher avant la fin du jalon** `M0`

## Contexte

Le cahier des charges suppose implicitement une adresse e-mail. En Guinée, le téléphone est l'identifiant réel ; l'e-mail est secondaire, parfois inexistant ou jamais consulté. Exiger un e-mail vérifié écarterait une part des candidats, et cet écart serait invisible dans les statistiques puisqu'on ne mesure pas ceux qui abandonnent.

## Options

### Téléphone avec code à usage unique

Correspond à l'usage réel. Coût par code envoyé, et gestion des changements de numéro.

### Adresse e-mail et mot de passe

Gratuit, standard, mais exclut une partie du public visé.

### Les deux au choix

Couverture maximale, complexité de récupération de compte plus élevée.

## Critères de décision

- Part réelle des candidats disposant d'une adresse e-mail active — à estimer auprès des entreprises pilotes et des universités.
- Coût unitaire du message, une fois les devis opérateurs obtenus.
- Conséquences sur `SPEC-001`, qui ne peut être approuvée avant cette décision.

## Conséquences et invariants

Cette décision modifie le modèle de données : la contrainte d'unicité et de non-nullité sur l'adresse e-mail est concernée.

## Décision

*Non prise.* À compléter : option retenue, date, personnes, et justification au regard des critères ci-dessus.
