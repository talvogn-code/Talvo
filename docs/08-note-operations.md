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

Pilote : 5 à 10 entreprises, quelques centaines de CV par mois. À l'échelle : ~50 000 CV/mois,
plusieurs pays.

| Poste | Pilote | À l'échelle |
|---|---|---|
| Hébergement de l'application | 50 – 150 $ | 400 – 1 200 $ |
| Machines de traitement des documents | 50 – 150 $ | 300 – 1 000 $ |
| Base de données et sauvegardes | 60 – 200 $ | 300 – 900 $ |
| Stockage des CV | < 10 $ | 50 – 150 $ |
| Modèles d'IA (lecture des CV) | 10 – 30 $ | 400 – 1 200 $ |
| E-mail | 0 – 30 $ | 100 – 300 $ |
| **SMS et WhatsApp** | **80 – 250 $** | **1 500 – 5 000 $** |
| Surveillance et alertes | 0 – 50 $ | 100 – 300 $ |
| **Total** | **≈ 250 – 870 $** | **≈ 3 150 – 10 050 $** |

Deux enseignements : le coût technique du pilote est **modeste** — l'équilibre se joue sur les
salaires et la vente, pas ici ; et **l'IA n'est pas le poste coûteux** (moins d'un centime par CV).
Le poste qui grossit avec le succès, c'est le SMS.

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
