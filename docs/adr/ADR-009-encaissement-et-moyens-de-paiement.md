---
id: ADR-009
titre: Encaissement et moyens de paiement
statut: proposée
jalon_de_decision: M7
date: 2026-09-23
---

# ADR-009 — Encaissement et moyens de paiement

**Statut** : `proposée` · **À trancher avant la fin du jalon** `M7`

## Contexte

Le cahier des charges autorise la facturation manuelle des entreprises pilotes. Pour l'abonnement candidat en revanche, les moyens de paiement locaux pèseront bien plus que la carte bancaire, et le niveau de prix des plateformes occidentales est hors d'atteinte pour un candidat guinéen.

## Options

### Mobile money en priorité

Correspond à l'usage, mais intégration par opérateur et réconciliation à outiller.

### Agrégateur de paiement régional

Une seule intégration pour plusieurs opérateurs, commission plus élevée.

### Carte bancaire seule

Simple, mais public très restreint.

## Critères de décision

- Part des candidats disposant d'un compte mobile money.
- Commissions et délais de reversement.
- Difficulté du remboursement en cas de litige — elle impose une politique de résiliation immédiate et sans friction.

## Conséquences et invariants

Nous n'imitons pas les pratiques d'abonnement agressives des plateformes occidentales : prix affichés, reconduction explicite, résiliation immédiate. Sur un produit biface, un candidat qui se sent piégé abîme l'actif que nous vendons aux entreprises.

## Décision

*Non prise.* À compléter : option retenue, date, personnes, et justification au regard des critères ci-dessus.
