# TalVo — Décisions techniques

> **Statut : arbitrage suspendu.** Ce document a été rédigé avant l'analyse de la chaîne de
> traitement documentaire. Or c'est cette chaîne — et non les préférences de framework — qui
> contraint l'infrastructure. Voir `04-ia-traitement-documentaire.md` : la charge IDP impose
> des traitements longs, par rafales, avec workers élastiques, ce qui **disqualifie une approche
> entièrement serverless orientée requête/réponse comme point de départ**, et relativise
> l'opposition « une app » vs « deux apps » ci-dessous.
>
> Aucun choix de fournisseur n'est arrêté. La décision attend les mesures du §6 de ce document-là.

Ce document confronte l'architecture recommandée par le cadrage aux contraintes de projet
(équipe, calendrier, hébergement) et inventorie les options.

## 1. Ce que dit le cadrage (§14)

| Composant | Choix recommandé |
|---|---|
| Frontend | React + TypeScript + Tailwind CSS |
| Backend | Node.js + NestJS |
| Base de données | PostgreSQL |
| ORM | Prisma |
| Authentification | JWT + refresh token |
| Stockage CV | Stockage objet S3-compatible |
| Recherche | PostgreSQL Full Text au MVP |
| Moteur de matching | Service backend dédié + règles pondérées ; IA en évolution |
| Tests | Moteur de questionnaire avec timer, scoring, banque de questions |
| Email | Service transactionnel |
| Déploiement | Docker + CI/CD |

Ces choix sont sains et sans surprise. La seule question ouverte est le **découpage** :
deux applications (SPA React + API NestJS) ou une seule application full-stack.

## 2. Options

### Option A — Next.js (App Router) + PostgreSQL managé
Une seule application TypeScript : rendu serveur, routes API, jobs de matching.
- **+** Un seul dépôt, un seul déploiement, un seul langage ; SEO natif sur la landing et les pages
  d'offres publiques (§14, écrans 01 et 10) ; time-to-market le plus court ; déploiement trivial.
- **+** Le SEO des pages d'offres n'est pas un détail : c'est le canal d'acquisition des candidats.
- **−** S'écarte de la lettre du cadrage (NestJS). Le moteur de matching en tâche de fond demande
  une file de jobs externe si les volumes montent.

### Option B — React (Vite) + API NestJS séparée
Exactement ce que décrit le cadrage.
- **+** Séparation nette, API réutilisable par une future app mobile (P2), structure familière pour
  une équipe backend Node ; le service de matching a sa place naturelle.
- **−** Deux déploiements, deux CI, CORS, auth à câbler des deux côtés ; SPA = SEO à traiter à part
  (pré-rendu ou vitrine séparée) ; plus lent à livrer pour janvier 2027.

### Option C — Next.js + Supabase (Postgres + Auth + Storage managés)
- **+** Auth, stockage objet et Postgres fournis d'emblée ; RLS au niveau base, ce qui sert
  directement les règles 2, 5, 6 et 8 (visibilité entreprise, notes privées, consentement sourcing) ;
  la vitesse de mise en place la plus élevée.
- **−** Dépendance à un fournisseur ; la logique d'autorisation part en policies SQL, à tester
  sérieusement ; l'auth JWT + refresh du cadrage est déléguée.

## 3. Lecture des options à la lumière de la charge documentaire

Les trois options ci-dessus portent sur la **couche web**. Elles sont secondaires : quelle que
soit celle retenue, il faut de toute façon une **file de travaux et un pool de workers** pour
l'IDP, le matching et la génération de PDF (voir `04-ia-traitement-documentaire.md` §4). C'est
cette partie-là qui détermine l'hébergement, le coût et la capacité à monter en charge.

Conséquences :
- L'option C telle qu'écrite ci-dessus (plateforme managée tout-en-un) **ne couvre pas** le
  besoin de calcul long et élastique. Elle n'est pas retenue comme point de départ.
- Le débat « une app vs deux apps » reste ouvert et n'est pas urgent : il n'engage ni le modèle
  de données, ni le moteur de matching, ni la chaîne documentaire, qui sont les trois pièces
  réellement coûteuses à refaire.
- Le critère décisif reste **qui maintiendra la plateforme après la V1**, et cette réponse n'a
  pas encore été instruite.

Ces points, en revanche, ne dépendent d'aucune option et peuvent être actés dès maintenant :
- **PostgreSQL**, migrations SQL versionnées dans le dépôt.
- **TypeScript de bout en bout**, Tailwind pour l'UI.
- Le **moteur de matching est un module pur** (entrées : profil + offre ; sortie : score + breakdown),
  sans dépendance au framework HTTP ni à l'ORM. C'est la pièce la plus testable et la plus durable
  du produit : elle doit survivre à un changement de stack.
- **Recherche** : PostgreSQL Full Text (`tsvector` + GIN) et `pg_trgm`, pas de moteur externe.
- **Stockage des CV** : objet S3-compatible, URLs signées, jamais d'accès public direct.
- **Traitements asynchrones** : file de travaux + workers dès le socle. Toute la chaîne
  documentaire, le recalcul de matching et la génération de PDF y passent.
- **Fournisseurs d'IA abstraits** derrière des interfaces internes (`OcrProvider`,
  `ExtractionProvider`), pour pouvoir comparer, basculer ou rapatrier sans réécriture.
- **Modèle de données multi-pays** dès la V1, même avec un seul pays ouvert.

## 4. Sujets à trancher hors stack

1. **Parsing de CV (PDF/DOCX)** — brique la plus risquée du périmètre P0, traitée en profondeur
   dans `04-ia-traitement-documentaire.md`. À décider sur mesures, pas sur catalogue fournisseur.
2. **Génération du PDF de CV** — rendu serveur (Puppeteer/Chromium) ou bibliothèque
   (`@react-pdf/renderer`). Contrainte : plusieurs modèles, accents français corrects.
3. **Email transactionnel** — délivrabilité vers les boîtes guinéennes à vérifier ;
   prévoir un canal SMS/WhatsApp pour les invitations aux tests (le cadrage le place post-MVP,
   mais l'invitation au test est un point de rupture du tunnel).
4. **Paiement** — Premium et B2B. Le cadrage autorise la facturation manuelle des pilotes. Les
   moyens de paiement locaux (Orange Money, MTN MoMo) pèseront plus qu'une carte bancaire pour
   le Premium candidat ; à arbitrer avant mars 2027.
5. **Hébergement et données personnelles** — localisation des données, durée de conservation,
   politique de consentement. À formaliser avant le pilote (règle 8).

## 5. Calendrier — état au 20 septembre 2026

Nous sommes dans la fenêtre **« Sept. 2026 — Cadrage »**. Livrables attendus de cette phase :
périmètre MVP validé, règles métier, architecture, backlog. Les deux premiers sont couverts par
`docs/00` à `docs/02`. L'architecture reste ouverte : elle dépend des mesures du corpus CV
(`04-ia-traitement-documentaire.md` §6), qui peuvent être menées **pendant** la phase UX/UI
d'octobre sans décaler le planning.

Prochain jalon : **Oct. 2026 — UX/UI** (maquettes, design system, parcours candidat et entreprise).
