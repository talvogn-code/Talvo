---
id: SPEC-013
titre: Référentiels métier
statut: en revue
version: 0.2
jalon: M1
priorite: P0
exigences: [EXI-MCH-10, EXI-ADM-03, NFR-11]
depend_de: []
auteur: ""
derniere_maj: 2026-09-23
---

# SPEC-013 — Référentiels métier

## 1. Objectif

Constituer et maintenir le dictionnaire qui rend le classement **reproductible et explicable** :
compétences, fonctions, diplômes et secteurs, avec leurs alias et leurs équivalences locales.

Sans normalisation, « Power BI », « PowerBI » et « MS Power BI » sont trois compétences
différentes : deux candidats identiques obtiennent deux scores différents, et le classement
devient impossible à justifier — donc invendable.

C'est aussi **l'actif différenciant de TalVo**. L'OCR s'achète au prix du marché et ne distingue
de personne. Aucune taxonomie internationale ne couvre correctement le marché ouest-africain :
ni l'expérience en économie informelle, ni les établissements locaux, ni le tissu d'employeurs
guinéen.

## 2. Hors périmètre

Le moteur de classement lui-même (`SPEC-008`) · l'extraction qui consomme le référentiel
(`SPEC-003`) · la bibliothèque de formulations de CV (`SPEC-004`).

## 3. Les quatre référentiels

| Référentiel | Contenu | Consommé par |
|---|---|---|
| **Compétences** | Libellé, identifiant stable, catégorie, alias, compétences voisines | Extraction, offres, classement, tests |
| **Fonctions métier** | Intitulé, famille métier, alias | Extraction, offres, classement |
| **Diplômes et niveaux** | Libellé local, niveau normalisé, domaine, pays | Extraction, offres, classement |
| **Secteurs** | Libellé, identifiant, pays | Profils d'entreprise, offres, classement |

## 4. Acteurs et déclencheurs

Un administrateur TalVo crée, modifie, fusionne ou retire une entrée. L'extraction et le
classement consomment le référentiel en lecture seule. Le moteur de rappel sémantique **propose**
des alias, qu'un humain valide ou refuse.

## 5. Règles métier

### Structure
- **RG-1** — Chaque entrée porte un identifiant stable, indépendant de son libellé. Renommer une
  compétence ne casse aucune donnée existante.
- **RG-2** — Chaque entrée porte un ou plusieurs alias. La correspondance ignore la casse, les
  accents, la ponctuation et les espaces multiples.
- **RG-3** — Une entrée applicable à un seul pays porte son code pays. Une entrée sans code pays
  est universelle. Le référentiel est structuré par pays **dès l'origine**, même avec un seul pays
  ouvert — rétro-ajouter cette dimension est l'une des migrations les plus douloureuses.
- **RG-4** — Les diplômes locaux sont ramenés à une **échelle de niveaux comparables**, de sorte
  qu'un BTS guinéen et un diplôme équivalent d'un autre pays produisent le même niveau.

### Alimentation
- **RG-5** — Une correspondance proposée par la similarité sémantique n'entre au référentiel
  **qu'après validation humaine**. L'IA nourrit le référentiel explicable, elle ne le contourne pas.
- **RG-6** — Un terme rencontré à l'extraction et absent du référentiel est journalisé comme
  candidat, avec son occurrence. Les candidats les plus fréquents remontent en tête de la file de
  curation.
- **RG-7** — Un terme non résolu **n'est jamais inventé ni deviné** : il est conservé tel quel sur
  le profil, sans identifiant, et ne pèse pas dans le classement.

### Intégrité
- **RG-8** — Toute modification est versionnée et journalisée avec son auteur, sa date et
  l'ancienne valeur. **Modifier le référentiel change les scores** : c'est un acte tracé.
- **RG-9** — Fusionner deux entrées conserve les deux identifiants ; l'entrée absorbée devient un
  alias de l'entrée conservée. Aucun identifiant n'est jamais supprimé.
- **RG-10** — Retirer une entrée la marque comme obsolète sans la supprimer : les profils et
  offres qui la référencent restent lisibles.
- **RG-11** — Une modification structurante — fusion, changement de niveau d'un diplôme —
  déclenche un recalcul des scores concernés, avec une nouvelle version d'algorithme.

### Qualité
- **RG-12** — Le taux de résolution — part des termes rencontrés qui trouvent une entrée — est
  mesuré en continu. C'est l'indicateur de santé du référentiel.
- **RG-13** — Une compétence sans alias et jamais rencontrée depuis six mois est signalée pour
  revue : le référentiel se nettoie autant qu'il s'enrichit.

## 6. Modèle de données

`skills` (`id`, `slug`, `name`, `category`, `aliases[]`, `country_code`, `status`) ·
`job_functions` (`id`, `slug`, `name`, `family`, `aliases[]`, `country_code`) ·
`degrees` (`id`, `name`, `level`, `field`, `country_code`, `aliases[]`) ·
`sectors` (`id`, `slug`, `name`, `country_code`) ·
`referential_versions` · `referential_changes` (auteur, entrée, avant, après, date) ·
`unresolved_terms` (terme, type présumé, occurrences, dernière rencontre, statut).

## 7. Interfaces

Écran d'administration des référentiels — extension de l'écran 23 du cahier des charges, avec une
**file de curation** des termes non résolus et des alias proposés. Événement
`referential.changed` qui déclenche les recalculs.

## 8. Critères d'acceptation

- **CA-1** — Étant donné les graphies « Power BI », « PowerBI » et « MS Power BI », quand elles
  sont normalisées, alors elles produisent le même identifiant de compétence.
- **CA-2** — Étant donné la graphie « EXPÉRIENCE » et « experience », quand elles sont
  normalisées, alors la casse et les accents sont ignorés.
- **CA-3** — Étant donné une compétence renommée, quand on consulte un profil qui la référence,
  alors le profil reste correct et affiche le nouveau libellé.
- **CA-4** — Étant donné deux compétences fusionnées, quand on interroge l'identifiant de
  l'entrée absorbée, alors il résout vers l'entrée conservée.
- **CA-5** — Étant donné un terme absent du référentiel rencontré à l'extraction, quand le
  traitement s'achève, alors le terme est conservé tel quel sur le profil, enregistré comme
  candidat, et ne pèse pas dans le classement.
- **CA-6** — Étant donné un alias proposé par la similarité sémantique, quand il n'a pas été
  validé, alors il n'influence aucun score.
- **CA-7** — Étant donné une modification du référentiel, quand elle est enregistrée, alors
  l'auteur, la date et l'ancienne valeur sont conservés et consultables.
- **CA-8** — Étant donné un diplôme guinéen et son équivalent d'un autre pays, quand ils sont
  normalisés, alors ils produisent le même niveau.
- **CA-9** — Étant donné un changement de niveau d'un diplôme, quand il est appliqué, alors les
  scores concernés sont recalculés sous une nouvelle version d'algorithme, sans écraser les
  anciens.
- **CA-10** — Étant donné une entrée marquée obsolète, quand un profil qui la référence est
  affiché, alors il reste lisible et l'entrée n'est proposée à aucune nouvelle saisie.

## 9. Cas limites

Compétence dont le libellé est aussi l'alias d'une autre · alias identique proposé pour deux
entrées distinctes · diplôme dont le nom a changé au fil des réformes · secteur d'activité d'une
entreprise qui en couvre plusieurs · terme en anglais désignant une compétence enregistrée en
français · faute de frappe fréquente qu'il faut décider d'accepter comme alias ou non.

## 10. Exigences non fonctionnelles

`NFR-11` structure multi-pays. La résolution d'un terme est une opération en mémoire : le
référentiel entier tient en cache et se recharge à chaque changement de version.

## 11. Télémétrie

`referential.resolution` (terme, résolu ou non, type), `referential.terme_inconnu` (terme,
occurrences), `referential.modification` (entrée, nature, auteur), `referential.alias_propose`,
`referential.alias_valide` ou `refuse`.

> Le **taux de résolution** est l'indicateur de santé du produit le plus sous-estimé : il baisse
> silencieusement quand le marché évolue, et le classement se dégrade avec lui sans qu'aucune
> erreur ne soit levée.

## 12. Questions ouvertes

| # | Question | Bloquante | Responsable | Échéance |
|---|---|---|---|---|
| 1 | Qui est propriétaire du référentiel et le maintient dans la durée ? | **Oui** | Direction | M1 |
| 2 | Partons-nous d'une base existante à adapter, ou de zéro ? | **Oui** | CTO | M1 |
| 3 | Quel taux de résolution minimal acceptable avant d'ouvrir au public ? | Non | CTO | M4 |
| 4 | Le référentiel est-il un jour exposé publiquement, comme actif de marque ? | Non | Direction | Post-MVP |

## 13. Historique

| Version | Date | Changement |
|---|---|---|
| 0.1 | 2026-09-23 | Création |
| 0.2 | 2026-09-23 | Rédaction complète : alias, curation, versionnement, recalculs |
