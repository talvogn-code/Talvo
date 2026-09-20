# TalVo — Stratégie de modèles IA, coût et anti-hallucination

> **Statut : analyse.** Aucun fournisseur n'est retenu ici. Ce document pose la méthode de
> sélection, les familles de modèles candidates, l'ordre des garde-fous anti-hallucination et
> la place réelle du *fine-tuning*.

## 1. Principe directeur

**Aucun modèle n'est choisi sans mesure sur le corpus TalVo** (voir `04-ia-traitement-documentaire.md` §6).
Les classements publics sont établis sur des documents anglophones propres ; ils ne prédisent
pas la performance sur un CV guinéen photographié de travers, en français, avec un diplôme local.

Corollaire de conception, à acter dès le socle : **tout appel de modèle passe par une interface
interne** (`OcrProvider`, `ExtractionProvider`, `GenerationProvider`). Changer de fournisseur,
en faire tourner deux en parallèle sur le même flux (*shadow mode*) pour comparer, ou rapatrier
le traitement sur une infrastructure propre doit être un changement de configuration, jamais une
réécriture. Cette interface est ce qui rend la stratégie « coût-efficiente » praticable dans la
durée : elle permet de rebasculer à chaque évolution du marché.

## 2. Familles de modèles candidates

### 2.1 Modèles à poids ouverts d'origine chinoise

L'intuition est juste : le rapport performance/prix de ces modèles est aujourd'hui l'un des
meilleurs du marché, et leur disponibilité en poids ouverts change la nature du choix.

| Famille | Éditeur | Intérêt pour TalVo |
|---|---|---|
| **Qwen-VL** (série vision-langage) | Alibaba | Compréhension de documents, poids ouverts, plusieurs tailles — auto-hébergeable ou via API |
| **DeepSeek** | DeepSeek | Modèles texte très compétitifs, tarification API agressive, poids ouverts |
| **GLM** | Zhipu AI | Alternative multimodale, poids ouverts |
| **MiniCPM-V** | OpenBMB | Petit multimodal, conçu pour tourner sur GPU modeste — pertinent pour un coût marginal très bas |
| **InternVL** | Shanghai AI Lab | Multimodal, poids ouverts |
| **PaddleOCR** | Baidu | **OCR pur, open source, mature, multilingue** — la référence gratuite auto-hébergeable |

### 2.2 Modèles à poids ouverts occidentaux

À ne pas écarter, pour deux raisons qui comptent ici : **Mistral** est français — donc entraîné
avec une part de français bien supérieure à la moyenne — et les licences européennes simplifient
le discours de conformité auprès de clients corporate. Llama (Meta) et Gemma (Google) complètent
le champ. Côté OCR pur : **Surya**, **docTR**, **Tesseract**.

### 2.3 API propriétaires

Claude (Anthropic), GPT (OpenAI), Gemini (Google). Plus chers au jeton, mais sans coût
d'exploitation, avec une qualité de sortie structurée généralement supérieure et aucune
infrastructure à maintenir. À conserver comme **référence haute du benchmark** : c'est l'étalon
qui dit combien on perd en descendant en gamme.

Ordre de grandeur utile, tarifs Anthropic constatés en juin 2026 (par million de jetons) :
Haiku 4.5 à 1 $ en entrée / 5 $ en sortie, Sonnet 5 à 2 $ / 10 $, Opus 5 à 5 $ / 25 $.
L'API Batch, adaptée à un traitement de CV non temps-réel, est à **moitié prix**.

### 2.4 Le point de vigilance décisif : le français

**La plupart des modèles à poids ouverts chinois sont optimisés pour le chinois et l'anglais.**
Le français — et *a fortiori* le vocabulaire des CV francophones d'Afrique de l'Ouest, les
intitulés de diplômes locaux, les noms d'employeurs guinéens — n'est pas leur terrain d'excellence
par défaut. Un OCR mal calibré sur les accents produit « experience » au lieu de « expérience »,
« Licence en gestion » au lieu de « Licence en géstion » : des erreurs **discrètes**, qui ne
lèvent aucune alerte et dégradent silencieusement le matching.

C'est précisément ce que le benchmark doit mesurer, et c'est la raison pour laquelle on ne peut
pas décider sur réputation. Un modèle « moins bon » au classement général peut être meilleur sur
le français ; un modèle excellent en anglais peut être inutilisable ici.

## 3. Économie : API ou auto-hébergement ?

### 3.1 Ordre de grandeur par CV

Estimation pour un CV de 2 pages traité par un modèle multimodal, à affiner par la mesure :
environ 4 000 à 6 000 jetons en entrée (pages en image + consigne), 1 000 à 2 000 en sortie (JSON
structuré). Sur un modèle d'entrée de gamme en mode batch, cela place le **coût unitaire aux
environs de 0,005 à 0,01 $ par CV**.

Ce qu'il faut en retenir : **à 10 000 CV par mois, la facture de modèle est de l'ordre de la
centaine de dollars.** Ce n'est pas là que se joue la rentabilité de TalVo. L'API n'est pas un
luxe au démarrage, et optimiser ce poste avant d'avoir des utilisateurs serait une erreur de
priorité.

### 3.2 Où bascule l'arbitrage

L'auto-hébergement d'un modèle à poids ouverts sur GPU loué a un **coût fixe** (la machine tourne
qu'elle serve ou non) là où l'API a un **coût variable pur**. Le point de bascule dépend donc du
volume et de la régularité de la charge — or la charge de TalVo sera **en rafales** (une campagne
de recrutement, puis le calme), ce qui est le pire profil pour un GPU dédié.

Conséquence : **l'API est le bon choix au démarrage**, et l'auto-hébergement devient pertinent
quand le volume mensuel est à la fois élevé et régulier. Le calcul se refait avec les chiffres
réels, pas maintenant.

### 3.3 Les trois raisons de s'auto-héberger qui ne sont pas le coût

1. **Souveraineté des données.** Les CV ne quittent pas ton infrastructure. C'est un argument
   commercial direct face à une banque ou un groupe minier dont la politique groupe interdit les
   transferts hors zone.
2. **Le fine-tuning** (§5) : on n'affine pas librement un modèle fermé.
3. **Indépendance tarifaire** : aucun fournisseur ne peut doubler ton coût unitaire du jour au
   lendemain.

Ces trois raisons plaident pour **garder l'option ouverte** — donc privilégier, à performance
égale au benchmark, un modèle à poids ouverts — sans pour autant s'auto-héberger dès le premier
jour.

## 4. Anti-hallucination : l'ordre des leviers

Le fine-tuning est **le dernier** levier, pas le premier. Dans l'ordre d'efficacité et de coût :

### Levier 1 — Sortie structurée contrainte
Imposer un schéma JSON au décodage. Élimine **par construction** toute une classe d'erreurs :
champ absent, type invalide, énumération inventée. Coût de mise en œuvre : quasi nul. À faire
systématiquement, sur tout fournisseur qui le propose.

### Levier 2 — L'extraction est une **sélection**, pas une génération
Règle de conception la plus importante de ce document :

> Un nom d'employeur, un intitulé de poste, une date, un diplôme **doivent exister littéralement
> dans le document source**. Le modèle ne les *rédige* pas, il les *désigne*.

On demande donc au modèle de restituer, pour chaque champ, **l'extrait source exact** en plus de
la valeur. Un post-traitement déterministe vérifie que cet extrait figure bien dans le texte du
document (comparaison tolérante aux variations d'espacement et de casse). Si l'extrait est
introuvable, le champ est rejeté ou marqué à valider — jamais accepté en silence.

La normalisation (« Power BI » → `skill:power-bi`, « Licence » → niveau 3) intervient **après**,
de manière déterministe, via le référentiel. L'IA ne normalise pas : elle désigne, le code
normalise. Cette séparation supprime la majorité du risque d'invention sans aucun fine-tuning.

### Levier 3 — Seuils de confiance et routage humain
Chaque champ porte un score de confiance. Sous un seuil, il est mis en évidence dans l'écran de
correction du candidat. Le cadrage impose déjà cette validation humaine (§8.1) : il s'agit de la
**cibler** plutôt que de tout faire relire.

### Levier 4 — Vérification d'ancrage pour la génération (CV adapté)
Pour l'adaptation de CV (Premium), le problème est différent : il y a bien génération de texte.
Le garde-fou est alors un **vérificateur d'implication** — chaque affirmation du CV produit doit
être justifiable par un élément du CV source. Les affirmations non ancrées sont supprimées ou
signalées. Le cadrage exige par ailleurs de **signaler les éléments manquants** : c'est la
soupape qui permet au modèle d'être honnête au lieu d'inventer.

### Levier 5 — Fine-tuning
Voir ci-dessous. Il améliore la précision moyenne ; **il ne garantit rien**. Un modèle affiné
hallucine moins souvent, mais il hallucine encore. Les leviers 1 à 4 sont des garanties
structurelles ; le fine-tuning est une optimisation statistique. On ne remplace jamais les
premiers par le dernier.

## 5. La place réelle du fine-tuning

Tu as raison sur le fond : affiner un modèle est devenu accessible (LoRA/QLoRA, quelques heures
de GPU, outillage mature). La difficulté n'est plus technique — **elle est dans les données**.

Un fine-tuning utile demande des milliers d'exemples annotés : document en entrée, extraction
correcte en sortie. Or TalVo possède déjà le mécanisme qui les produit : **l'écran de correction
du candidat**. Chaque correction est un couple (extraction erronée → extraction juste), c'est-à-dire
exactement la donnée d'entraînement recherchée, produite gratuitement par l'usage.

D'où la séquence, qui est aussi un calendrier :

| Étape | Quand | Contenu |
|---|---|---|
| 1 | Maintenant | Benchmark, choix d'une chaîne, leviers 1 à 4 |
| 2 | V1 → pilote | Instrumenter la correction : stocker systématiquement version extraite et version corrigée |
| 3 | Après quelques milliers de CV | Mesurer où le modèle se trompe **réellement** (quels champs, quels types de documents) |
| 4 | Ensuite | Affiner un modèle à poids ouverts **ciblé sur ces erreurs**, et le mesurer sur le même corpus |

Affiner avant l'étape 3 reviendrait à optimiser à l'aveugle. Et l'étape 4 n'est possible que si
le modèle retenu est à poids ouverts — **c'est le vrai argument en faveur des modèles ouverts,
bien avant le prix** : ils préservent une option que les API fermées ferment définitivement.

## 6. Synthèse opérationnelle

1. Abstraire les fournisseurs dès le socle — non négociable.
2. Mesurer sur le corpus TalVo avant tout choix, avec le français comme critère de premier rang.
3. Démarrer sur API (coût négligeable au volume initial), à condition de pouvoir en sortir.
4. Privilégier, à performance égale, un modèle à poids ouverts — pour le fine-tuning et la
   souveraineté, pas pour le prix.
5. Construire les garde-fous 1 à 4 dans l'architecture, pas dans les consignes envoyées au modèle.
6. Instrumenter les corrections dès la V1 : c'est le carburant du fine-tuning et l'actif de long terme.
