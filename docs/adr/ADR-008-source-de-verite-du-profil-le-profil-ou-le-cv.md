---
id: ADR-008
titre: Source de vérité du profil : le profil ou le CV
statut: proposée
jalon_de_decision: M2
date: 2026-09-23
---

# ADR-008 — Source de vérité du profil : le profil ou le CV

**Statut** : `proposée` · **À trancher avant la fin du jalon** `M2`

## Contexte

Les expériences et formations peuvent être portées par le CV, le profil n'en étant qu'une agrégation, ou par le profil, le CV n'en étant qu'un rendu. Le cahier des charges laisse les deux lectures ouvertes. Le choix décide de ce que lit le moteur de classement.

## Options

### Le CV porte les données

L'import multi-CV est naturel ; le classement doit désigner un CV de référence.

### Le profil porte les données

Le classement est plus simple ; l'import de plusieurs CV devient une fusion à arbitrer.

## Critères de décision

- Un candidat aura-t-il réellement plusieurs CV actifs à la V1 ?
- Complexité induite pour le moteur de classement.
- Comportement attendu lors d'un second import.

## Conséquences et invariants

Cette décision touche `SPEC-002`, `SPEC-003` et `SPEC-008`. Elle doit être prise avant d'écrire les migrations correspondantes.

## Décision

*Non prise.* À compléter : option retenue, date, personnes, et justification au regard des critères ci-dessus.
