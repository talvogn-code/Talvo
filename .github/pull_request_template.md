## Ce que fait cette PR

<!-- Une à trois phrases. Le pourquoi avant le comment. -->

## Spec

<!-- Obligatoire pour tout code applicatif. Une PR sans spec approuvée est du périmètre non décidé. -->

- Spec : `SPEC-0xx`
- Critères couverts : `CA-x`, `CA-y`
- Décision associée, le cas échéant : `ADR-00x`

## Type

- [ ] Spécification (nouvelle ou modifiée)
- [ ] Décision technique
- [ ] Documentation
- [ ] Implémentation d'une spec approuvée
- [ ] Correction
- [ ] Outillage

## Vérifications

- [ ] Les tests des critères d'acceptation cités existent et passent
- [ ] `python3 scripts/check_specs.py` ne signale aucune erreur
- [ ] Aucune règle invariante du domaine n'est contournée (voir `CLAUDE.md`)
- [ ] Migration éventuelle : en expansion, compatible avec la version précédente du code,
      et **sans le code qui l'utilise** dans le même déploiement
- [ ] Événements de télémétrie prévus par la spec émis
- [ ] Aucune donnée réelle, aucun secret, aucune adresse interne dans le diff

## Ce qui reste à faire

<!-- Ce que cette PR ne fait pas volontairement, et où c'est suivi. -->
