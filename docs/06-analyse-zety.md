# TalVo — Analyse de Zety : ce qui est transposable, ce qui ne l'est pas

> Analyse d'un produit cité en référence. Objectif : séparer ce qui mérite d'être repris de ce
> qui relève d'un modèle économique et d'un marché différents.

## 1. Avertissement sur les sources

Les descriptions de « l'architecture IT de Zety » qui circulent — y compris celles produites par
des moteurs de recherche assistés par IA — sont en grande partie **des conjectures plausibles,
pas des faits vérifiés**. Zety ne publie pas son architecture.

Il suffit de relire ces textes pour repérer les marqueurs d'incertitude : « bien que
l'architecture exacte soit privée », « des frameworks **similaires à** React ou Vue.js »,
« **généralement** hébergée sur AWS ou GCP ». Docker/Kubernetes, Redis, Cloudflare, SQL/NoSQL
distribués : ce sont les composants que l'on citerait pour **n'importe quel** SaaS à fort trafic.
Cette description n'est pas fausse — elle n'est simplement **pas spécifique à Zety**, donc elle
n'apprend rien d'exploitable.

Second biais à connaître : plusieurs de ces analyses proviennent de **concurrents directs**
(Enhancv, LiveCareer, ResumeMind, SoundCV publient des « reviews » de Zety). Ce sont des contenus
marketing optimisés pour le référencement, pas des audits techniques.

**Ce qui est raisonnablement établi :** Zety est un produit du groupe **BOLD LLC**, qui édite
également LiveCareer, MyPerfectResume et ResumeNow ; le produit existe depuis le milieu des
années 2010 ; une partie de l'ingénierie est en Pologne ; le modèle est un abonnement B2C avec
une période d'essai à bas prix.

**Ce qui n'est pas établi :** le détail du frontend, l'orchestration, les fournisseurs cloud,
la nature exacte de l'intégration IA, et la consistance réelle des « algorithmes propriétaires
entraînés sur 10 ans de données ».

## 2. Ce que Zety est réellement

**Un éditeur de CV grand public en libre-service, vendu par abonnement.**

Zety n'a **pas** de côté entreprise. Pas d'offres d'emploi, pas de candidatures, pas de matching,
pas de tests, pas de shortlist, pas de recruteur. Son client est le candidat, et son produit est
un document.

C'est une différence de nature, pas de taille. Dans le périmètre TalVo, Zety correspond aux
écrans 05 et 06 — *Mes CV* et *Créateur de CV* — soit **deux écrans sur vingt-quatre**. Les
modules Matching, Sourcing, Présélection, Tests et Dashboards entreprise, c'est-à-dire ce qui
fonde la proposition de valeur B2B de TalVo, n'ont aucun équivalent chez Zety.

Il ne faut donc pas chercher chez Zety un modèle d'architecture pour TalVo. En revanche, sur les
deux écrans où les produits se recouvrent, Zety est un excellent étalon.

## 3. Ce qui mérite d'être repris

### 3.1 La fidélité WYSIWYG → PDF

C'est le vrai défi technique d'un éditeur de CV, et il est systématiquement sous-estimé : **ce
que l'utilisateur voit à l'écran doit être exactement ce qu'il télécharge**, pagination comprise.
Les pièges concrets : une ligne coupée en bas de page, une section orpheline, une police
substituée qui décale la mise en page, des accents rendus différemment à l'écran et au PDF.

L'approche éprouvée est le rendu HTML/CSS via un navigateur *headless* côté serveur — un seul
moteur de rendu, donc une seule vérité. C'est plus lourd qu'une bibliothèque PDF, et c'est le
prix de la fidélité.

### 3.2 La sortie lisible par les ATS

Zety met en avant des modèles « ATS-friendly ». Derrière l'argument marketing, il y a une
contrainte réelle : un CV mis en page en colonnes, en tableaux ou en zones de texte est mal
relu par les systèmes de tri automatique.

**Ironie utile : TalVo est lui-même un ATS.** Le pipeline de compréhension documentaire de
`04-ia-traitement-documentaire.md` est exactement ce qui peine sur les CV mal structurés. TalVo
sait donc, mieux que quiconque, ce qui rend un CV lisible par une machine — et peut garantir que
les CV qu'il **produit** sont parfaitement lisibles par le moteur qui les **relira**.

C'est un avantage de boucle fermée que Zety n'a pas : Zety optimise pour des ATS tiers qu'il ne
contrôle pas et ne mesure pas.

### 3.3 La bibliothèque de contenu rédactionnel

La fonction la plus imitée de Zety n'est pas de l'IA : c'est un **catalogue de formulations
pré-rédigées par métier** (phrases d'accroche, descriptions de missions, compétences typiques).
L'utilisateur choisit plutôt qu'il ne rédige.

C'est un **actif éditorial**, pas un actif technique — donc peu coûteux à produire et à fort
effet perçu. Et c'est particulièrement pertinent en Guinée, où une part importante des candidats
n'a jamais été formée à rédiger un CV : le blocage n'est pas l'outil, c'est la page blanche.

Point d'attention : ce catalogue doit être **local**. Les formulations calquées sur le marché
nord-américain sonnent faux et décrivent des réalités professionnelles qui ne sont pas celles du
tissu économique guinéen.

### 3.4 Le vrai moteur de Zety : le référencement

Ce qu'il faut réellement admirer chez Zety n'est pas la technique, c'est **la machine
d'acquisition**. Des milliers d'articles de conseil carrière, déclinés en de nombreuses langues,
positionnés sur les requêtes que tape un candidat (« modèle de CV », « lettre de motivation
exemple », « CV comptable »), qui captent un trafic massif et le convertissent en essai payant.

**C'est directement transposable à TalVo**, et c'est même stratégique : les pages publiques
d'offres d'emploi (écran 10) et le contenu conseil sont le **canal d'acquisition candidats** de
TalVo — sur un marché où aucun acteur n'occupe sérieusement le terrain francophone ouest-africain.
Cela a une conséquence d'architecture directe : **les pages publiques doivent être rendues côté
serveur et indexables**. Une application monopage qui n'affiche rien sans JavaScript rate ce
canal.

## 4. Ce qu'il ne faut pas reprendre

### 4.1 L'entonnoir d'abonnement

Le schéma de Zety — essai à très bas prix se transformant automatiquement en abonnement récurrent
nettement plus cher — lui vaut des critiques récurrentes sur les plaintes d'utilisateurs qui
n'avaient pas compris s'engager.

Ce schéma serait une **erreur grave** pour TalVo, pour trois raisons :
1. TalVo est un **produit biface**. Un candidat qui se sent piégé ne détruit pas seulement sa
   propre relation au produit : il en parle, et le vivier de candidats est l'actif que TalVo
   vend aux entreprises.
2. Sur un marché où la confiance dans le paiement en ligne est encore en construction, un litige
   d'abonnement coûte beaucoup plus cher en réputation qu'il ne rapporte.
3. Les moyens de paiement locaux (mobile money) se prêtent mal au remboursement. Un litige n'est
   pas absorbable aussi facilement qu'avec une carte bancaire.

Position recommandée : **prix affichés clairement, reconduction explicite, résiliation immédiate.**
La confiance est ici un actif commercial, pas une contrainte morale.

### 4.2 Le niveau de prix

L'abonnement de Zety se situe à quelques dizaines d'euros par mois sur les marchés occidentaux.
**Ce niveau est hors d'atteinte pour un candidat guinéen.** Le Premium TalVo doit être tarifé en
monnaie locale, à un niveau compatible avec le pouvoir d'achat réel, et encaissé par mobile money.

Conséquence stratégique importante : **le Premium candidat ne financera pas TalVo.** Il a une
fonction de valorisation du profil, d'engagement et de qualification du vivier ; **le revenu
vient du B2B** — sourcing, présélection, tests, shortlist. Le cadrage l'a d'ailleurs bien vu en
plaçant les services professionnels au cœur de la monétisation. Zety, qui est un pur B2C, ne peut
servir de modèle économique.

### 4.3 La revendication « dix ans de données »

Zety s'appuie sur un historique que TalVo ne peut pas répliquer, et il serait vain d'essayer.
Mais cet historique est **occidental** : il ne dit rien du marché de l'emploi guinéen, des
employeurs locaux, des diplômes régionaux, ni des parcours en économie informelle.

Sur ce terrain, TalVo part avec zéro donnée — et Zety aussi. **Le premier acteur qui constitue un
référentiel professionnel ouest-africain structuré crée un actif que personne ne peut acheter.**
C'est cohérent avec ce qui est dit en `04-ia-traitement-documentaire.md` : la normalisation, pas
l'OCR, est le moat.

## 5. Ce qu'il faut en retenir

| Sujet | Verdict |
|---|---|
| Architecture technique de Zety | Non documentée publiquement ; les descriptions disponibles sont génériques. Sans valeur décisionnelle |
| Éditeur de CV WYSIWYG + fidélité PDF | **À reprendre** — c'est le vrai savoir-faire, et il est exigeant |
| Sortie lisible par les ATS | **À reprendre**, avec un avantage propre : TalVo est son propre ATS |
| Bibliothèque de formulations par métier | **À reprendre**, en version localisée — fort impact, faible coût |
| Machine de référencement et de contenu | **À reprendre** — c'est le vrai moteur de Zety, et le canal d'acquisition de TalVo |
| Entonnoir d'abonnement agressif | **À rejeter** — destructeur sur un produit biface et un marché à confiance fragile |
| Niveau de prix | **Non transposable** — tarification locale, revenu porté par le B2B |
| Historique de données | Non réplicable, et non pertinent pour l'Afrique de l'Ouest — construire le référentiel local |

**En une phrase :** Zety est un excellent étalon pour deux écrans de TalVo et un modèle
d'acquisition à étudier de près, mais ce n'est ni un modèle d'architecture, ni un modèle
économique pour une plateforme biface en Afrique de l'Ouest.
