# TalVo — Angles morts du premier débrief

> Sujets techniques et opérationnels absents du cadrage **et** de nos échanges jusqu'ici.
> Classés par famille. Le niveau de criticité indique ce qui peut compromettre la V1.

---

## A. Identité et accès

### A.1 Authentification par téléphone plutôt que par e-mail — **critique**

Le cadrage suppose implicitement un compte e-mail. **En Guinée, le téléphone est l'identifiant
réel ; l'e-mail est secondaire, parfois inexistant ou jamais consulté.** Une inscription qui exige
un e-mail vérifié écartera une part significative des candidats — et ce sera invisible dans les
statistiques, puisqu'on ne mesure pas ceux qui abandonnent.

Décisions à prendre : identifiant principal (téléphone, e-mail, ou les deux) · vérification par
SMS OTP · coût par OTP envoyé · que se passe-t-il quand un candidat change de numéro (fréquent) ·
comment récupérer un compte sans e-mail. Ces choix touchent le modèle de données (`users.email`
en `UNIQUE NOT NULL` est peut-être déjà une erreur) et le tunnel d'inscription entier.

### A.2 Sessions, appareils partagés, cybercafés — **moyen**
Une partie des candidats se connectera depuis un téléphone partagé ou un cybercafé. Durées de
session, déconnexion explicite bien visible, alerte de connexion depuis un nouvel appareil.

### A.3 Comptes professionnels multi-utilisateurs — **moyen**
Le cadrage parle d'« un compte entreprise ». En réalité une entreprise a plusieurs recruteurs, et
un cabinet gère plusieurs clients. Prévoir dès le modèle : organisation → membres → rôles
(admin, recruteur, lecteur). Rétro-ajouter cette structure après la V1 est douloureux.

---

## B. Moteur de tests — la brique la plus sous-spécifiée

### B.1 Autorité du chronomètre — **critique**
Le temps doit être calculé **côté serveur**. Un minuteur client est trivialement contournable
(changer l'horloge, recharger la page). Le serveur enregistre `started_at`, accepte ou refuse les
réponses selon l'échéance réelle, et ne fait jamais confiance à ce que dit le navigateur.

### B.2 Résistance aux coupures réseau — **critique**
Sur une connexion 3G instable, un candidat **perdra sa connexion pendant un test**. Sans
sauvegarde incrémentale de chaque réponse et reprise à l'endroit exact, chaque coupure produit un
test perdu, un candidat furieux et une donnée d'évaluation inexploitable. C'est le point où un
produit conçu pour une connexion stable échoue en pratique.

### B.3 Anti-triche — **critique pour la promesse commerciale**
TalVo vend « des talents évalués ». Si les scores sont contournables, la proposition B2B
s'effondre — et une entreprise pilote qui embauche un candidat au score flatteur puis découvre
son niveau réel ne renouvellera pas.

Mesures proportionnées, par ordre de coût croissant : banque de questions très supérieure au
nombre servi (ratio 5 à 10 pour 1) et tirage aléatoire · ordre des questions et des options
randomisé · durée serrée limitant la recherche en ligne · détection des changements d'onglet et
du collage · empreinte d'appareil et d'adresse IP · corrélation entre score et entretien réel,
mesurée sur le pilote. Ce qui compte n'est pas de rendre la triche impossible, mais **de la rendre
plus coûteuse que d'apprendre**, et de pouvoir détecter les anomalies a posteriori.

### B.4 Qualité et calibration des questions — **élevé**
Le catalogue initial compte 9 tests. À 30 questions par test avec un ratio 5:1, cela fait
**environ 1 350 questions à rédiger, relire et calibrer** — un travail de plusieurs
semaines-personnes, jamais chiffré dans le cadrage. Il faut aussi mesurer la difficulté réelle
de chaque question après le pilote (taux de réussite) et retirer celles qui ne discriminent rien.

### B.5 Contestation d'un résultat — **moyen**
Un candidat contestera un score. Il faut pouvoir rejouer sa tentative, voir ses réponses, et
décider. Prévu par `attempt_answers`, mais l'écran d'arbitrage et la procédure ne le sont pas.

---

## C. Sécurité applicative

### C.1 Fichiers téléversés — **critique**
TalVo accepte des PDF et DOCX de parfaits inconnus. Un PDF peut contenir du code malveillant, un
DOCX des macros, une archive peut être une bombe de décompression. À prévoir : analyse antivirus
avant traitement · vérification du type réel (pas de l'extension) · taille maximale · stockage
hors du domaine applicatif, jamais servi directement · URLs signées à durée courte · isolation
du processus d'extraction.

### C.2 Base — **élevé**
Limitation de débit sur l'authentification et l'envoi d'OTP (un OTP coûte de l'argent : un
attaquant peut faire exploser la facture SMS) · protection contre l'énumération de comptes ·
journalisation des accès aux profils par les recruteurs · gestion des secrets hors du code ·
revue de sécurité avant la mise en production pilote.

### C.3 Cloisonnement des données entre organisations — **critique**
Un recruteur de l'entreprise A ne doit jamais voir les candidatures de l'entreprise B. C'est la
faute la plus classique et la plus grave d'un produit multi-organisations. Le cloisonnement doit
être systématique et testé, pas laissé à la vigilance de chaque requête.

---

## D. Confiance, fraude et modération

### D.1 Fausses offres d'emploi — **critique, spécifique au marché**
Les plateformes d'emploi en Afrique de l'Ouest sont une cible connue d'escroqueries : fausses
offres demandant des « frais de dossier », de « formation » ou de « traitement ». **Une seule
arnaque réussie sur TalVo suffit à détruire la confiance des candidats.**

La validation des entreprises exigée par le cadrage (règle 1) est la bonne réponse, mais elle
n'est pas spécifiée : qui vérifie, sur quelles pièces (RCCM, NIF, attestation), en combien de
temps, avec quel recours en cas de refus ? Il faut aussi un signalement accessible en un clic
depuis chaque offre, et un message explicite et permanent : **TalVo ne demande jamais d'argent à
un candidat**.

### D.2 Faux profils et doublons — **moyen**
Même personne avec deux comptes, CV recopié d'un autre candidat, profils fictifs. Détection par
similarité et par numéro de téléphone, réconciliation, procédure de fusion.

### D.3 Support et réclamations — **élevé, opérationnel**
Qui répond à un candidat dont l'extraction de CV est fausse, dont le test a planté, dont le
compte est bloqué ? Canal de support, délai de réponse, outil de suivi, personne responsable.
C'est un coût récurrent, pas un détail.

---

## E. Exploitation

### E.1 Sauvegardes et reprise d'activité — **critique**
Absent de tous les documents. Il faut définir : fréquence des sauvegardes de la base et du
stockage des CV · durée de conservation · **restauration testée** (une sauvegarde jamais restaurée
n'est pas une sauvegarde) · perte de données maximale acceptable · durée d'interruption
acceptable. Perdre les CV, c'est perdre le vivier, c'est-à-dire l'actif.

### E.2 Observabilité — **élevé**
Sans journalisation centralisée, suivi des erreurs et alertes, la première panne en production se
diagnostique à l'aveugle. À prévoir dès le socle, pas après le premier incident. Pour une chaîne
asynchrone, c'est même indispensable : un CV bloqué en file ne produit aucune erreur visible par
l'utilisateur, il ne se passe simplement **rien**.

### E.3 Environnements et livraison — **élevé**
Développement, recette, production séparés · migrations de base versionnées et réversibles ·
données de test réalistes mais anonymisées · procédure de retour arrière.

### E.4 Disponibilité attendue — **moyen**
Les entreprises pilotes auront des attentes implicites. Les rendre explicites : objectif de
disponibilité, fenêtres de maintenance, engagement de délai en cas d'incident.

---

## F. Communication avec les utilisateurs

### F.1 Délivrabilité e-mail — **élevé**
Configuration SPF/DKIM/DMARC, réputation du domaine, montée en charge progressive. Un e-mail
d'invitation à un test qui part en spam est une candidature perdue et un client déçu.

### F.2 SMS et WhatsApp — **élevé, avec un impact budgétaire réel**
Le cadrage place WhatsApp/SMS en post-MVP. **C'est à réexaminer** : l'invitation à un test est le
point de rupture du tunnel, et le SMS y est bien plus fiable que l'e-mail dans ce contexte.

Attention au budget : contrairement aux autres postes techniques, **le SMS a un coût unitaire non
négligeable** et proportionnel à l'usage. À volume élevé, il peut devenir le premier poste de
dépense variable, devant les modèles d'IA. À chiffrer avec des devis opérateurs locaux.

### F.3 Préférences et désabonnement — **moyen**
Choix du canal, fréquence, désinscription. Exigence légale autant que confort.

---

## G. Mesure — le chaînon manquant des KPI

Le cadrage définit 14 KPI et des cibles de pilotage. **Aucun document ne dit comment ils seront
mesurés.** Or un KPI se mesure avec des événements instrumentés dès le premier jour : une donnée
non collectée en janvier est définitivement perdue pour l'analyse du pilote.

À instrumenter dès la V1 : étapes du tunnel d'inscription (et **abandons**) · dépôt de CV, succès
et échecs d'extraction, **corrections apportées par le candidat** (aussi le carburant du
fine-tuning) · candidatures, invitations aux tests, tests commencés / terminés / abandonnés ·
actions du recruteur sur une fiche candidat · **temps réellement passé par le recruteur**, seule
manière de démontrer le « temps économisé » qui est l'argument de vente central.

---

## H. Facturation et administratif — **élevé, souvent oublié en phase technique**

Devis, factures conformes, TVA guinéenne, suivi des règlements, relances. Réconciliation des
paiements mobile money (rapprochement, litiges, remboursements). Le cadrage autorise la
facturation manuelle des pilotes, ce qui est raisonnable — mais « manuel » signifie qu'une
personne doit le faire, et cela doit figurer au plan de charge.

---

## I. Qualité d'usage

### I.1 Performance sur réseau contraint — **élevé**
Budget de poids par page, images optimisées, chargement différé, fonctionnement acceptable en 3G.
À fixer comme contrainte mesurée, pas comme intention.

### I.2 Accessibilité et niveau de littératie — **moyen**
Au-delà des normes techniques : formulations simples, parcours peu chargés, icônes explicites.
Une partie des utilisateurs n'est pas à l'aise avec les interfaces complexes.

### I.3 Internationalisation — **moyen**
Mécanique de traduction en place dès le début, même avec une seule langue active. Ajouter
l'anglais après coup dans une base de code non préparée coûte dix fois plus cher.

### I.4 Fuseaux horaires et dates — **faible mais piégeux**
La Guinée est à UTC+0, ce qui masquera les bugs. L'expansion régionale les révélera tous d'un
coup, notamment sur les **échéances de tests**. Stocker en UTC, afficher en local, dès le début.

---

## J. Cadre juridique — **critique avant la mise en ligne**

Conditions générales d'utilisation, politique de confidentialité, mentions légales, contrats
entreprises. Registre des traitements, base légale de chaque traitement, durées de conservation,
procédure d'exercice des droits (accès, rectification, effacement, export). Position documentée
sur les transferts de données hors du pays (voir `04-ia-traitement-documentaire.md` §5).

Ce sont des livrables à produire **avant** le pilote, avec un conseil juridique local. Ils ne
relèvent pas de la technique mais bloquent la mise en production.

---

## Synthèse — les sept points à traiter en priorité

| # | Sujet | Pourquoi maintenant |
|---|---|---|
| 1 | Identifiant téléphone vs e-mail | Touche le modèle de données et tout le tunnel d'inscription |
| 2 | Robustesse et anti-triche des tests | Conditionne la crédibilité de la promesse commerciale |
| 3 | Sécurité des fichiers téléversés | Risque d'incident grave dès le premier CV reçu |
| 4 | Validation des entreprises et lutte anti-arnaque | La confiance des candidats ne se répare pas |
| 5 | Sauvegardes et restauration testée | Perdre le vivier, c'est perdre l'entreprise |
| 6 | Instrumentation des KPI | Une donnée non collectée au pilote est perdue |
| 7 | Volume et budget de la banque de questions | Charge de travail importante, jamais chiffrée |
