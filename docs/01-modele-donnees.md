# TalVo — Modèle de données (brouillon V1)

Dérivé de la section 15 du cadrage. Notation neutre (SQL/PostgreSQL), indépendante de l'ORM retenu.
`id` = UUID v4 partout. Toutes les tables portent `created_at` / `updated_at`.

## Vue d'ensemble

```
User ─┬─< CandidateProfile ─┬─< Resume ─┬─< Experience
      │                     │           ├─< Education
      │                     │           └─< ResumeSkill >─ Skill
      │                     ├─< Application >─ Job
      │                     ├─< TestAttempt >─ Test ─< Question
      │                     ├─< MatchScore >─ Job
      │                     └─< SourcedCandidate >─ Job
      ├─< CompanyProfile ───< Job ─< JobSkill >─ Skill
      ├─< Subscription
      ├─< Notification
      └─< Message
```

## Comptes et accès

### `users`
| Colonne | Type | Notes |
|---|---|---|
| id | uuid PK | |
| email | citext UNIQUE | |
| password_hash | text | selon la stratégie d'auth retenue |
| role | enum | `candidate`, `company`, `agency`, `admin` |
| status | enum | `pending`, `active`, `suspended` |
| email_verified_at | timestamptz NULL | |
| last_login_at | timestamptz NULL | |

> Le statut Premium n'est **pas** un rôle : il découle d'un `subscriptions` actif (règle 2 du cadrage).

### `candidate_profiles`
`id`, `user_id` FK UNIQUE, `first_name`, `last_name`, `phone`, `professional_title`,
`summary`, `city`, `region`, `willing_to_relocate` bool, `years_experience` int,
`education_level` enum, `sector` FK→`sectors`, `availability` enum,
`completeness_score` int (0–100, calculé), `is_searchable` bool (consentement sourcing).

> `is_searchable` matérialise le consentement du candidat à apparaître dans les **profils sourcés**
> (règles 6 et 8). Sans ce flag, le profil n'entre pas dans le vivier proposé aux recruteurs.

### `company_profiles`
`id`, `user_id` FK UNIQUE, `name`, `type` enum (`company`, `agency`), `sector` FK→`sectors`,
`size` enum, `description`, `logo_url`, `website`, `address`, `rccm_number` (registre du commerce),
`verification_status` enum (`pending`, `verified`, `rejected`), `verified_at`, `verified_by` FK→`users`.

> Règle 1 : `verification_status = 'verified'` est un **prérequis à la publication** d'une offre publique.

## Référentiels

- `skills` : `id`, `name`, `slug` UNIQUE, `category`, `aliases` text[] — le dictionnaire de compétences
  normalisé (admin). Les alias servent au matching (« Power BI » / « PowerBI » / « MS Power BI »).
- `sectors` : `id`, `name`, `slug` — Banque, Mines, Télécoms, ONG, …
- `job_functions` : `id`, `name`, `slug`, `aliases` text[] — Data Analyst, Comptable, Ingénieur, …

> Ces trois référentiels sont la **condition du matching explicable** : sans normalisation, le score
> n'est pas reproductible. Leur gestion est un écran admin P0 de fait, même si le cadrage la liste
> au module Administration.

## CV

### `resumes`
`id`, `candidate_id` FK, `source` enum (`imported`, `builder`, `adapted`), `title`,
`template` (pour les CV builder), `file_url` (original importé), `parsed_at`, `is_primary` bool,
`parent_resume_id` FK NULL (CV adapté → CV source), `target_job_id` FK NULL (CV adapté → offre).

### `experiences`
`id`, `resume_id` FK, `company_name`, `job_title`, `job_function_id` FK NULL, `sector_id` FK NULL,
`location`, `start_date`, `end_date` NULL, `is_current` bool, `description`, `order_index`.

### `educations`
`id`, `resume_id` FK, `school`, `degree`, `field_of_study`, `level` enum, `start_date`, `end_date`, `description`.

### `resume_skills`
`resume_id` FK, `skill_id` FK, `level` enum NULL, `years` int NULL — PK composite.

### `languages`, `certifications`
Rattachées à `resume_id`, structure simple (`name`, `level` / `issuer`, `issued_at`, `credential_url`).

## Offres et candidatures

### `jobs`
`id`, `company_id` FK, `title`, `description`, `job_function_id` FK, `sector_id` FK,
`city`, `region`, `remote_policy` enum, `contract_type` enum (`cdi`, `cdd`, `stage`, `mission`),
`experience_min_years` int, `education_level_min` enum NULL, `deadline` date,
`status` enum (`draft`, `published`, `paused`, `archived`), `published_at`,
`tests_required` bool, `test_deadline_days` int NULL, `search_vector` tsvector (index GIN).

### `job_skills`
`job_id` FK, `skill_id` FK, `weight` enum (`required`, `nice_to_have`), `min_years` int NULL — PK composite.

> La distinction `required` / `nice_to_have` est nécessaire pour que les 35 % « compétences » soient
> calculables ; le cadrage donne le poids global mais pas sa répartition interne.

### `job_tests`
`job_id` FK, `test_id` FK, `is_mandatory` bool, `min_score` int NULL — PK composite.

### `applications`
`id`, `job_id` FK, `candidate_id` FK, `resume_id` FK, `cover_letter` text NULL,
`status` enum (`submitted`, `screening`, `test_pending`, `test_done`, `shortlisted`,
`interview`, `rejected`, `hired`), `applied_at`, `status_changed_at`.
UNIQUE (`job_id`, `candidate_id`).

> La suite de `status` est le **mini-ATS / pipeline** (P1). La modéliser dès la V1 évite une migration
> lourde en mars ; seuls les écrans arrivent plus tard.

### `application_notes`
`id`, `application_id` FK, `author_id` FK→`users`, `body`, `created_at` — **privé recruteur** (règle 5).

## Matching, sourcing, shortlist

### `match_scores`
`id`, `job_id` FK, `candidate_id` FK, `total_score` numeric(5,2),
`skills_score`, `experience_score`, `title_score`, `education_score`, `location_score` numeric(5,2),
`breakdown` jsonb, `algorithm_version` text, `computed_at`.
UNIQUE (`job_id`, `candidate_id`, `algorithm_version`).

> `breakdown` stocke les éléments ayant conduit au score (compétences trouvées/manquantes, années
> retenues, etc.) : c'est ce qui alimente le « résumé des éléments ayant conduit au score » de la
> fiche candidat (§12.3) et ce qui rend le moteur **explicable** (contrainte V1).
> `algorithm_version` permet de recalculer sans écraser l'historique et de comparer deux jeux de poids.

### `sourced_candidates`
`id`, `job_id` FK, `candidate_id` FK, `match_score_id` FK, `status` enum (`suggested`,
`contacted`, `dismissed`), `surfaced_at`, `surfaced_by` enum (`engine`, `admin`).
UNIQUE (`job_id`, `candidate_id`).

> Table **distincte** de `applications` : règle 6 (espace séparé côté recruteur).

### `shortlists` / `shortlist_items`
`shortlists` : `id`, `job_id` FK, `created_by` FK→`users`, `status` enum (`draft`, `sent`), `sent_at`, `note`.
`shortlist_items` : `id`, `shortlist_id` FK, `candidate_id` FK, `application_id` FK NULL,
`sourced_candidate_id` FK NULL, `rank` int, `justification` text.

## Tests

### `tests`
`id`, `name`, `slug`, `category` enum (`technical`, `logic`, `language`), `skill_id` FK NULL,
`description`, `duration_minutes` int, `question_count` int, `pass_threshold` int,
`status` enum (`draft`, `published`, `archived`).

Catalogue initial : Excel, SQL, Power BI, Agile/Scrum, PHP, React, Logique, Français, Anglais.

### `questions`
`id`, `test_id` FK, `body`, `type` enum (`single_choice`, `multiple_choice`, `true_false`),
`difficulty` enum, `points` int, `explanation` text NULL, `order_index`.

### `question_options`
`id`, `question_id` FK, `body`, `is_correct` bool, `order_index`.

> `is_correct` ne doit **jamais** traverser l'API côté candidat pendant une tentative.

### `test_attempts`
`id`, `test_id` FK, `candidate_id` FK, `origin` enum (`company_request`, `self_certification`),
`job_id` FK NULL, `application_id` FK NULL, `invited_at`, `expires_at`, `started_at`,
`submitted_at`, `status` enum (`invited`, `in_progress`, `submitted`, `expired`).

> `origin` matérialise la §11.3 : les tests demandés par une entreprise sont **distincts** des tests
> de certification volontaire.

### `attempt_answers`
`id`, `attempt_id` FK, `question_id` FK, `selected_option_ids` uuid[], `is_correct` bool, `answered_at`.

### `test_results`
`id`, `attempt_id` FK UNIQUE, `score` numeric(5,2), `max_score`, `percentage`,
`level` enum (`beginner`, `intermediate`, `advanced`), `passed` bool, `computed_at`.

> Règle 4 : aucun résultat sans `test_attempt` au statut `submitted`. Règle 9 : `computed_at` +
> lien vers une tentative identifiable.

### `skill_badges`
`id`, `candidate_id` FK, `skill_id` FK, `test_result_id` FK, `percentage`, `level`, `earned_at`,
`is_public` bool. (Ex. *Excel — 87 % — Niveau avancé*.)

## Messagerie, abonnements, transverse

- `conversations` : `id`, `job_id` FK NULL, `company_id` FK, `candidate_id` FK, `last_message_at`.
- `messages` : `id`, `conversation_id` FK, `sender_id` FK→`users`, `body`, `read_at`.
- `subscriptions` : `id`, `user_id` FK, `plan` enum (`candidate_premium`, `company_basic`,
  `company_pro`), `period` enum (`monthly`, `yearly`), `status` enum (`active`, `past_due`,
  `canceled`), `started_at`, `current_period_end`, `canceled_at`.
  → **Source de vérité du statut Premium** (règle 2, visibilité du nom d'entreprise).
- `notifications` : `id`, `user_id` FK, `type`, `payload` jsonb, `read_at`.
- `audit_logs` : `id`, `actor_id` FK→`users` NULL, `action`, `entity_type`, `entity_id`,
  `before` jsonb, `after` jsonb, `ip`, `created_at` (règle 10).

## Points à trancher

1. **Profil vs CV** — les expériences/formations sont-elles portées par le CV (`resume_id`, modèle
   ci-dessus) ou par le profil candidat, le CV n'en étant qu'une vue ? Le cadrage laisse les deux
   lectures ouvertes. Le modèle ci-dessus attache au CV et considère le CV primaire comme la source
   du matching ; l'alternative (profil = source, CV = rendu) simplifie le matching mais complique
   l'import multi-CV.
2. **Granularité du consentement sourcing** — un simple booléen `is_searchable`, ou un opt-out par
   secteur/entreprise ?
3. **Rétention des résultats de tests** — durée de validité d'un badge de compétence (re-test après
   12 / 24 mois ?). Non traité par le cadrage.
