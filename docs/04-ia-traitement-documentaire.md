# TalVo — IA et traitement documentaire

> **Statut : analyse, pas décision.** Ce document cartographie le problème et les options.
> Aucun choix de fournisseur ou de stack n'y est arrêté. Il se conclut par le protocole de
> mesure qui permettra de décider sur des données réelles plutôt que sur des impressions.

## 1. Le vrai problème

TalVo n'est pas un site d'annonces avec un champ « joindre votre CV ». La promesse est :
**« déposez un document, nous le comprenons, nous le classons, nous l'évaluons »**. Tout le
produit repose donc sur une chaîne de compréhension documentaire fiable. Si elle échoue,
le matching classe du bruit, la shortlist n'a pas de valeur, et la proposition B2B s'effondre.

### 1.1 Ce qui va réellement arriver dans l'application

| Type d'entrée | Fréquence attendue | Difficulté |
|---|---|---|
| PDF natif export Word, 1 colonne | élevée | faible |
| PDF natif, mise en page 2 colonnes / encadrés | élevée | **moyenne à forte** — l'ordre de lecture est faux si on extrait naïvement |
| PDF scanné (imprimé puis numérisé) | moyenne | **forte** — OCR requis |
| Photo de CV prise au téléphone, insérée dans un PDF ou un DOCX | non négligeable | **très forte** — inclinaison, ombres, flou, contraste |
| DOCX avec tableaux invisibles pour la mise en page | élevée | moyenne — l'ordre logique ≠ ordre du flux |
| DOCX avec zones de texte / colonnes | moyenne | forte |
| CV de 4 à 8 pages, très verbeux | moyenne | moyenne |
| CV en anglais (candidats régionaux) | croissante | moyenne |

Deux pièges spécifiques au contexte ouest-africain, sous-estimés par les outils conçus pour
des CV nord-américains :

1. **Le parc matériel et la connectivité.** Une part des candidats produira un document
   dégradé : photographié plutôt que scanné, compressé, parfois de travers. Un pipeline qui
   suppose un PDF propre échouera silencieusement sur ce segment — c'est-à-dire précisément
   sur les candidats les moins équipés.
2. **Les référentiels locaux.** Diplômes (BTS guinéen, Licence LMD, diplômes d'écoles
   régionales), employeurs locaux, secteurs dominants (mines, télécoms, ONG, administration),
   expérience en économie informelle, mentions de stages longs. Aucune taxonomie internationale
   (ESCO, O*NET) ne couvre correctement cela. C'est un travail de référentiel propre à TalVo.

### 1.2 Pourquoi l'extraction naïve ne suffit pas

Extraire le texte d'un PDF sur deux colonnes sans analyse de mise en page produit typiquement
l'entrelacement des colonnes : une ligne d'expérience, une ligne de compétences, une ligne
d'expérience. Le texte est *présent* mais sémantiquement détruit. Aucun modèle en aval ne
rattrape proprement ce désordre. **L'analyse de mise en page n'est pas une option.**

## 2. « Faut-il une IDP ? »

**IDP** (*Intelligent Document Processing*) = capture → classification → OCR/analyse de mise en
page → extraction structurée → validation → intégration.

**Réponse courte : oui, TalVo a besoin d'une chaîne IDP. Non, cela n'implique pas
nécessairement d'acheter une plateforme IDP du marché.**

Les plateformes IDP commerciales (Google Document AI, AWS Textract, Azure Document
Intelligence, Rossum, Instabase) sont optimisées pour des **documents à champs fixes** :
factures, bons de commande, formulaires, pièces d'identité. Leur force est la détection de
champs et de tableaux sur des gabarits récurrents. Un CV n'est pas cela : c'est un document
**semi-structuré et narratif**, dont la difficulté est la compréhension de prose libre et de
chronologie, pas la localisation d'un champ « Total TTC ».

La question pertinente n'est donc pas « IDP ou pas », mais **acheter ou construire, couche par
couche**.

### 2.1 Décomposition acheter / construire

| Couche | Ce qu'elle fait | Acheter | Construire | Orientation |
|---|---|---|---|---|
| Capture & triage | MIME, détection couche texte vs scan, anti-virus, limites de taille | — | trivial | **Construire** |
| OCR + mise en page | texte + coordonnées + ordre de lecture + blocs | Document AI, Textract, Azure DI, OCR spécialisés | PaddleOCR, Surya, docTR (auto-hébergés) | **Acheter d'abord, abstrait derrière une interface.** Réévaluer l'auto-hébergement au volume |
| Extraction structurée | prose → expériences, formations, compétences, dates | Parseurs de CV dédiés (Textkernel/Sovren, Daxtra, Affinda, RChilli, HireAbility) · Modèles multimodaux (VLM) | LLM avec sortie structurée + schéma | **Mesurer les deux.** Les parseurs dédiés sont matures mais calibrés sur des CV occidentaux et contraignent le schéma |
| Normalisation / ontologie | « Power BI » = « PowerBI » ; « Licence en Info » → niveau + domaine ; employeur → secteur | ESCO, O*NET (partiels) | référentiel TalVo + embeddings + alias | **Construire — c'est l'actif différenciant** |
| Validation humaine | le candidat corrige, ce qui produit de la donnée d'entraînement | — | — | **Construire (déjà exigé par le cadrage §8.1)** |
| Intégration | écriture profil/CV, provenance, versions | — | — | **Construire** |

### 2.2 L'approche multimodale change l'arbitrage

Une chaîne classique sépare OCR puis compréhension. Les modèles multimodaux récents acceptent
directement l'**image de la page** et produisent du JSON structuré, en absorbant OCR, mise en
page et extraction en une seule étape. Sur des documents dégradés ou à mise en page atypique —
exactement notre cas difficile — cette voie est souvent supérieure à la chaîne classique, et
plus simple à opérer.

Elle a deux contreparties à mesurer, pas à supposer :
- **Coût par page** à volume (à chiffrer sur les tarifs en vigueur au moment de la décision) ;
- **Absence de coordonnées** exploitables si le modèle ne les restitue pas — or la provenance
  (« cette date vient de la page 2, bloc 3 ») est ce qui rend l'écran de correction utilisable
  et l'extraction auditable.

**Conséquence de conception, quelle que soit l'option retenue : la provenance de chaque champ
extrait doit être stockée.** C'est un choix structurant, à acter tôt.

### 2.3 Ce qui doit être vrai dans tous les cas

1. **La chaîne est asynchrone.** Dépôt → file → workers → statut. Un traitement peut prendre de
   quelques secondes à plusieurs minutes. Un modèle requête/réponse synchrone ne tient pas, et
   contraint fortement le choix d'hébergement (voir §4).
2. **Les fournisseurs sont abstraits derrière une interface interne.** `OcrProvider`,
   `ExtractionProvider`. Changer de fournisseur, en tester deux en parallèle (*shadow mode*) ou
   basculer vers de l'auto-hébergé ne doit jamais être une réécriture.
3. **Chaque extraction est versionnée** (`pipeline_version`, `model_version`) et **rejouable**
   sur le document d'origine. Sans cela, on ne peut ni mesurer une amélioration, ni corriger un
   lot de profils mal extraits.
4. **Le document brut est conservé.** Il est la seule source de vérité ; toute extraction est
   dérivée et jetable.
5. **Le candidat valide.** Aussi bon soit le modèle, la correction humaine reste le filet de
   sécurité — et la source d'un jeu de données propriétaire qui, au bout de milliers de CV,
   devient l'actif le plus difficile à répliquer par un concurrent.

## 3. Cartographie des besoins d'IA dans TalVo

Le cadrage sous-estime la place de l'IA : il la mentionne surtout comme évolution future du
matching. En réalité, sept usages distincts apparaissent, de maturité et de risque très différents.

| # | Usage | Nécessaire en V1 | Nature | Risque |
|---|---|---|---|---|
| 1 | Compréhension du CV déposé (OCR + extraction) | **Oui, P0** | IDP / multimodal | Élevé — tout en dépend |
| 2 | Normalisation compétences / fonctions / diplômes | **Oui, P0** | Embeddings + référentiel curé | Moyen |
| 3 | Extraction structurée de l'offre d'emploi rédigée en prose | Souhaitable | LLM structuré | Faible |
| 4 | Matching sémantique (rappel au-delà des mots-clés) | Partiel | Embeddings + recherche vectorielle | **Conflit avec l'exigence d'explicabilité — voir §3.1** |
| 5 | Adaptation du CV à une offre (Premium) | P1 | LLM génératif **contraint** | **Élevé — risque d'invention, voir §3.2** |
| 6 | Génération/calibration de questions de tests | Confort admin | LLM | Faible |
| 7 | Détection d'anomalies (fraude, doublons, CV recopiés) | Post-MVP | Heuristiques + similarité | Faible |

### 3.1 Résoudre la tension « sémantique » vs « explicable »

Le cadrage impose un moteur explicable. L'IA sémantique est, par nature, difficile à justifier.
Ces deux exigences ne s'opposent que si on les place au même endroit. La réponse d'architecture :

- **Rappel (*recall*) — IA autorisée.** Trouver les candidats plausibles dans le vivier, y compris
  ceux dont le vocabulaire diffère de celui de l'offre. Un candidat écrit « états financiers »,
  l'offre demande « reporting comptable » : seule la similarité sémantique les rapproche. Ici,
  on ne justifie rien : on élargit un ensemble de candidats.
- **Classement (*ranking*) — règles pondérées uniquement.** Le score affiché au recruteur,
  celui qui ordonne la shortlist, reste le moteur 35/30/15/10/10 avec son `breakdown`
  (voir `02-moteur-matching.md`).
- **Le pont** : quand la similarité sémantique fait correspondre deux termes, cette
  correspondance devient une **entrée du référentiel** (alias), validée par un humain. L'IA
  alimente alors le référentiel explicable au lieu de le contourner. Le système apprend, et
  reste justifiable.

Cette séparation n'est pas un compromis : elle est aussi la réponse à la contrainte
réglementaire (§5).

### 3.2 L'adaptation de CV : la fonction la plus délicate

Le cadrage est net (§8.3) : **interdiction d'inventer** une compétence, un diplôme, une
expérience. Or un LLM à qui l'on demande « améliore ce CV pour cette offre » embellira — c'est
son comportement par défaut, pas un bug.

Il ne suffit pas de l'écrire dans la consigne. Il faut un **vérificateur** : chaque affirmation
du CV produit doit être rattachable à un élément du CV source. Une sortie non rattachable est
rejetée ou signalée, jamais publiée en silence. La fonction n'est donc pas « un appel de
modèle » mais **génération contrainte + vérification d'ancrage + signalement des manques**
(ce dernier point étant d'ailleurs explicitement demandé par le cadrage).

C'est aussi un enjeu de responsabilité : un CV enjolivé par TalVo et démenti en entretien
détruit la confiance des entreprises clientes, qui sont la source de revenus.

## 4. Architecture pour l'échelle

Ambition affichée : Guinée, puis Afrique de l'Ouest, puis continent. Cela impose des choix
structurants **maintenant**, et en écarte d'autres.

### 4.1 Ce que la charge documentaire impose

Une chaîne IDP ne ressemble pas à une application web classique :
- traitements **longs** (secondes à minutes), donc **file de travaux + workers**, jamais de
  fonctions à délai court ;
- travail **par rafales** (une campagne de recrutement génère 500 candidatures en 48 h), donc
  **workers élastiques** et découplés du web ;
- éventuellement **GPU** si des modèles sont auto-hébergés ;
- **stockage objet** volumineux et durable.

C'est la raison technique — et non une préférence — pour laquelle une plateforme entièrement
*serverless* orientée requête/réponse est un mauvais point de départ ici. Il faut du calcul
maîtrisé : conteneurs orchestrés, pool de workers, région choisie.

### 4.2 Ce qu'il ne faut pas faire pour autant

Le cadrage exclut explicitement microservices et infrastructure complexe du MVP, et il a
raison. « Scalable » ne signifie pas « distribué dès le premier jour ». Une architecture qui
porte TalVo jusqu'à plusieurs millions de profils :

```
┌────────────┐   ┌──────────────┐   ┌──────────────────────┐
│  Web (SSR) │──▶│  API modulaire│──▶│ PostgreSQL (primaire │
│  mobile-1er│   │  (monolithe   │   │  + réplicas lecture) │
└────────────┘   │   modulaire)  │   └──────────────────────┘
                 └───────┬───────┘              ▲
                         │ publie               │
                    ┌────▼─────┐   ┌────────────┴──────┐
                    │  File    │──▶│ Workers (élastiques│
                    │ de jobs  │   │ IDP · matching ·   │
                    └──────────┘   │ PDF · emails)      │
                                   └────────┬───────────┘
                                   ┌────────▼───────────┐
                                   │ Stockage objet (CV)│
                                   └────────────────────┘
```

Trois frontières seulement, mais nettes : **web / API modulaire / workers**, plus Postgres et
le stockage objet. Les modules métier (matching, IDP, tests, facturation) sont isolés *dans le
code* — dépendances explicites, pas d'accès croisé aux tables d'un autre module — de sorte que
l'extraction ultérieure d'un module en service autonome soit mécanique. On paie la discipline
d'architecture, pas la complexité opérationnelle.

Le point dur de l'échelle n'est presque jamais le serveur web : c'est la base de données et le
coût unitaire du traitement documentaire. Les deux se traitent par la conception (index,
partitionnement à terme, cache, coût par CV mesuré), pas par le nombre de services.

### 4.3 Multi-pays dès le modèle de données

Rétro-ajouter le multi-pays est une des migrations les plus douloureuses qui soient. À intégrer
dès la V1, même si un seul pays est ouvert :

- `country_code` sur les entités géographiques, les offres, les organisations, les abonnements ;
- **référentiels par pays** : régions/villes, systèmes de diplômes, secteurs, types de contrat
  (le droit du travail diffère : CDI/CDD guinéen ≠ sénégalais ≠ nigérian) ;
- **devises** et prix par marché (GNF, XOF, NGN, GHS…), jamais un prix unique ;
- **téléphones** au format international, indicatifs multiples ;
- **langues** : français d'abord, anglais indispensable pour l'Afrique anglophone, portugais et
  arabe selon expansion. L'interface **et** la chaîne d'extraction doivent être multilingues —
  un OCR mal configuré sur les accents français produit des données fausses de manière discrète.

### 4.4 Réalités du terrain

- **Mobile d'abord, réseau contraint.** Une grande partie des candidats sera sur mobile en 3G.
  Poids des pages, tolérance aux coupures, reprise d'envoi, upload depuis l'appareil photo.
  Une PWA sobre sert mieux ce public qu'une application lourde (le natif est P2 au cadrage).
- **Dépôt par photo.** Puisqu'il arrivera de toute façon, autant le traiter comme un cas
  nominal : cadrage assisté, redressement, contrôle de netteté **avant** l'envoi.
- **Canal d'invitation aux tests.** L'e-mail est un point de rupture du tunnel dans la région.
  Le cadrage place WhatsApp/SMS en post-MVP ; c'est à réexaminer, car un test non passé
  invalide toute la promesse de présélection.
- **Paiement.** Mobile money (Orange Money, MTN MoMo, Wave) avant la carte bancaire pour le
  Premium candidat. Structurant pour l'abonnement, à anticiper même si la facturation des
  pilotes reste manuelle.

## 5. Données personnelles et conformité

Un CV est une donnée personnelle ; TalVo en traitera des volumes importants et les soumettra à
des traitements automatisés affectant l'**accès à l'emploi**. Trois conséquences concrètes :

1. **Transferts hors du pays.** Envoyer les CV à une API de modèle hébergée hors d'Afrique est
   un transfert transfrontalier. C'est peut-être acceptable, mais ce doit être **un choix
   documenté**, pas un effet de bord. Les clients corporate visés (banques, mines, télécoms,
   ONG internationales) appliquent les politiques de leur groupe et poseront la question lors
   de la contractualisation. L'abstraction des fournisseurs (§2.3) est aussi ce qui permettra
   de rapatrier le traitement si un grand compte l'exige.
2. **Décision automatisée.** Le score classe des candidats. Le cadrage interdit déjà de le
   présenter comme une décision d'embauche (règle 7) — c'est la bonne position, et elle doit
   être tenue dans l'interface, pas seulement dans le document. Les cadres réglementaires
   émergents (AI Act européen pour les groupes internationaux, législations africaines en
   construction sur la protection des données) classent ce type d'usage comme sensible.
3. **Biais.** Un moteur entraîné ou réglé sans précaution peut pénaliser systématiquement un
   profil (genre déduit du prénom, établissement d'origine, quartier). L'explicabilité du
   moteur à règles est ici un **avantage commercial** autant qu'une protection : elle rend le
   biais mesurable. Prévoir un audit périodique de distribution des scores.

## 6. Ce qu'il faut faire avant de décider

Aucun arbitrage sérieux n'est possible sans mesure. Les parseurs de CV du marché, les IDP
généralistes et les approches multimodales sont tous « bons » sur leurs démonstrations, faites
sur des CV qui ne ressemblent pas à ceux que TalVo recevra.

### Livrable proposé : corpus d'évaluation + banc de mesure

1. **Constituer un corpus de 150 à 200 CV réels**, représentatifs : PDF natifs 1 et 2 colonnes,
   scans, photos, DOCX, 1 à 6 pages, français et anglais, profils juniors et seniors, secteurs
   mines/banque/télécoms/ONG/administration. Sources : entreprises pilotes, cabinets,
   universités, candidatures spontanées — **avec consentement explicite et anonymisation**.
2. **Annoter une vérité terrain** sur un sous-ensemble (≈ 50 CV) : expériences avec dates,
   employeurs, intitulés, formations, compétences. C'est le travail le plus ingrat du projet et
   le plus rentable.
3. **Mesurer 3 à 4 chaînes candidates** sur le même corpus : au minimum une chaîne classique
   (OCR commercial + LLM structuré), une chaîne multimodale directe, un parseur de CV du marché,
   et une option auto-hébergée.
4. **Comparer sur cinq axes** : exactitude par champ (précision/rappel), taux d'échec total,
   coût par CV, latence, effort de correction résiduel côté candidat.

Ce corpus reste ensuite le **harnais de non-régression permanent** de TalVo : tout changement de
modèle, de fournisseur ou de version se mesure dessus. C'est un actif durable, indépendant de la
stack, et il peut être constitué **pendant** la phase UX/UI d'octobre sans retarder le planning.

### Questions ouvertes à instruire en parallèle

- Volumes réalistes à 12 et 36 mois (CV traités/mois) — détermine le seuil de bascule vers
  l'auto-hébergement.
- Exigences de localisation des données des entreprises pilotes — à demander dès les premiers
  entretiens commerciaux, cela peut contraindre l'hébergement.
- Budget cible par CV traité, et budget d'infrastructure mensuel acceptable.
- Compétences de l'équipe qui maintiendra la plateforme après la V1 — c'est cela, et non la
  performance théorique, qui doit trancher entre acheter et auto-héberger.
