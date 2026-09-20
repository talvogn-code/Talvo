# TalVo — Cadrage MVP 2027

> Restitution structurée du document de cadrage fourni (`TalVo_MVP.pdf`, version de travail).
> Ce fichier est la **source de vérité fonctionnelle** du dépôt. Toute évolution du périmètre
> se fait par modification de ce document, en PR.

## 1. Résumé exécutif

TalVo est une plateforme guinéenne de recrutement qui ne se limite pas à publier des offres.
Le MVP repose sur un modèle de **mise en relation, sourcing, présélection et évaluation**.

Objectifs :
- réduire le temps consacré par les entreprises au tri des CV ;
- améliorer la pertinence des opportunités proposées aux candidats.

Principe central : une entreprise décrit son besoin → TalVo analyse les profils disponibles →
classe les candidats selon compétences et expériences → organise si nécessaire des tests en
ligne → présente au recruteur une sélection de profils pertinents.

**Positionnement** : faire passer l'entreprise de « recevoir des CV » à « recevoir une sélection
de talents évalués », et le candidat de « chercher des annonces » à « accéder à des opportunités
pertinentes et mieux valoriser son profil ».

**Signature** : *Trouver les bons talents. Trouver les bonnes opportunités.*

## 2. Proposition de valeur par cible

| Cible | Proposition de valeur |
|---|---|
| Candidat gratuit | Créer son profil, importer/créer son CV, rechercher et candidater aux offres |
| Candidat Premium | Recevoir des offres adaptées, connaître l'entreprise, adapter son CV à une offre, contacter la RH |
| Entreprise | Publier des offres, accéder aux candidatures, identifier des profils pertinents, demander des tests |
| Cabinet de recrutement | Sourcer, filtrer et présélectionner des talents pour ses clients |
| TalVo | Monétiser les services professionnels de sourcing, présélection et évaluation |

## 3. Modèle fonctionnel — 8 modules prioritaires

| # | Module | Fonction | Priorité |
|---|---|---|---|
| 1 | Comptes & accès | Candidat, Premium, Entreprise, Cabinet, Administrateur | P0 |
| 2 | Profils | Profils candidats et professionnels | P0 |
| 3 | CV | Importer, créer, exporter, adapter | P0 |
| 4 | Offres | Créer, publier, rechercher, candidater | P0 |
| 5 | Matching & sourcing | Identifier et classer les profils pertinents | P0 |
| 6 | Tests | Tests demandés par entreprises + tests de compétences | P0 |
| 7 | Présélection | Scoring, shortlist et transmission au client | P0 |
| 8 | Dashboards | Pilotage candidat, entreprise, cabinet et admin | P0 |

## 4. Roadmap 2027 — priorisation des fonctionnalités

| Fonctionnalité | Priorité | Jalon visé |
|---|---|---|
| Création de compte / connexion | P0 | V1 — Jan. 2027 |
| Profil candidat | P0 | V1 — Jan. 2027 |
| Import CV PDF/DOCX | P0 | V1 — Jan. 2027 |
| Création de CV TalVo | P0 | V1 — Jan. 2027 |
| Export CV PDF | P0 | V1 — Jan. 2027 |
| Profil entreprise / cabinet | P0 | V1 — Jan. 2027 |
| Publication d'offres | P0 | V1 — Jan. 2027 |
| Recherche / filtres d'offres | P0 | V1 — Jan. 2027 |
| Candidature en ligne | P0 | V1 — Jan. 2027 |
| Tri automatique des CV | P0 | V1 — Jan. 2027 |
| Matching profil ↔ offre | P0 | V1 — Jan. 2027 |
| Shortlist TalVo | P0 | V1 — Jan. 2027 |
| Tests techniques / logiques | P0 | V1 — Jan. 2027 |
| Dashboard entreprise | P0 | V1 — Jan. 2027 |
| Tests de compétences candidats | P1 | Fév. 2027 |
| Scores / badges de compétences | P1 | Fév. 2027 |
| Mini-ATS / pipeline | P1 | Mars 2027 |
| Messagerie candidat ↔ recruteur | P1 | Mars 2027 |
| Sourcing de talents n'ayant pas postulé | P1 | Mars 2027 |
| Candidat Premium | P1 | Mars 2027 |
| CV adapté à chaque offre | P1 | Avr.–Juin 2027 |
| Offres recommandées Premium | P1 | Avr.–Juin 2027 |
| Nom de l'entreprise pour Premium | P1 | Mars 2027 |
| Paiement / abonnements | P1 | Avr.–Juin 2027 |
| Tests avancés / catalogue élargi | P2 | Post-MVP |
| Application mobile native | P2 | Post-MVP |
| Vérification des diplômes | P2 | Post-MVP |

Niveaux : **P0** indispensable (doit être dans la V1) · **P1** après validation du pilote ·
**P2** plus tard (non nécessaire au démarrage).

## 5. Planning de livraison

| Période | Objectif | Livrables |
|---|---|---|
| Sept. 2026 | Cadrage | Validation du périmètre MVP, règles métier, architecture, backlog |
| Oct. 2026 | UX/UI | Maquettes, design system, parcours candidat et entreprise |
| Nov. 2026 | Développement socle | Auth, profils, BDD, stockage CV, administration de base |
| Déc. 2026 | Recrutement | Offres, candidatures, moteur de tri, tests, dashboard entreprise |
| Jan. 2027 | V1 pilote | Mise en production pilote : tri CV + offres + tests + shortlist |
| Fév. 2027 | Stabilisation | Corrections, scores/badges, amélioration matching, UX |
| Mars 2027 | V1.5 | Premium, messagerie, sourcing de talents |
| Avr.–Juin 2027 | V2 | CV adapté, recommandations, paiement, tests avancés |

## 6. Contenu de la V1 (janvier 2027)

La V1 doit être **réellement utilisable avec quelques entreprises pilotes**. Elle ne cherche pas
à couvrir toutes les ambitions de TalVo : elle démontre rapidement la valeur du **tri des CV**
et des **tests**.

### 6.1 Parcours candidat V1
1. Créer un compte candidat.
2. Compléter un profil simple.
3. Importer un CV ou renseigner son expérience dans TalVo.
4. Consulter les offres disponibles.
5. Postuler à une offre.
6. Recevoir une invitation à un test lorsque l'entreprise l'a demandé.
7. Passer le test en ligne.
8. Consulter le statut de sa candidature.

### 6.2 Parcours entreprise V1
1. Créer et faire valider un compte professionnel.
2. Créer une offre avec critères de recrutement.
3. Choisir si un test est requis.
4. Sélectionner un ou plusieurs tests.
5. Recevoir les candidatures.
6. Visualiser le classement des profils réalisé par TalVo.
7. Consulter les résultats des tests.
8. Recevoir une shortlist de candidats pertinents.
9. Décider des candidats à contacter ou à faire passer en entretien.

## 7. Gestion des comptes

### 7.1 Candidat gratuit
- Création de compte et connexion.
- Création et modification du profil professionnel.
- Import d'un CV PDF/Word.
- Création d'un CV directement dans TalVo.
- Export du CV créé en PDF.
- Recherche et consultation des offres.
- Candidature aux offres.
- Suivi des candidatures.
- Accès aux tests de compétences proposés par TalVo selon les règles du service.

### 7.2 Candidat Premium
- Toutes les fonctions du compte gratuit.
- Recommandation d'offres correspondant au profil.
- Affichage du nom et des informations disponibles sur l'entreprise.
- Possibilité de contacter la RH/recruteur via TalVo pour une offre.
- Adaptation du CV à chaque offre grâce à une fonction d'assistance.
- Accès élargi aux tests et fonctionnalités de valorisation du profil.

### 7.3 Entreprise / Cabinet de recrutement
- Création du compte professionnel + profil organisation.
- Publication et gestion des offres.
- Accès aux candidats ayant postulé.
- Accès aux profils pertinents identifiés par TalVo **même s'ils n'ont pas postulé**.
- Consultation du scoring et des éléments de correspondance.
- Demande de tests techniques/logiques.
- Accès à une shortlist préparée par TalVo.
- Messagerie avec les candidats dans le cadre d'un recrutement.

## 8. Gestion des CV

### 8.1 Importer un CV
- Formats prioritaires : **PDF** et **DOCX**.
- Extraction des informations principales.
- Préremplissage du profil candidat.
- Possibilité de corriger manuellement les données.

### 8.2 Créer un CV
Informations personnelles · titre et résumé professionnel · expériences · formations ·
compétences · langues · certifications · choix d'un modèle · prévisualisation · export PDF.

### 8.3 CV adapté à une offre (Premium)
- Analyse de l'offre et du CV.
- Identification des compétences et expériences pertinentes **déjà présentes**.
- Réorganisation et reformulation du contenu existant.
- Mise en avant des expériences pertinentes.
- Signalement des éléments manquants.
- **Interdiction d'inventer** une compétence, un diplôme ou une expérience.
- Prévisualisation et export du CV adapté.

## 9. Gestion des offres d'emploi

Création d'une offre : titre, description, secteur, localisation, type de contrat, expérience,
compétences, date limite. Option « Tests requis » + sélection des tests. Publication,
modification, mise en pause, archivage. Page publique de l'offre.

### 9.1 Visibilité de l'entreprise

| Utilisateur | Information affichée |
|---|---|
| Candidat gratuit | Secteur d'activité de l'entreprise uniquement |
| Candidat Premium | Nom de l'entreprise + informations disponibles |
| Entreprise / Cabinet | Informations complètes nécessaires au recrutement |

## 10. Matching, sourcing et présélection

### 10.1 Critères de correspondance

| Critère | Exemple |
|---|---|
| Compétences | Power BI, SQL, Excel, React |
| Expérience | Nombre d'années et pertinence des expériences |
| Fonction | Data Analyst, Comptable, Ingénieur… |
| Secteur | Banque, Mines, Télécoms, ONG… |
| Formation | Diplôme ou domaine pertinent |
| Localisation | Ville, région, mobilité |
| Type de contrat | CDI, CDD, Stage, Mission |
| Tests | Scores des tests demandés par l'entreprise |

### 10.2 Pondération V1 (moteur explicable, à base de règles)

| Critère | Poids indicatif V1 | Exemple |
|---|---|---|
| Compétences recherchées | 35 % | SQL, Excel, Power BI |
| Expériences pertinentes | 30 % | Expérience Data Analyst |
| Intitulé / fonction | 15 % | Correspondance du métier |
| Formation | 10 % | Data, informatique, finance… |
| Localisation / mobilité | 10 % | Conakry, mobilité |

> **Contrainte forte V1** : le moteur de tri doit rester **explicable et maîtrisable**. TalVo doit
> pouvoir comprendre *pourquoi* un profil est classé. L'IA enrichira le moteur plus tard.

### 10.3 Deux catégories de profils
- Candidats ayant **postulé** à l'offre.
- **Talents sourcés** : identifiés par TalVo comme correspondant au besoin mais n'ayant pas postulé.

### 10.4 Workflow de présélection
1. Réception des candidatures.
2. Analyse automatique des profils.
3. Calcul d'un score de correspondance.
4. Classement des profils.
5. Identification de profils externes pertinents dans le vivier TalVo.
6. Application des critères de tests lorsqu'ils sont requis.
7. Préparation d'une shortlist.
8. Transmission au recruteur.

## 11. Tests en ligne

### 11.1 Tests demandés par l'entreprise
L'entreprise coche « Tests requis » à la création de l'offre → sélectionne un ou plusieurs tests →
TalVo invite les candidats concernés → les candidats passent les tests en ligne dans un délai
défini → TalVo calcule les scores → les résultats sont intégrés à la présélection → les meilleurs
profils sont présentés au client.

### 11.2 Catalogue initial de tests
Excel · SQL · Power BI · Agile/Scrum · PHP · React · Logique · Français · Anglais
(+ autres tests ajoutés progressivement).

### 11.3 Tests de certification de compétence candidat
- Le candidat peut passer volontairement un test pour vérifier une compétence.
- Le score est conservé sur son profil ; un badge ou niveau peut être affiché
  (ex. *Excel — 87 % — Niveau avancé*).
- Ces résultats sont **distincts** des tests spécifiquement demandés par une entreprise.

## 12. Dashboards

### 12.1 Candidat
Résumé du profil et niveau de complétude · mes candidatures · mes offres recommandées (Premium) ·
mes CV · mes tests et scores · mes badges · messages reçus (Premium selon les offres) · notifications.

### 12.2 Entreprise / Cabinet
Offres actives · nombre de candidatures · profils correspondants · profils présélectionnés ·
tests en cours et terminés · shortlists · pipeline de recrutement · messagerie · historique des recrutements.

### 12.3 Fiche candidat (vue recruteur)
Identité et titre professionnel · **score de correspondance** · **résumé des éléments ayant conduit
au score** · expériences pertinentes · compétences · formations · scores de tests · CV.
Actions : présélectionner, contacter, demander entretien, écarter.

### 12.4 Administration TalVo
Gestion des utilisateurs · validation des entreprises et cabinets · gestion des offres · gestion des
signalements · gestion du catalogue de tests · création et gestion des questions · gestion des
catégories, métiers et compétences · suivi des abonnements · statistiques d'utilisation · journal d'audit.

## 13. Monétisation du MVP

**Candidat Premium** — abonnement mensuel ou annuel : offres personnalisées, nom de l'entreprise,
contact RH, adaptation du CV à une offre, fonctionnalités avancées de valorisation du profil.

**Services professionnels payants** — publication d'offres selon le plan, sourcing de talents,
présélection, tests candidats, shortlist, services de recrutement sur mesure.

> Les tarifs ne sont pas figés dans le MVP : ils seront testés avec les premières entreprises clientes.

## 14. Écrans du MVP

| ID | Écran | Utilisateur |
|---|---|---|
| 01 | Landing Page | Public |
| 02 | Connexion / inscription | Tous |
| 03 | Dashboard candidat | Candidat |
| 04 | Profil candidat | Candidat |
| 05 | Mes CV | Candidat |
| 06 | Créateur de CV | Candidat |
| 07 | Mes candidatures | Candidat |
| 08 | Tests & résultats | Candidat |
| 09 | Offres recommandées | Premium |
| 10 | Détail offre | Public / Candidat |
| 11 | Messagerie | Premium / Professionnel |
| 12 | Dashboard entreprise | Professionnel |
| 13 | Créer une offre | Professionnel |
| 14 | Mes offres | Professionnel |
| 15 | Candidatures | Professionnel |
| 16 | Profils sourcés | Professionnel |
| 17 | Shortlist TalVo | Professionnel |
| 18 | Fiche candidat | Professionnel |
| 19 | Configuration des tests | Professionnel |
| 20 | Résultats des tests | Professionnel |
| 21 | Dashboard admin | Admin |
| 22 | Gestion tests | Admin |
| 23 | Gestion utilisateurs / offres | Admin |
| 24 | Abonnement | Premium / Professionnel |

## 15. Règles métier essentielles

1. Une entreprise doit être **validée** avant de publier une offre publique.
2. Le **nom de l'entreprise est masqué** aux candidats gratuits (modèle Premium).
3. Le CV adapté par TalVo ne peut utiliser **que des informations réellement présentes** dans le
   profil ou le CV du candidat.
4. Un candidat **ne peut pas être présenté comme ayant passé un test** s'il ne l'a pas réalisé.
5. Les **notes internes du recruteur restent privées**.
6. Les **profils sourcés sans candidature** doivent être présentés dans un **espace distinct**.
7. Les scores de matching sont des **aides à la décision**, jamais une décision automatique d'embauche.
8. Les données personnelles ne sont accessibles que selon les **droits et le cadre de consentement** applicables.
9. Les résultats de tests sont **horodatés** et associés à une **tentative identifiable**.
10. Toute action importante de modération ou de modification doit être **journalisée**.

## 16. Hors périmètre V1 (exclusions explicites)

Application mobile native · marketplace freelance · visioconférence intégrée · vérification
automatisée des diplômes · API publique · dashboard national avancé · microservices et
infrastructure complexe · IA conversationnelle générale · signature électronique · intégrations
universités · système de paiement complet (si les pilotes peuvent être facturés manuellement).

## 17. Critères d'acceptation V1

- [ ] Un candidat peut créer son compte et son profil.
- [ ] Un candidat peut importer un CV ou en créer un.
- [ ] Le CV créé peut être exporté en PDF.
- [ ] Un Premium peut adapter son CV à une offre.
- [ ] Un Premium reçoit des offres correspondant à son profil.
- [ ] Un candidat gratuit ne voit que le secteur d'activité de l'entreprise.
- [ ] Un Premium voit le nom de l'entreprise et peut contacter la RH.
- [ ] Une entreprise peut publier une offre et demander des tests.
- [ ] Une entreprise peut sélectionner les tests disponibles.
- [ ] TalVo peut inviter les candidats aux tests.
- [ ] Les candidats peuvent passer les tests en ligne.
- [ ] Les résultats sont calculés et associés aux profils.
- [ ] Un candidat peut afficher ses compétences vérifiées.
- [ ] L'entreprise voit les candidats ayant postulé.
- [ ] L'entreprise voit aussi les talents sourcés par TalVo qui n'ont pas postulé.
- [ ] Les candidatures sont classées selon les critères du poste.
- [ ] TalVo peut produire une shortlist.
- [ ] Les rôles et permissions sont respectés.

## 18. KPI

**Cibles de pilotage V1** : 5 à 10 entreprises/cabinets pilotes · au moins 20 offres actives
cumulées · volume de CV analysés · nombre de tests réalisés · shortlists produites ·
**temps économisé côté recruteur** (comparer tri manuel vs présélection TalVo).

**KPI de suivi** : candidats inscrits · profils complétés · CV créés/importés · entreprises actives ·
offres actives · candidatures · taux de matching · tests complétés · taux de réussite · shortlists
produites · conversion en entretien · conversion en recrutement · Premium actifs · revenus B2B.

## 19. Vision post-MVP

Matching avancé par IA · vérification des diplômes et certifications · passeport professionnel
vérifié · tests adaptatifs · application mobile · intégration WhatsApp/SMS · analytics RH avancés ·
API partenaires · intégration avec établissements de formation · marketplace de consultants et
freelances · services de recrutement externalisés.
