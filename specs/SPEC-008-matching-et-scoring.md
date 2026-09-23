---
id: SPEC-008
titre: Matching et scoring
statut: en revue
version: 0.2
jalon: M4
priorite: P0
exigences: [EXI-MCH-01, EXI-MCH-02, EXI-MCH-03, EXI-MCH-04, EXI-MCH-05, EXI-MCH-06, EXI-MCH-07, NFR-16]
depend_de: [SPEC-003, SPEC-006, SPEC-013]
auteur: ""
derniere_maj: 2026-09-23
---

# SPEC-008 — Matching et scoring

## 1. Objectif

Classer les profils face à une offre, et **pouvoir expliquer chaque position**. Un recruteur doit
obtenir, pour n'importe quel candidat, la réponse à « pourquoi celui-ci est-il troisième ? » en
une phrase compréhensible.

## 2. Hors périmètre

Sourcing des profils n'ayant pas postulé (`SPEC-009`) · shortlist (`SPEC-011`) ·
recommandation d'offres aux candidats Premium (`SPEC-017`).

## 3. Déclencheurs de calcul

Publication ou modification d'une offre · nouvelle candidature · validation d'un profil après
correction · résultat de test enregistré · recalcul en lot déclenché par un administrateur.

## 4. Le score

```
total = 0,35 × compétences
      + 0,30 × expérience
      + 0,15 × fonction
      + 0,10 × formation
      + 0,10 × localisation
```

Chaque sous-score est ramené à l'intervalle 0–100. Les poids sont **stockés en configuration**,
jamais écrits dans le code.

## 5. Règles métier

### Calcul
- **RG-1** — Compétences : somme pondérée des compétences requises trouvées sur la somme des
  requises. Une compétence `requise` pèse 1,0 ; `souhaitée` pèse 0,4.
- **RG-2** — La correspondance d'une compétence passe par le référentiel et ses alias, jamais par
  une comparaison de chaînes brute.
- **RG-3** — Si l'offre exige un nombre d'années sur une compétence et que le candidat en a moins,
  la compétence ne compte que pour moitié.
- **RG-4** — Expérience : moitié volume (années totales rapportées à l'exigence de l'offre,
  plafonnée à 100), moitié pertinence (part des années sur une fonction ou un secteur proche).
- **RG-5** — Fonction : 100 si identique, 60 si même famille métier, sinon similarité textuelle
  ramenée à l'intervalle 0–60.
- **RG-6** — Formation : 100 si le niveau atteint l'exigence, 50 si un cran en dessous, 0 au-delà.
  100 si l'offre n'exige rien.
- **RG-7** — Localisation : 100 même ville, 80 même région ou mobilité déclarée, 60 offre à
  distance, 20 sinon.

### Tests
- **RG-8** — Les scores de tests **n'entrent pas** dans le total. Ils constituent un filtre et un
  second axe de tri, appliqués après le calcul (`SPEC-010`, `SPEC-011`).

### Explicabilité
- **RG-9** — Tout score enregistré s'accompagne d'un détail structuré contenant, au minimum : la
  version d'algorithme, les poids appliqués, et par critère le sous-score et les éléments qui l'ont
  produit — compétences trouvées, manquantes, partielles ; années retenues ; règle de localisation.
- **RG-10** — Aucun score n'est affiché sans son explication en langage naturel.
- **RG-11** — L'interface présente le score comme une aide à la décision. Aucun rejet automatique,
  aucune formulation suggérant une décision d'embauche.

### Intégrité
- **RG-12** — Le calcul est **déterministe** : mêmes entrées et même version produisent le même
  score, au centième près.
- **RG-13** — Toute modification des poids incrémente la version d'algorithme et est journalisée.
  Les scores existants ne sont jamais écrasés : une nouvelle version crée de nouvelles lignes.
- **RG-14** — Le moteur est un **module pur** : entrées profil et offre, sortie score et détail.
  Aucune dépendance au framework HTTP ni à la couche de persistance.
- **RG-15** — Aucun attribut discriminatoire — âge, genre, origine, situation familiale, photo —
  n'est accessible au moteur. Ces champs ne figurent pas dans sa structure d'entrée.
- **RG-16** — La similarité sémantique est autorisée pour **élargir** l'ensemble des candidats
  examinés, jamais pour produire le score affiché. Une correspondance sémantique jugée pertinente
  est proposée comme alias au référentiel et validée par un humain avant de peser sur un score.

## 6. Modèle de données

`match_scores` (`job_id`, `candidate_id`, `total_score`, cinq sous-scores, `breakdown` jsonb,
`algorithm_version`, `computed_at`, unicité sur le triplet offre / candidat / version) ·
`matching_weights` (version, poids, auteur, date d'activation).

## 7. Interfaces

Écrans 15 (candidatures), 17 (shortlist), 18 (fiche candidat). Travail asynchrone
`matching.score_job` et `matching.score_candidate`. Événement `matching.scored`.

## 8. Critères d'acceptation

- **CA-1** — Étant donné un profil et une offre fixés, quand le score est calculé deux fois,
  alors les deux résultats sont identiques.
- **CA-2** — Étant donné un candidat possédant « PowerBI » et une offre demandant « Power BI »,
  quand le score est calculé, alors la compétence est reconnue comme trouvée.
- **CA-3** — Étant donné une offre exigeant trois compétences dont deux sont trouvées, quand le
  détail est produit, alors il nomme les deux trouvées **et** la manquante.
- **CA-4** — Étant donné un score affiché au recruteur, quand il ouvre la fiche, alors il lit une
  explication en français mentionnant compétences, expérience et localisation.
- **CA-5** — Étant donné un changement de poids, quand il est activé, alors la version
  d'algorithme change, l'action est journalisée, et les scores antérieurs restent consultables.
- **CA-6** — Étant donné la structure d'entrée du moteur, quand elle est inspectée, alors elle ne
  contient ni date de naissance, ni genre, ni photographie, ni situation familiale.
- **CA-7** — Étant donné un candidat sans expérience et une offre n'exigeant aucune expérience,
  quand le score est calculé, alors le sous-score d'expérience vaut 100 et non 0.
- **CA-8** — Étant donné une offre publiée, quand 500 candidatures arrivent en une heure, alors
  tous les scores sont calculés sans dégrader le temps de réponse des pages.
- **CA-9** — Étant donné un jeu de référence de couples profil / offre, quand l'algorithme est
  modifié, alors l'écart de classement est mesuré et présenté dans la pull request.

## 9. Cas limites

Offre sans compétence renseignée · candidat sans CV validé · profil dont toutes les compétences
sont hors référentiel · deux candidats à score identique — l'ordre doit rester stable ·
offre modifiée pendant un calcul en cours · candidat supprimant son compte.

## 10. Exigences non fonctionnelles

`NFR-16` versionnement et journalisation des poids. Le calcul d'une offre de 500 candidatures
s'effectue en moins de cinq minutes.

## 11. Télémétrie

`matching.calcul` (offre, nombre de profils, durée, version), `matching.distribution`
(histogramme des scores par offre), `matching.affiche` (score consulté par un recruteur),
`matching.decision` (action prise après consultation).

> Le couple `matching.affiche` / `matching.decision` est la seule façon de mesurer si le
> classement aide réellement — c'est-à-dire si les recruteurs retiennent les profils bien classés.

## 12. Questions ouvertes

| # | Question | Bloquante | Responsable | Échéance |
|---|---|---|---|---|
| 1 | Répartition interne des 35 % entre compétences requises et souhaitées | Non *(valeurs par défaut posées)* | Produit | M4 |
| 2 | Seuil minimal d'affichage d'un profil au recruteur | **Oui** | Produit | M4 |
| 3 | Fréquence de l'audit de distribution des scores par profil | Non | CTO | M6 |

## 13. Historique

| Version | Date | Changement |
|---|---|---|
| 0.1 | 2026-09-23 | Création à partir de `docs/02-moteur-matching.md` |
| 0.2 | 2026-09-23 | Séparation explicite du rappel sémantique et du classement |
