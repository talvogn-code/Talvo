# TalVo — Décisions techniques

Statut : **à valider**. Ce document confronte l'architecture recommandée par le cadrage aux
contraintes réelles du projet (équipe, calendrier, hébergement) et propose un choix.

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

## 3. Recommandation

**Option A ou C selon la réponse à une seule question : qui maintiendra le code après la V1 ?**

- Équipe backend Node en place, app mobile ferme à moyen terme → **Option B** (le cadrage a raison).
- Petite équipe, objectif « pilote en janvier 2027 » → **Option A**, avec Postgres managé
  (Supabase/Neon) et migrations SQL versionnées. On garde l'API sous `/api` structurée en modules
  pour pouvoir l'extraire en NestJS plus tard sans réécrire la logique métier.
- Besoin de livrer vite **et** de s'appuyer sur RLS pour les règles de confidentialité → **Option C**.

Dans les trois cas, ces points ne changent pas et peuvent être actés dès maintenant :
- **PostgreSQL**, migrations SQL versionnées dans le dépôt.
- **TypeScript de bout en bout**, Tailwind pour l'UI.
- Le **moteur de matching est un module pur** (entrées : profil + offre ; sortie : score + breakdown),
  sans dépendance au framework HTTP ni à l'ORM. C'est la pièce la plus testable et la plus durable
  du produit : elle doit survivre à un changement de stack.
- **Recherche** : PostgreSQL Full Text (`tsvector` + GIN) et `pg_trgm`, pas de moteur externe.
- **Stockage des CV** : objet S3-compatible, URLs signées, jamais d'accès public direct.

## 4. Sujets à trancher hors stack

1. **Parsing de CV (PDF/DOCX)** — brique la plus risquée du périmètre P0. Les CV guinéens sont
   souvent des PDF scannés ou des mises en page Word atypiques. Options : bibliothèque locale
   (`pdf-parse`/`mammoth`) + correction manuelle obligatoire · service de parsing spécialisé ·
   extraction assistée par LLM avec validation par le candidat. Le cadrage impose déjà la
   correction manuelle (§8.1), ce qui est la bonne garantie quel que soit le choix.
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
périmètre MVP validé, règles métier, architecture, backlog. Les trois premiers sont couverts par
`docs/00` à `docs/02` ; l'architecture est ce document, en attente d'arbitrage.

Prochain jalon : **Oct. 2026 — UX/UI** (maquettes, design system, parcours candidat et entreprise).
