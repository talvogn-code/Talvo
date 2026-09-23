---
id: ADR-007
titre: Canal des notifications critiques
statut: proposée
jalon_de_decision: M4
date: 2026-09-23
---

# ADR-007 — Canal des notifications critiques

**Statut** : `proposée` · **À trancher avant la fin du jalon** `M4`

## Contexte

L'invitation à passer un test est le point de rupture du parcours : une invitation qui n'arrive pas est une candidature perdue et un client déçu. Le cahier des charges place le SMS et WhatsApp après le MVP. Par ailleurs, le message unitaire est facturé, et à l'échelle ce poste peut dépasser celui des modèles d'IA.

## Options

### E-mail seul

Gratuit, mais taux de lecture faible dans le public visé.

### E-mail avec repli SMS

Compromis coût et fiabilité.

### SMS en priorité pour les notifications critiques

Le plus fiable, le plus coûteux.

### WhatsApp Business

Usage répandu, contrainte de modèles de messages et d'accord préalable.

## Critères de décision

- Devis opérateurs locaux comparés aux agrégateurs internationaux — l'écart va de trois à dix fois.
- Taux de remise et de lecture mesurés pendant le pilote.
- Budget mensuel plafond accepté pour ce poste.

## Conséquences et invariants

Quel que soit le choix, chaque envoi est tracé avec son canal, son statut de remise et son coût unitaire, pour pouvoir arbitrer sur des chiffres après le pilote.

## Décision

*Non prise.* À compléter : option retenue, date, personnes, et justification au regard des critères ci-dessus.
