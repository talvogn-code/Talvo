# TalVo — instructions de travail

Plateforme guinéenne de recrutement : sourcing, présélection et évaluation des talents.
Cible V1 pilote : **janvier 2027**, 5 à 10 entreprises à Conakry.

## Ce projet est conduit par les specs

**Ne jamais écrire de code applicatif sans spec approuvée.** Lire `CONTRIBUTING.md` avant
toute contribution, et la spec concernée avant d'écrire une ligne.

Avant d'implémenter :
1. Lire la spec dans `specs/` et vérifier qu'elle est `approuvée`.
2. Écrire les tests des critères d'acceptation (`CA-x`) avant le code.
3. Citer la spec et les critères couverts dans le message de commit et la PR.

Si la spec est ambiguë ou incomplète : **modifier la spec d'abord**, en PR séparée. Ne jamais
combler un trou de spec par une décision prise dans le code.

## Carte des documents

| Fichier | Rôle |
|---|---|
| `docs/00-cadrage-mvp.md` | Cahier des charges fonctionnel — source de vérité produit |
| `docs/01-modele-donnees.md` | Modèle de données |
| `docs/02-moteur-matching.md` | Spécification du moteur de classement |
| `docs/04-ia-traitement-documentaire.md` | Chaîne de lecture des CV |
| `docs/05-strategie-modeles-ia.md` | Choix de modèles et garde-fous anti-hallucination |
| `docs/07-angles-morts.md` | Sujets absents du cadrage |
| `docs/09-jalons.md` | Jalons et critères de sortie |
| `docs/10-registre-exigences.md` | Registre des exigences (`EXI-xxx`, `NFR-xxx`) |
| `docs/adr/` | Décisions techniques |
| `specs/` | Spécifications |

## Règles invariantes du domaine

Elles viennent du cahier des charges et ne se négocient pas dans le code :

1. Une entreprise doit être **validée** avant de publier une offre publique.
2. Le **nom de l'entreprise est masqué** aux candidats en offre gratuite.
3. Un CV adapté ne peut contenir **que des informations présentes** dans le profil ou le CV
   source. **Interdiction d'inventer** une compétence, un diplôme ou une expérience.
4. Un candidat n'est **jamais** présenté comme ayant passé un test qu'il n'a pas réalisé.
5. Les notes internes du recruteur restent **privées**.
6. Les profils sourcés sans candidature sont présentés dans un **espace distinct**.
7. Un score de matching est une **aide à la décision**, jamais une décision automatique.
8. Toute action de modération ou de modification importante est **journalisée**.

## Règles d'ingénierie

- **L'extraction est une sélection, pas une génération.** Un employeur, une date, un diplôme
  doivent exister littéralement dans le document source ; le modèle désigne un extrait, le code
  normalise ensuite via le référentiel. Un champ non ancré est rejeté ou marqué à valider,
  jamais accepté en silence.
- **Le chronomètre des tests fait autorité côté serveur.** Aucune confiance dans le client.
- **Chaque réponse à un test est enregistrée immédiatement** et la tentative reprend après une
  coupure réseau.
- **Fournisseurs externes derrière des interfaces internes** (`OcrProvider`,
  `ExtractionProvider`) — jamais d'appel direct depuis la logique métier.
- **Migrations en expansion puis contraction.** Une migration et le code qui l'utilise ne
  partent jamais dans le même déploiement.
- **Le moteur de matching est un module pur** : entrées profil + offre, sortie score +
  `breakdown`. Aucune dépendance au framework HTTP ni à l'ORM.
- **Aucune donnée de production** dans un autre environnement.

## Conventions

- Documents, specs, commits, interface : **français**. Identifiants de code, tables, champs,
  API : **anglais**.
- Aucun texte destiné à l'utilisateur écrit en dur dans le code.
- Multi-pays dès le modèle de données, même avec un seul pays ouvert.
- Dates stockées en UTC, affichées en heure locale.
