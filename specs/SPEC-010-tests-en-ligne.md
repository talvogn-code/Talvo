---
id: SPEC-010
titre: Tests en ligne
statut: en revue
version: 0.2
jalon: M4
priorite: P0
exigences: [EXI-OFF-08, EXI-TST-01, EXI-TST-02, EXI-TST-03, EXI-TST-04, EXI-TST-05, EXI-TST-06, EXI-TST-07, EXI-TST-09, EXI-TST-10, EXI-TST-11, EXI-TST-12]
depend_de: [SPEC-001, SPEC-006, SPEC-014]
auteur: ""
derniere_maj: 2026-09-23
---

# SPEC-010 — Tests en ligne

## 1. Objectif

Permettre de **vérifier une compétence** au lieu de la croire sur parole, dans des conditions
réseau dégradées, et produire un score sur lequel une entreprise peut fonder une décision.

C'est la brique qui distingue « recevoir des CV » de « recevoir des talents évalués ».
Si les scores sont contournables, la proposition commerciale s'effondre.

## 2. Hors périmètre

Rédaction des questions (travail éditorial) · intégration des scores à la shortlist
(`SPEC-011`) · surveillance par caméra, explicitement écartée du MVP.

## 3. Parcours nominal

1. L'entreprise coche « tests requis » sur son offre et sélectionne un ou plusieurs tests.
2. À la réception d'une candidature, TalVo crée une invitation et notifie le candidat.
3. Le candidat ouvre le test. Le serveur enregistre l'heure de début et retourne les questions
   tirées pour cette tentative.
4. Le candidat répond. **Chaque réponse est envoyée et confirmée dès la validation.**
5. À la soumission ou à l'échéance, le serveur calcule le score.
6. Le résultat est rattaché à la candidature et devient visible par l'entreprise.

## 4. Règles métier

### Autorité du serveur
- **RG-1** — L'heure de début, l'échéance et l'expiration sont **calculées et vérifiées côté
  serveur**. Le temps affiché au candidat est indicatif.
- **RG-2** — Une réponse reçue après l'échéance serveur est refusée, quelle que soit l'heure
  déclarée par le client.
- **RG-3** — La bonne réponse d'une question n'est **jamais** transmise au client pendant une
  tentative en cours.

### Résistance au réseau
- **RG-4** — Chaque réponse est enregistrée individuellement dès sa validation et confirmée.
  Une réponse non confirmée est retentée par le client.
- **RG-5** — Après une coupure, la reprise restitue la tentative exactement là où elle s'est
  arrêtée : mêmes questions, même ordre, réponses déjà données conservées, temps restant recalculé
  par le serveur.
- **RG-6** — Une tentative interrompue n'est jamais perdue. Elle est soit reprise, soit expirée
  avec les réponses déjà fournies.

### Intégrité de l'évaluation
- **RG-7** — Les questions servies sont tirées aléatoirement dans une banque au moins **cinq fois
  plus grande** que le nombre servi. Un test dont la banque n'atteint pas ce ratio ne peut pas
  être publié.
- **RG-8** — L'ordre des questions et celui des options sont aléatoires par tentative.
- **RG-9** — Un candidat ne rejoue pas le même test pour la même offre.
- **RG-10** — Les changements d'onglet et les collages sont comptabilisés et joints au résultat
  **à titre indicatif**. Ils ne modifient jamais le score automatiquement.
- **RG-11** — Un résultat n'existe que s'il existe une tentative au statut `soumise`. Un candidat
  invité mais n'ayant pas passé le test apparaît comme `invité` ou `expiré`, **jamais comme échoué**.

### Deux natures de tests
- **RG-12** — Un test demandé par une entreprise et un test de certification volontaire sont
  distingués par l'origine de la tentative et ne sont jamais présentés de la même façon.
- **RG-13** — Un score de certification volontaire est conservé au profil et peut donner un badge
  affichable, à la discrétion du candidat.

### Arbitrage
- **RG-14** — Une tentative est intégralement rejouable par un administrateur : questions servies,
  réponses données, horodatages. Une contestation se tranche sur pièces.

## 5. Modèle de données

`tests`, `questions`, `question_options`, `job_tests`, `test_attempts` (avec `origin`,
`invited_at`, `expires_at`, `started_at`, `submitted_at`, `status`), `attempt_questions`
(les questions effectivement tirées, dans leur ordre), `attempt_answers`, `test_results`,
`skill_badges`.

## 6. Interfaces

Écrans 08 (tests et résultats candidat), 19 (configuration des tests), 20 (résultats côté
entreprise), 22 (gestion des tests, administration). Travaux asynchrones
`tests.invite`, `tests.remind`, `tests.expire`, `tests.score`.

## 7. Critères d'acceptation

- **CA-1** — Étant donné une offre avec tests requis, quand un candidat postule, alors une
  invitation est créée et une notification envoyée.
- **CA-2** — Étant donné une tentative en cours, quand le client avance son horloge d'une heure,
  alors le serveur refuse les réponses postérieures à l'échéance réelle.
- **CA-3** — Étant donné une tentative en cours, quand la connexion est coupée puis rétablie,
  alors le candidat retrouve ses réponses et le temps restant calculé par le serveur.
- **CA-4** — Étant donné une réponse validée, quand le réseau échoue avant confirmation, alors le
  client réessaie et aucune réponse n'est perdue ni dupliquée.
- **CA-5** — Étant donné une tentative en cours, quand on inspecte les données reçues par le
  navigateur, alors elles ne contiennent aucune indication de bonne réponse.
- **CA-6** — Étant donné deux candidats passant le même test, quand on compare leurs tentatives,
  alors les questions servies et leur ordre diffèrent.
- **CA-7** — Étant donné un test dont la banque compte moins de cinq fois le nombre de questions
  servies, quand on tente de le publier, alors la publication est refusée.
- **CA-8** — Étant donné un candidat invité n'ayant pas passé le test, quand l'entreprise consulte
  les résultats, alors son statut est `invité` ou `expiré`, et aucun score ne lui est attribué.
- **CA-9** — Étant donné une tentative expirée avec des réponses partielles, quand le score est
  calculé, alors il porte sur les réponses fournies et la tentative est marquée expirée.
- **CA-10** — Étant donné une tentative soumise, quand un administrateur l'ouvre, alors il voit
  les questions servies, les réponses données et les horodatages.
- **CA-11** — Étant donné un test de certification volontaire, quand une entreprise consulte la
  fiche du candidat, alors le résultat est identifié comme une certification et non comme un test
  qu'elle aurait demandé.

## 8. Cas limites

Candidat fermant son navigateur en plein test · deux onglets ouverts sur la même tentative ·
invitation reçue après l'échéance de l'offre · entreprise modifiant les tests d'une offre déjà
publiée · test retiré du catalogue alors que des tentatives sont en cours · candidat sans réseau
pendant toute la durée impartie.

## 9. Exigences non fonctionnelles

Une réponse est confirmée en moins de 800 ms sur un réseau 3G. Le poids d'une page de test reste
compatible avec une connexion lente. Aucune tentative perdue — une tentative perdue est un
incident, pas une statistique.

## 10. Télémétrie

`test.invite`, `test.ouvert`, `test.question_repondue`, `test.reprise_apres_coupure`,
`test.soumis`, `test.expire`, `test.score`, `test.anomalie` (changement d'onglet, collage).
Alimentent : taux de complétion, abandon par question, part de reprises réseau, et la corrélation
score / retour d'entretien mesurée au jalon M6.

## 11. Questions ouvertes

| # | Question | Bloquante | Responsable | Échéance |
|---|---|---|---|---|
| 1 | Délai par défaut accordé pour passer un test | **Oui** | Produit | M4 |
| 2 | Seuil de réussite par test, et qui le fixe | **Oui** | Produit | M4 |
| 3 | Canal d'invitation : SMS, e-mail ou les deux — `ADR-007` | **Oui** | Direction | M4 |
| 4 | Durée de validité d'un badge de compétence avant re-test | Non | Produit | M7 |
| 5 | Que faire d'une anomalie répétée sur un même candidat ? | Non | Produit | M6 |

## 12. Historique

| Version | Date | Changement |
|---|---|---|
| 0.1 | 2026-09-23 | Création |
| 0.2 | 2026-09-23 | Ajout de l'autorité serveur, de la reprise réseau et du ratio de banque |
