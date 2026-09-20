# TalVo — Moteur de matching V1 (spécification)

Contrainte fondatrice du cadrage : **le moteur doit rester explicable et maîtrisable**.
TalVo doit pouvoir répondre à « pourquoi ce profil est-il classé 3e ? » avec une phrase, pas
avec un modèle opaque. La V1 est donc un moteur **à règles pondérées**, déterministe et versionné.
L'IA viendra enrichir ce socle, pas le remplacer.

## 1. Score global

```
total = 0.35 × S_compétences
      + 0.30 × S_expérience
      + 0.15 × S_fonction
      + 0.10 × S_formation
      + 0.10 × S_localisation
```

Chaque sous-score est normalisé sur `[0, 100]`. `total` ∈ `[0, 100]`.
Les poids sont **configurables** (table de configuration + `algorithm_version` sur `match_scores`),
pas codés en dur : les ajuster après le pilote est explicitement prévu (« Fév. 2027 — amélioration
matching »).

## 2. Sous-scores

### 2.1 Compétences — 35 %

```
S_compétences = 100 × ( Σ poids(compétence requise trouvée) / Σ poids(toutes compétences requises) )
```
- `required` → poids 1,0 · `nice_to_have` → poids 0,4.
- Correspondance via `skills.slug` + `skills.aliases` (normalisation, casse et accents ignorés).
- Si `job_skills.min_years` est renseigné et que le candidat a moins d'années sur cette compétence,
  la compétence compte pour moitié.
- **Sortie explicable** : liste des compétences trouvées, liste des manquantes.

### 2.2 Expérience — 30 %

Deux composantes à parts égales :
- **Volume** : `min(100, 100 × années_totales / experience_min_years)` de l'offre
  (100 si l'offre n'exige rien).
- **Pertinence** : part des années passées sur une `job_function` ou un `sector` proche de l'offre.

```
S_expérience = 0.5 × volume + 0.5 × pertinence
```
- **Sortie explicable** : « 4 ans dont 3 en Data Analyst (secteur Banque) — requis : 2 ans ».

### 2.3 Intitulé / fonction — 15 %

- 100 si `job_function_id` identique entre le titre courant du candidat et l'offre.
- 60 si la fonction appartient à la même famille métier.
- Sinon, similarité textuelle (trigram `pg_trgm`) entre `professional_title` et `jobs.title`,
  ramenée sur `[0, 60]`.

### 2.4 Formation — 10 %

- Niveau : 100 si `education_level` ≥ `education_level_min`, 50 si un cran en dessous, 0 au-delà.
- Domaine : bonus si `field_of_study` correspond au secteur/fonction de l'offre.
- Si l'offre n'exige aucun niveau : 100.

### 2.5 Localisation / mobilité — 10 %

- 100 : même ville.
- 80 : même région, ou candidat `willing_to_relocate`.
- 60 : offre en remote.
- 20 : autre région sans mobilité déclarée.

## 3. Tests

Les scores de tests **n'entrent pas** dans les 100 % ci-dessus : ils constituent un **filtre et un
second axe de tri**, conformément au workflow §10.4 (« application des critères de tests lorsqu'ils
sont requis », après le calcul du score).

Pour une offre avec `tests_required = true` :
1. Le score de correspondance classe les candidatures.
2. Les candidats sont invités aux tests (`job_tests`).
3. À l'échéance, les candidats sous `job_tests.min_score` sur un test `is_mandatory` sont **écartés
   de la shortlist** (pas de la liste des candidatures).
4. Le tri de la shortlist devient : `(a réussi les tests obligatoires) DESC, moyenne tests DESC, total DESC`.

Un candidat qui n'a pas passé le test n'est jamais affiché comme l'ayant passé (règle 4) : son état
est `invited` ou `expired`, distinct de « échoué ».

## 4. Sourcing (profils n'ayant pas postulé)

Même moteur, population différente :
- candidats avec `is_searchable = true` ;
- n'ayant **pas** de `application` sur cette offre ;
- `total ≥ seuil_sourcing` (défaut : 60, configurable) ;
- limités aux N meilleurs (défaut : 20).

Résultat écrit dans `sourced_candidates`, affiché dans un **espace distinct** des candidatures
(règle 6, écran 16 « Profils sourcés »).

## 5. Explicabilité — contrat de sortie

Chaque `match_scores.breakdown` (jsonb) contient au minimum :

```json
{
  "algorithm_version": "v1.0",
  "weights": { "skills": 0.35, "experience": 0.30, "title": 0.15, "education": 0.10, "location": 0.10 },
  "skills":    { "score": 82, "matched": ["SQL", "Excel"], "missing": ["Power BI"], "partial": [] },
  "experience":{ "score": 75, "total_years": 4, "relevant_years": 3, "required_years": 2 },
  "title":     { "score": 100, "candidate": "Data Analyst", "job": "Data Analyst", "rule": "exact_function" },
  "education": { "score": 100, "level": "licence", "required": "licence", "field_match": true },
  "location":  { "score": 80, "rule": "same_region", "candidate": "Kindia", "job": "Conakry" }
}
```

La fiche candidat (§12.3) rend ce JSON en langage naturel. Aucun score ne doit être affiché sans
son « pourquoi ».

## 6. Garde-fous

- Le score est une **aide à la décision**, jamais une décision d'embauche automatique (règle 7).
  L'interface doit le formuler explicitement et ne jamais présenter de rejet automatique.
- Aucun critère de tri ne doit encoder d'attribut discriminatoire (âge, genre, origine, situation
  familiale). Ces champs ne doivent pas exister dans le profil de matching.
- Toute modification des poids est un **changement de `algorithm_version`** et est journalisée
  (`audit_logs`) : on doit pouvoir rejouer le classement d'une offre passée.
- Le recalcul est déclenché à : publication/modification d'offre, nouvelle candidature, mise à jour
  du CV primaire, résultat de test. Idempotent, rejouable en lot.

## 7. Ce que la V1 ne fait pas

Embeddings sémantiques · apprentissage sur les décisions des recruteurs · scoring des soft skills ·
parsing par LLM comme seule source du profil (le parsing d'import reste corrigible à la main, §8.1).
