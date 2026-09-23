---
id: SPEC-016
titre: Observabilité et indicateurs
statut: en revue
version: 0.2
jalon: M1
priorite: P0
exigences: [NFR-08, NFR-09, NFR-10, NFR-12, NFR-17]
depend_de: []
auteur: ""
derniere_maj: 2026-09-23
---

# SPEC-016 — Observabilité et indicateurs

## 1. Objectif

Savoir ce qui se passe en production, **être averti avant les utilisateurs**, et pouvoir mesurer
au pilote ce que le cahier des charges promet de mesurer.

Deux raisons de traiter ce sujet au socle et non après le premier incident :

1. Dans une chaîne asynchrone, **un document bloqué ne lève aucune erreur**. Il ne se passe
   simplement rien, et personne ne le sait avant qu'un recruteur ne s'en plaigne.
2. Le cahier des charges définit quatorze indicateurs sans dire comment les mesurer. **Une donnée
   non collectée en janvier est définitivement perdue** pour l'analyse du pilote.

## 2. Hors périmètre

Tableaux de bord destinés aux utilisateurs (`SPEC-012`) · administration fonctionnelle
(`SPEC-015`).

## 3. Les trois couches

| Couche | Question à laquelle elle répond | Destinataire |
|---|---|---|
| **Santé technique** | Le système fonctionne-t-il ? | Équipe technique, en alerte |
| **Santé produit** | Le parcours aboutit-il ? | Équipe produit, au quotidien |
| **Indicateurs de pilotage** | La promesse commerciale tient-elle ? | Direction, au jalon |

## 4. Règles métier

### Santé technique
- **RG-1** — Le signal principal n'est pas le taux d'erreur mais **la profondeur de la file et
  l'âge du plus vieux travail en attente**. Une alerte est émise au-delà de dix minutes, bien
  avant qu'un utilisateur ne le remarque.
- **RG-2** — Chaque requête et chaque travail asynchrone porte un identifiant de corrélation,
  propagé d'un bout à l'autre de la chaîne, y compris dans les appels aux fournisseurs externes.
- **RG-3** — Toute erreur non rattrapée est enregistrée avec son contexte, **expurgée de toute
  donnée personnelle** : jamais de contenu de CV, de numéro de téléphone ni de nom dans un journal.
- **RG-4** — Les appels aux fournisseurs externes enregistrent leur durée, leur issue **et leur
  coût unitaire**. Sans cela, le coût par CV et le coût par candidat actif ne sont pas calculables.

### Sauvegarde et restauration
- **RG-5** — Les sauvegardes de la base et du stockage des documents sont automatiques et leur
  rétention est explicite.
- **RG-6** — **La restauration est testée périodiquement et chronométrée.** Une sauvegarde jamais
  restaurée n'est pas une sauvegarde. Le résultat de chaque exercice est consigné.
- **RG-7** — La perte de données maximale acceptable et la durée d'interruption acceptable sont
  écrites, connues de l'équipe, et vérifiées par l'exercice de restauration.

### Environnements
- **RG-8** — **Aucune donnée de production n'est copiée dans un autre environnement.** Un CV est
  une donnée personnelle ; copier la base de production en recette, geste banal ailleurs, serait
  une fuite.
- **RG-9** — Un générateur de données synthétiques produit des profils, offres, candidatures et
  tentatives de test crédibles et volumineux, utilisable par toute l'équipe.

### Temps
- **RG-10** — Tous les horodatages sont stockés en temps universel et affichés en heure locale.
  La Guinée étant à l'heure universelle, l'absence de décalage **masquera les défauts** jusqu'à
  la première ouverture d'un autre pays : les échéances de tests sont le point le plus exposé.

### Mesure produit
- **RG-11** — Tout événement nécessaire au calcul d'un indicateur du cahier des charges est émis
  **dès la V1**, sans échantillonnage.
- **RG-12** — Les abandons sont instrumentés au même titre que les réussites. Un tunnel qui ne
  mesure que ceux qui vont au bout ne mesure rien.
- **RG-13** — Le temps réellement passé par un recruteur sur une offre est mesuré : c'est la
  preuve de la promesse commerciale — « du temps de tri économisé » — et il n'existe aucune autre
  façon de l'établir.

## 5. Correspondance indicateurs du cadrage / événements

| Indicateur (cadrage §18) | Événements requis | Spec qui les émet |
|---|---|---|
| Candidats inscrits | `auth.compte_cree` | `SPEC-001` |
| Profils complétés | `profil.complete` | `SPEC-002` |
| CV créés ou importés | `cv.depose`, `cv.valide` | `SPEC-003`, `SPEC-004` |
| Entreprises actives | `offre.publiee`, `recruteur.action` | `SPEC-005`, `SPEC-006` |
| Offres actives | `offre.publiee`, `offre.archivee` | `SPEC-006` |
| Candidatures | `candidature.envoyee` | `SPEC-007` |
| Taux de matching | `matching.distribution` | `SPEC-008` |
| Tests complétés | `test.soumis` | `SPEC-010` |
| Taux de réussite | `test.score` | `SPEC-010` |
| Shortlists produites | `shortlist.transmise` | `SPEC-011` |
| Conversion en entretien | `candidature.statut_change` | `SPEC-007` |
| Conversion en recrutement | `candidature.statut_change` | `SPEC-007` |
| Premium actifs | `abonnement.actif` | `SPEC-017` |
| **Temps économisé côté recruteur** | `recruteur.session_offre` (durée) | `SPEC-011` |

> La dernière ligne est **l'indicateur de valeur business** du cahier des charges. Il est le seul
> qui ne se déduit d'aucun autre : sans instrumentation dédiée dès la V1, la promesse centrale de
> TalVo ne pourra pas être démontrée au pilote.

## 6. Modèle de données

Pas de table métier. Les événements partent vers la collecte ; `audit_logs` reste la trace
métier réglementaire, distincte de la télémétrie. `backup_drills` consigne chaque exercice de
restauration : date, durée, volume, résultat.

## 7. Interfaces

Tableau de bord technique — files, latences, erreurs, coûts externes. Tableau de bord produit —
tunnels et abandons. Canal d'alerte. Aucun écran destiné aux utilisateurs finaux.

## 8. Critères d'acceptation

- **CA-1** — Étant donné un travail en file depuis plus de dix minutes, quand la surveillance
  s'exécute, alors une alerte est émise sur le canal d'astreinte.
- **CA-2** — Étant donné un dépôt de CV, quand on suit son identifiant de corrélation, alors on
  retrouve toute la chaîne : requête, mise en file, traitement, appels externes, résultat.
- **CA-3** — Étant donné une erreur enregistrée, quand on inspecte son contenu, alors elle ne
  contient ni nom, ni numéro de téléphone, ni extrait de CV.
- **CA-4** — Étant donné un appel à un fournisseur externe, quand il s'achève, alors sa durée,
  son issue et son coût sont enregistrés.
- **CA-5** — Étant donné une sauvegarde, quand la procédure de restauration est jouée, alors la
  base est reconstituée, la durée est mesurée et le résultat consigné.
- **CA-6** — Étant donné les quatorze indicateurs du cahier des charges, quand on les calcule,
  alors chacun s'appuie sur des événements réellement émis — vérifié par un test de couverture.
- **CA-7** — Étant donné un candidat qui abandonne à l'étape de vérification du code, quand on
  consulte le tunnel, alors cet abandon est visible et localisé.
- **CA-8** — Étant donné un recruteur consultant une offre, quand il la quitte, alors le temps
  passé est enregistré.
- **CA-9** — Étant donné un environnement de recette, quand on inspecte sa base, alors elle ne
  contient aucune donnée issue de la production.
- **CA-10** — Étant donné une date enregistrée, quand elle est lue depuis un autre fuseau, alors
  elle désigne le même instant.

## 9. Cas limites

Fournisseur externe lent qui ne renvoie ni succès ni erreur · travail qui échoue en boucle et
sature la file · pic de candidatures qui fait croître la file sans qu'il y ait de défaut ·
restauration échouant partiellement · horloge d'un serveur désynchronisée.

## 10. Exigences non fonctionnelles

`NFR-08` sauvegardes restaurées · `NFR-09` surveillance de la file · `NFR-10` événements émis
dès la V1 · `NFR-12` temps universel · `NFR-17` cloisonnement des environnements.

## 11. Indicateurs sur l'équipe

Quatre mesures, gratuites à collecter dès le premier jour, qui disent si le pipeline sert
l'équipe ou la freine : délai entre un commit et sa mise en production · fréquence de
déploiement · part des déploiements provoquant un incident · temps de rétablissement.

## 12. Questions ouvertes

| # | Question | Bloquante | Responsable | Échéance |
|---|---|---|---|---|
| 1 | Quelle perte de données maximale et quelle durée d'interruption acceptables ? | **Oui** | Direction | M1 |
| 2 | À quelle fréquence l'exercice de restauration est-il joué ? | Non | CTO | M1 |
| 3 | Qui reçoit les alertes en dehors des heures ouvrées pendant le pilote ? | **Oui** | Opérations | M5 |
| 4 | Durée de conservation des journaux et de la télémétrie | Non | Juridique | M5 |

## 13. Historique

| Version | Date | Changement |
|---|---|---|
| 0.1 | 2026-09-23 | Création |
| 0.2 | 2026-09-23 | Rédaction complète, dont la correspondance indicateurs / événements |
