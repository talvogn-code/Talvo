---
id: SPEC-003
titre: Import et lecture des CV
statut: en revue
version: 0.2
jalon: M2
priorite: P0
exigences: [EXI-CV-01, EXI-CV-02, EXI-CV-03, EXI-CV-04, EXI-CV-05, EXI-CV-06, NFR-03, NFR-04, NFR-07, NFR-15]
depend_de: [SPEC-001, SPEC-013]
auteur: ""
derniere_maj: 2026-09-23
---

# SPEC-003 — Import et lecture des CV

## 1. Objectif

Transformer un document déposé par un candidat — PDF natif, PDF scanné, DOCX ou photographie —
en un profil structuré **exploitable par le moteur de classement**, sans jamais enregistrer une
information qui ne figure pas dans le document.

C'est la brique dont dépend toute la valeur du produit : si elle produit du bruit, le classement
porte sur du bruit et la shortlist n'a aucune valeur commerciale.

## 2. Hors périmètre

Création d'un CV dans TalVo (`SPEC-004`) · adaptation d'un CV à une offre (`SPEC-017`) ·
choix du fournisseur d'OCR ou d'extraction (`ADR-004`). **Cette spec est délibérément
indépendante du fournisseur** : elle décrit le comportement attendu, pas l'outil.

## 3. Déclencheur

Un candidat authentifié dépose un fichier depuis son téléphone ou son ordinateur.

## 4. Parcours nominal

1. Le candidat choisit un fichier ou photographie son CV.
2. Le fichier est envoyé **directement au stockage objet** par une URL signée à durée courte —
   il ne transite pas par l'application.
3. Le système répond immédiatement : le document est reçu, l'analyse est en cours.
   **Le candidat n'attend pas.**
4. Un traitement asynchrone enchaîne : triage, extraction ou reconnaissance de texte, extraction
   structurée, vérification d'ancrage, normalisation.
5. Le candidat est notifié quand le profil proposé est prêt.
6. Il relit, corrige ce qui est faux, valide.
7. Le profil devient exploitable par le classement.

## 5. Règles métier

### Dépôt et sécurité
- **RG-1** — Formats acceptés : PDF, DOCX, JPEG, PNG. Le type est déterminé par le **contenu**,
  jamais par l'extension.
- **RG-2** — Taille maximale 15 Mo, 10 pages. Au-delà, refus explicite et compréhensible.
- **RG-3** — Tout fichier est analysé par un antivirus avant traitement. Un fichier suspect est
  mis en quarantaine, le candidat informé, l'événement journalisé.
- **RG-4** — Les fichiers ne sont jamais servis publiquement. Toute lecture passe par une URL
  signée valable 15 minutes au plus.
- **RG-5** — Le document d'origine est **conservé** : il est la seule source de vérité, toute
  extraction en est dérivée et jetable.

### Triage
- **RG-6** — Un PDF est considéré comme natif si l'extraction directe produit un texte
  significatif ; sinon il est traité comme une image.
- **RG-7** — L'analyse de mise en page est **obligatoire** dans les deux branches. Une extraction
  linéaire sur un CV à deux colonnes entrelace les colonnes et détruit le sens : cette sortie doit
  être détectée et refusée plutôt que transmise.

### Extraction — la règle centrale
- **RG-8** — L'extraction est une **sélection**, pas une génération. Pour chaque champ extrait,
  le système produit la valeur **et l'extrait source exact** dont elle provient.
- **RG-9** — Un extrait source qui ne se retrouve pas dans le texte du document — comparaison
  tolérante à la casse, aux accents et aux espaces — invalide le champ. Le champ est alors marqué
  `à valider`, jamais enregistré comme certain.
- **RG-10** — La normalisation est **déterministe et postérieure** : le modèle désigne, le code
  normalise via le référentiel (`SPEC-013`). Le modèle ne produit jamais directement un
  identifiant de compétence ou de diplôme.
- **RG-11** — Chaque champ porte un indice de confiance et sa provenance (page, position).
- **RG-12** — La sortie du modèle est contrainte par un schéma. Une sortie non conforme est
  rejetée et retentée une fois, puis le document part en revue manuelle.

### Correction
- **RG-13** — Les champs `à valider` et de faible confiance sont mis en évidence en premier.
- **RG-14** — Toute correction est enregistrée avec la valeur extraite **et** la valeur corrigée.
  Ce couple constitue le jeu de données d'entraînement de TalVo.
- **RG-15** — Tant que le candidat n'a pas validé, le profil est `incomplet` et n'entre pas dans
  le vivier proposé aux recruteurs.

### Reprise et versions
- **RG-16** — Chaque traitement porte la version de la chaîne et du modèle utilisés, et est
  **rejouable** sur le document d'origine sans nouveau dépôt.
- **RG-17** — Un échec de traitement est réessayé deux fois avec attente croissante, puis marqué
  en échec avec un message actionnable pour le candidat.
- **RG-18** — Les appels aux fournisseurs passent par `OcrProvider` et `ExtractionProvider`.
  Aucun appel direct depuis la logique métier.

## 6. Modèle de données

`resumes` (+ `source`, `file_url`, `parsed_at`, `pipeline_version`, `model_version`,
`status`) · `experiences`, `educations`, `resume_skills`, `languages`, `certifications`
(+ `source_excerpt`, `confidence`, `page`, `bbox`, `needs_review` sur chaque enregistrement
extrait) · `extraction_jobs` · `extraction_corrections` (valeur extraite, valeur corrigée,
horodatage).

## 7. Interfaces

Écrans 04 (profil) et 05 (mes CV), plus un écran de correction non listé au cahier des charges
et à ajouter. Travail asynchrone `extraction.process_resume`. Événement `resume.parsed` qui
déclenche le recalcul des scores.

## 8. Critères d'acceptation

- **CA-1** — Étant donné un PDF natif sur une colonne, quand il est déposé, alors expériences,
  formations et compétences sont extraites, chacune avec son extrait source.
- **CA-2** — Étant donné un PDF sur deux colonnes, quand il est traité, alors l'ordre de lecture
  respecte les colonnes et non le flux brut du fichier.
- **CA-3** — Étant donné un PDF scanné sans couche texte, quand il est déposé, alors la branche
  de reconnaissance optique est empruntée et le profil est produit.
- **CA-4** — Étant donné une photographie de CV légèrement inclinée, quand elle est déposée,
  alors le traitement aboutit ou échoue **avec un message expliquant comment reprendre la photo**.
- **CA-5** — Étant donné une valeur extraite dont l'extrait source est introuvable dans le
  document, quand la vérification s'exécute, alors le champ est marqué `à valider` et n'est pas
  enregistré comme certain.
- **CA-6** — Étant donné un document dont l'extension est `.pdf` mais dont le contenu est un
  exécutable, quand il est déposé, alors il est refusé au triage.
- **CA-7** — Étant donné un fichier de 40 Mo, quand il est déposé, alors il est refusé avant tout
  traitement et aucun appel payant n'est effectué.
- **CA-8** — Étant donné un dépôt, quand le candidat consulte son écran, alors il obtient une
  réponse en moins de deux secondes, sans attendre la fin de l'analyse.
- **CA-9** — Étant donné un profil extrait, quand le candidat corrige un champ, alors le couple
  valeur extraite / valeur corrigée est enregistré.
- **CA-10** — Étant donné un profil non validé par son candidat, quand un recruteur consulte les
  profils sourcés, alors ce profil n'y figure pas.
- **CA-11** — Étant donné une nouvelle version de la chaîne, quand elle est déployée, alors un
  document déjà traité peut être rejoué sans nouveau dépôt.
- **CA-12** — Étant donné le corpus d'évaluation, quand la chaîne est exécutée dessus, alors
  l'exactitude par champ dépasse le seuil enregistré, sinon l'intégration continue échoue.

## 9. Cas limites

CV de huit pages très verbeux · CV en anglais · CV sans dates · dates au format ambigu ·
deux expériences simultanées · fichier corrompu · fichier protégé par mot de passe · document
qui n'est pas un CV · même CV déposé deux fois · coupure réseau pendant l'envoi.

## 10. Exigences non fonctionnelles

`NFR-03` sécurité des dépôts · `NFR-04` URLs signées · `NFR-07` 95 % traités en moins de trois
minutes · `NFR-15` fournisseurs derrière une interface.

## 11. Télémétrie

`cv.depose` (type, taille, source), `cv.triage` (branche empruntée), `cv.extrait`
(durée, coût, version, champs extraits, champs à valider), `cv.echec` (motif),
`cv.corrige` (champ, distance entre extrait et corrigé), `cv.valide`.

> `cv.corrige` est le signal le plus précieux du produit : il mesure la qualité réelle de la
> chaîne et constitue le jeu d'entraînement. Il ne doit jamais être échantillonné.

## 12. Questions ouvertes

| # | Question | Bloquante | Responsable | Échéance |
|---|---|---|---|---|
| 1 | Chaîne de lecture retenue — `ADR-004` | Non *(spec indépendante du fournisseur)* | CTO | Fin M0 |
| 2 | Seuil d'exactitude en deçà duquel la CI échoue | **Oui** | CTO | M1 |
| 3 | Que fait-on d'un document qui n'est manifestement pas un CV ? | Non | Produit | M2 |
| 4 | Durée de conservation du document d'origine après suppression du compte | Non | Juridique | M5 |

## 13. Historique

| Version | Date | Changement |
|---|---|---|
| 0.1 | 2026-09-23 | Création |
| 0.2 | 2026-09-23 | Ajout de la vérification d'ancrage et du rejeu versionné |
