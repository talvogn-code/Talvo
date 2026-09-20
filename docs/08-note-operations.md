# TalVo — Note aux opérations

> Version de référence de la note destinée à la direction des opérations.
> Volontairement non technique. Montants en dollars, hors salaires, ordres de grandeur
> à confirmer par devis.

## 1. Ce que TalVo fait, en clair

Une entreprise cherche un comptable. Aujourd'hui elle publie une annonce, reçoit cent vingt CV,
et quelqu'un passe deux journées à les trier — souvent mal, parce que lire cent vingt CV à la
suite épuise l'attention.

TalVo remplace ce tri. L'entreprise décrit son besoin, la plateforme lit les CV disponibles,
classe les candidats selon leurs compétences réelles, leur fait passer un test quand c'est
demandé, et présente au recruteur **une liste courte de profils pertinents, avec la raison de
chaque classement**.

Nous ne vendons donc pas de la visibilité, comme un site d'annonces, mais **du temps de recruteur
économisé et une sélection sur laquelle on peut s'appuyer**. Un site d'annonces affiche des
textes ; TalVo doit comprendre des documents et évaluer des personnes. C'est là que va l'essentiel
de l'effort, et c'est ce qui explique les coûts ci-dessous.

## 2. Les six briques à financer

| Brique | À quoi elle sert | Si nous ne la finançons pas |
|---|---|---|
| 1. Lecture des CV | Transformer un PDF, un Word ou une photo en informations exploitables | Tout le reste s'effondre : le classement porte sur du bruit |
| 2. Référentiel métier | Savoir que « Power BI » et « PowerBI » sont la même compétence, qu'une Licence LMD vaut tel niveau | Deux candidats identiques obtiennent deux scores différents. Invendable |
| 3. Classement des candidats | Ordonner les profils **et justifier chaque position** | Nous vendons une boîte noire. Un DRH de banque ne l'achètera pas |
| 4. Tests en ligne | Vérifier une compétence au lieu de la croire sur parole | Nous redevenons un site d'annonces |
| 5. La plateforme | Comptes, offres, candidatures, messagerie, tableaux de bord, administration | Rien n'est utilisable |
| 6. L'exploitation | Sauvegardes, surveillance, sécurité, support | Le produit marche jusqu'au premier incident |

Les briques 1 et 2 sont invisibles pour l'utilisateur et systématiquement sous-estimées. La
brique 2 n'est pas du développement : c'est un travail de constitution de connaissances propre au
marché guinéen, qu'aucun fournisseur ne peut nous vendre.

## 3. Investissement initial (octobre 2026 → janvier 2027)

| Poste | Nature | Charge estimée | Dépense directe |
|---|---|---|---|
| Corpus de CV réels et annotation | Interne | 2 à 3 semaines-personnes | Quasi nulle |
| Comparaison des solutions de lecture | Interne | 1 à 2 semaines-personnes | 200 à 500 $ |
| Maquettes et charte graphique | Prestataire/interne | 3 à 4 semaines | Devis |
| Développement de la V1 | Équipe technique | Novembre → février | Selon l'équipe |
| Banque de questions de tests | Éditorial | **6 à 10 semaines-personnes** | Ou experts métier |
| Référentiel métier initial | Éditorial | 3 à 4 semaines-personnes | Quasi nulle |
| Bibliothèque de formulations | Éditorial | 2 à 3 semaines-personnes | Quasi nulle |
| CGU et politique de confidentialité | Juridique local | — | Devis |
| Revue de sécurité | Prestataire | — | Devis |

**Le développement n'est pas le poste le plus lourd.** Les trois lignes éditoriales représentent
à elles seules **onze à dix-sept semaines-personnes**, absentes de tout document de cadrage. Ce ne
sont pas des tâches d'ingénieur.

## 4. Fonctionnement mensuel

Montants en dollars par mois, **hors salaires**, tarifs publics constatés à confirmer par devis au
moment de la décision. Deux scénarios chiffrés, tous deux limités à Conakry :

- **Pilote** *(janvier à mars 2027)* — environ 2 000 visites/mois, 5 à 10 entreprises, une
  vingtaine d'offres, de l'ordre de 400 CV déposés par mois.
- **Conakry à maturité** *(fin 2027)* — environ 20 000 candidats inscrits, 30 000 visites/mois,
  2 000 CV/mois, 50 à 80 entreprises clientes.

| Poste | Ce qu'il y a dedans · services candidats et base de facturation | Pilote | Conakry à maturité |
|---|---|---|---|
| Serveur d'application | 1 à 2 petites machines (2 vCPU, 4 Go). Hetzner, OVH, Scaleway, DigitalOcean : ~20–25 $/machine. AWS Fargate ou App Runner : facturé à l'usage | 20 – 45 $ | 60 – 120 $ |
| Répartiteur de charge | Point d'entrée unique devant les machines. DigitalOcean ~12 $, AWS ALB ~18–25 $ + trafic. Au début il ne sert pas à la charge mais aux mises à jour sans coupure | 0 – 20 $ | 20 – 30 $ |
| Machines de traitement des documents | Les workers qui lisent les CV. Au pilote ils tiennent sur la machine applicative. Ensuite 1 à 2 machines dédiées, éteintes quand la file est vide | 0 – 15 $ | 25 – 60 $ |
| Base de données | PostgreSQL managé avec sauvegardes. DigitalOcean ~15 $, AWS RDS petite instance ~15–20 $ + stockage, Neon/Supabase gratuit puis ~25 $ | 15 – 35 $ | 50 – 120 $ |
| Stockage des CV | Fichiers déposés. ~0,02 $/Go/mois ; 400 CV pèsent moins d'un Go. Cloudflare R2 ne facture pas la sortie, AWS S3 la facture ~0,09 $/Go | < 2 $ | 5 – 12 $ |
| Diffusion et bande passante | Cloudflare, offre gratuite — suffisante bien au-delà de notre trafic | 0 $ | 0 – 20 $ |
| Lecture des CV par les modèles | Facturé au document. OCR : AWS Textract ou Google Document AI ~1,50 $/1 000 pages. Extraction : Claude Haiku 4.5 à 1 $/M jetons entrée et 5 $/M sortie, moitié prix en batch → **~1 centime par CV de 2 pages**. Modèle ouvert auto-hébergé : coût GPU, pertinent seulement à fort volume régulier | 4 – 15 $ | 20 – 60 $ |
| E-mail | AWS SES ~0,10 $/1 000 messages. Resend, Postmark, Brevo : gratuit jusqu'à quelques milliers/mois | 0 – 5 $ | 10 – 25 $ |
| **SMS** | **Le seul poste vraiment sensible.** Codes de connexion, invitations aux tests, rappels. Agrégateur international (Twilio, Vonage) vers la Guinée : ~0,03 à 0,10 $/message. Agrégateur ou opérateur local (Orange, MTN) : souvent 3 à 10× moins cher, contrat à négocier. Base : ~4 messages par candidat actif | **25 – 120 $** | **120 – 500 $** |
| Surveillance et alertes | Sentry, Grafana Cloud, Better Stack : offres gratuites suffisantes au démarrage | 0 $ | 0 – 30 $ |
| Nom de domaine et certificats | Domaine ~15 $/an. Certificats TLS gratuits | ~2 $ | ~2 $ |
| Sauvegardes externalisées | Copie hors du fournisseur principal, stockage froid | 2 – 5 $ | 10 – 20 $ |
| **Total mensuel** | | **≈ 70 – 265 $** | **≈ 320 – 1 000 $** |

### Et le scénario régional ?

Une version précédente de cette note annonçait 3 000 à 10 000 $/mois. Ce montant correspondait à
**50 000 CV par mois sur plusieurs pays** — un horizon 2029, pas une ligne de budget 2027. Il
indique seulement que même à cette taille, l'infrastructure reste de l'ordre de quelques milliers
de dollars par mois, dont environ la moitié en SMS.

### Ce qui coûte n'est pas le trafic

**Multiplier les visites par dix ne change presque rien au total.** Deux mille ou vingt mille
visites par mois, c'est la même petite machine. Ce qui coûte, ce sont les **CV traités** et les
**SMS envoyés** — deux postes qui suivent le nombre de candidats réellement actifs, pas le nombre
de pages vues. La facture suit donc notre activité réelle, et un mois creux coûte presque le prix
du socle.

### « Je ne paie que mon trafic » : en partie, et c'est voulu

- **À l'usage** — modèles d'IA, SMS, e-mail, stockage : réellement proportionnels à l'activité.
- **À la machine** — serveur applicatif et base de données, montant fixe. À notre volume une
  machine coûte une vingtaine de dollars ; au-delà, le prix à la machine devient nettement plus
  avantageux que la facturation à la requête.

Le répartiteur de charge n'est pas là pour la charge — à 2 000 visites/mois une seule machine
suffit. Il est là pour **mettre à jour sans coupure**, et pour qu'ajouter une machine plus tard
soit un réglage et non une migration.

### Comment cela monte, sans rien réécrire

- Serveur applicatif et workers sans état : monter en charge, c'est **en ajouter**.
- La base grandit en taille, puis par réplicas de lecture.
- Le stockage des fichiers est illimité par construction.
- Le traitement des documents monte **indépendamment du site** : une rafale de 500 candidatures
  allonge la file, elle ne ralentit pas la navigation.

Rien dans l'architecture ne change entre les deux colonnes — seuls le nombre et la taille des
machines. C'est ce que nous achetons en séparant dès le départ le site, l'API et les workers.

## 5. Les deux postes qui surprennent

**Le SMS coûtera plus cher que l'IA.** Chaque message se paie à l'unité et le volume croît avec
les utilisateurs. Tout passer par e-mail serait une erreur : beaucoup de candidats n'ont pas
d'adresse active, et une invitation à un test qui n'arrive pas est une candidature perdue et un
client déçu. Demander des devis opérateurs dès maintenant.

**Le travail de contenu n'est pas du développement.** Environ 1 300 questions de tests (trente
servies au hasard dans un stock cinq à dix fois plus grand), le référentiel métier, la
bibliothèque de formulations. Trois chantiers qui demandent des gens qui connaissent les métiers.
Ils peuvent démarrer dès octobre, en parallèle.

## 6. Ce que nous ne dépensons pas

Application mobile installée · infrastructure complexe · plateforme de lecture de documents du
marché (conçue pour des factures, pas des CV) · entraînement d'un modèle sur mesure (inutile avant
d'avoir mesuré les erreurs réelles) · système de paiement complet (facturation manuelle au pilote)
· vérification automatique des diplômes. Dépenses reportées jusqu'à ce qu'un usage réel les
justifie.

## 7. Les risques à couvrir

| Risque | Conséquence | Parade |
|---|---|---|
| Fausses offres réclamant des « frais de dossier » | La confiance des candidats ne se répare pas | Validation des entreprises, signalement en un clic, message permanent : TalVo ne demande jamais d'argent |
| Triche aux tests | Candidat bien noté et incompétent → client perdu | Tirage aléatoire dans un large stock, durée serrée, détection d'anomalies |
| Perte des données | Perdre les CV, c'est perdre le vivier | Sauvegardes **et restauration testée** |
| Lecture erronée d'un CV | Bon candidat mal classé, sans le savoir | Le candidat voit et corrige ce que la machine a lu |
| Coupure réseau pendant un test | Test perdu, évaluation inutilisable | Enregistrement au fil de l'eau, reprise où le test s'est arrêté |
| Fichier malveillant déposé | Incident de sécurité dès les premiers CV | Antivirus, vérification du type, traitement isolé |
| Litige d'abonnement | Réputation abîmée, remboursement difficile en mobile money | Prix clairs, reconduction explicite, résiliation immédiate |

Un risque ne se couvre pas par la technique : **le support**. Quelqu'un doit répondre au candidat
dont le test a planté. Charge récurrente à prévoir dès le pilote.

## 8. Ce que nous demandons maintenant

1. **Feu vert pour constituer un recueil de 150 à 200 CV réels** (consentement, anonymisation).
   Argent : quasi nul. Temps : 2 à 3 semaines. C'est ce qui permettra de choisir notre solution de
   lecture sur mesures réelles plutôt que sur les démonstrations des fournisseurs.
2. **Mise en relation avec 3 à 5 entreprises pilotes dès octobre** — pour les CV, et surtout pour
   leur poser une question qui engage notre infrastructure : *exigez-vous que les données restent
   dans le pays ou sur le continent ?*
3. **Budget d'amorçage de quelques centaines de dollars** pour les tests comparatifs.
4. **Une personne à temps partiel sur le contenu dès octobre** — profil marché du travail
   guinéen, pas informaticien.
5. **Un conseil juridique local**, à engager avant décembre : CGU et politique de confidentialité
   conditionnent la mise en ligne.

## 9. Calendrier et points de décision

| Période | Ce qui se passe | Décision attendue |
|---|---|---|
| Sept. 2026 *(en cours)* | Cadrage | Valider le périmètre, lancer le recueil de CV |
| Oct. 2026 | Maquettes · recueil et annotation · contenu | **Choisir la solution de lecture des CV**, sur résultats mesurés |
| Nov. 2026 | Socle technique | Arbitrer l'hébergement selon les exigences des pilotes |
| Déc. 2026 | Offres, candidatures, classement, tests | Valider la banque de questions et les CGU |
| Jan. 2027 | **Mise en service pilote** (5 à 10 entreprises) | Accord des pilotes, ouverture |
| Fév. 2027 | Stabilisation | Fixer les tarifs d'après le pilote |
| Mars 2027 | Premium, messagerie, sourcing | Mode de paiement : mobile money en priorité |

Le calendrier tient et rien de ce qui est demandé ne le décale — recueil et contenu se font
**pendant** la phase de maquettes d'octobre. Le risque réel de report est ailleurs : laisser le
travail éditorial pour « plus tard » et le découvrir en décembre, quand l'équipe technique sera
saturée. C'est le scénario le plus facile à éviter.
