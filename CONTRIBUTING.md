# Contribuer à TalVo

Ce projet est conduit **par les specs**. Aucune ligne de code applicatif n'est écrite avant
qu'une spécification approuvée ne la décrive. Ce document dit comment le travail circule.

## 1. Le principe

> **Une spec décrit un comportement observable et ses critères d'acceptation.
> Le code la satisfait. Les tests la vérifient. Rien ne part en production sans ce trio.**

La spec n'est pas de la documentation écrite après coup : c'est **l'artefact de conception**.
Elle est discutée, revue et approuvée comme du code, dans le même dépôt, avec le même
historique. Quand la spec et le code divergent, c'est un défaut — de l'un ou de l'autre.

## 2. La chaîne de traçabilité

```
Exigence (EXI-xxx)  →  Spec (SPEC-0xx)  →  Critère d'acceptation (CA-x)  →  Test  →  Code
      registre            specs/              dans la spec               suite      PR
```

Chaque maillon cite le précédent :

- une **exigence** vient du cahier des charges (`docs/00-cadrage-mvp.md`) ou d'un angle mort
  identifié (`docs/07-angles-morts.md`) ; elle est enregistrée dans `docs/10-registre-exigences.md` ;
- une **spec** déclare dans son en-tête les exigences qu'elle couvre ;
- chaque **critère d'acceptation** est numéroté et testable ;
- chaque **test** cite le critère qu'il vérifie ;
- chaque **pull request** cite la spec qu'elle met en œuvre.

Une exigence sans spec est un trou. Une spec sans critère testable est un vœu. Une PR sans
spec est un ajout de périmètre non décidé.

## 3. Cycle de vie d'une spec

| Statut | Signification | Qui fait avancer |
|---|---|---|
| `brouillon` | En cours d'écriture, incomplète | L'auteur |
| `en revue` | Complète, soumise en pull request | Les relecteurs |
| `approuvée` | Revue et acceptée — **l'implémentation peut commencer** | Les deux CTO |
| `implémentée` | Le code la satisfait, tous les critères passent | L'auteur du code |
| `obsolète` | Remplacée ou abandonnée, conservée pour l'historique | — |

**Une spec ne passe pas en `approuvée` s'il lui reste une question ouverte bloquante.**
C'est la règle qui protège le calendrier : une ambiguïté non levée à l'écriture coûte dix fois
plus cher découverte pendant le développement.

## 4. Le flux de travail

### Écrire ou modifier une spec
1. Ouvrir une issue « Proposition de spec » décrivant le besoin.
2. Créer une branche `spec/SPEC-0xx-titre-court`.
3. Copier `specs/TEMPLATE.md`, remplir, statut `brouillon`.
4. Ouvrir une pull request dès que c'est lisible — une spec se discute tôt, pas une fois finie.
5. Passer en `en revue`, obtenir deux approbations, fusionner. La spec devient `approuvée`.

### Implémenter
1. Créer une branche `feat/SPEC-0xx-tranche` (une tranche par PR, pas la spec entière).
2. Écrire les tests des critères d'acceptation **avant** le code.
3. La PR cite `SPEC-0xx` et liste les `CA-x` couverts.
4. Une fois tous les critères couverts, passer la spec en `implémentée`.

### Changer d'avis
Modifier la spec **d'abord**, en PR séparée. Jamais de code qui contredit une spec approuvée :
soit la spec avait tort et on la corrige, soit le code a tort et on le corrige.

## 5. Décisions techniques

Les choix structurants ne vont pas dans les specs mais dans `docs/adr/` — un fichier par
décision, avec son contexte, ses options et ses conséquences. Une décision porte un statut
(`proposée`, `acceptée`, `remplacée`) et **un jalon avant lequel elle doit être tranchée**.

Une spec qui dépend d'une décision non prise le déclare dans ses questions ouvertes.

## 6. Conventions

**Branches** — `spec/`, `feat/`, `fix/`, `chore/`, `docs/`. Courtes, fusionnées en moins de
deux jours (voir le pipeline de livraison).

**Commits** — préfixe conventionnel, message en français, corps expliquant le *pourquoi* :
`feat(cv): extraire les expériences avec leur extrait source`.

**Langue** — documents, specs, commits et interface : **français**. Identifiants de code, noms
de tables, de champs et d'API : **anglais**. Un terme réglementaire local garde son nom
(`rccm_number`). Les messages destinés à l'utilisateur ne sont jamais écrits en dur dans le code.

**Pull requests** — une spec citée, un périmètre, des tests. Une PR qui « en profite pour »
faire autre chose est scindée.

## 7. Ce qu'on ne fait pas

- Pas de code applicatif sans spec approuvée.
- Pas de migration et de code qui l'utilise dans le même déploiement.
- Pas de donnée de production dans un autre environnement.
- Pas de changement de modèle ou de consigne d'extraction sans passer la barrière d'évaluation.
- Pas de test désactivé pour faire passer une chaîne rouge.
