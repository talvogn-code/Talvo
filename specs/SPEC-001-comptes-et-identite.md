---
id: SPEC-001
titre: Comptes et identité
statut: brouillon
version: 0.2
jalon: M1
priorite: P0
exigences: [EXI-CPT-01, EXI-CPT-02, EXI-CPT-07, NFR-01, NFR-02, NFR-05]
depend_de: []
auteur: ""
derniere_maj: 2026-09-23
---

# SPEC-001 — Comptes et identité

> **Cette spec ne peut pas être approuvée avant `ADR-003`** (identifiant de compte). Le parcours
> décrit ci-dessous suppose le téléphone comme identifiant principal ; la section 12 liste ce qui
> change si la décision retient l'e-mail.

## 1. Objectif

Permettre à un candidat guinéen de créer un compte et d'y revenir, **sans supposer qu'il possède
une adresse e-mail active**, et garantir qu'aucun utilisateur n'accède aux données d'une autre
organisation.

## 2. Hors périmètre

Profil professionnel (`SPEC-002`) · validation des entreprises (`SPEC-005`) · abonnements
(`SPEC-017`) · administration (`SPEC-015`).

## 3. Acteurs

| Acteur | Accès |
|---|---|
| Visiteur | Pages publiques uniquement |
| Candidat | Son propre espace |
| Membre d'organisation | L'espace de son organisation, selon son rôle |
| Administrateur TalVo | Back-office, avec journalisation de chaque accès à un profil |

Rôles au sein d'une organisation : `admin` (gère les membres et la facturation), `recruteur`
(publie, consulte, décide), `lecteur` (consulte seulement).

## 4. Parcours nominal — candidat

1. Le candidat saisit son numéro de téléphone au format local ou international.
2. Le système normalise le numéro en format international et envoie un code à six chiffres.
3. Le candidat saisit le code. À la première validation réussie, le compte est créé.
4. Le candidat choisit un nom et, **facultativement**, une adresse e-mail de secours.
5. Les connexions suivantes reprennent les étapes 1 à 3.

Aucun mot de passe n'est demandé au candidat. Un membre d'organisation utilise en revanche un
couple e-mail et mot de passe, avec second facteur optionnel.

## 5. Règles métier

- **RG-1** — Un numéro de téléphone identifie au plus un compte candidat actif.
- **RG-2** — Un code de vérification est valable 10 minutes, utilisable une seule fois, et
  invalidé dès qu'un nouveau code est demandé pour le même numéro.
- **RG-3** — Au plus 3 codes par numéro et par heure, et 10 par adresse réseau et par heure.
  Au-delà, la demande est refusée sans indiquer si le numéro est connu.
- **RG-4** — Après 5 codes erronés consécutifs, le numéro est bloqué 30 minutes.
- **RG-5** — Le système ne révèle jamais si un identifiant existe déjà : les messages de
  connexion et d'inscription sont identiques.
- **RG-6** — Un changement de numéro exige la validation de l'ancien **et** du nouveau numéro.
  Si l'ancien n'est plus accessible, la procédure passe par le support et est journalisée.
- **RG-7** — Toute requête portant sur une donnée rattachée à une organisation est filtrée par
  l'organisation de l'appelant, au niveau de l'accès aux données et non de chaque contrôleur.
- **RG-8** — Une session candidat expire après 30 jours d'inactivité ; une session
  professionnelle après 12 heures. La déconnexion est accessible en deux interactions au plus.
- **RG-9** — La consultation d'un profil candidat par un administrateur TalVo est journalisée
  avec l'identité de l'administrateur et le motif.

## 6. Modèle de données

`users` — ajout de `phone` (unique, format international, nullable), `phone_verified_at` ;
`email` devient nullable pour les candidats et reste obligatoire pour les comptes professionnels.
Nouvelles tables : `verification_codes` (numéro, empreinte du code, expiration, tentatives),
`organizations`, `organization_members` (`user_id`, `organization_id`, `role`), `sessions`.

## 7. Interfaces

Écrans 02 (connexion / inscription) et un écran de gestion des membres côté organisation.
Points d'entrée : demande de code, vérification de code, rafraîchissement de session,
déconnexion, gestion des membres.

## 8. Critères d'acceptation

- **CA-1** — Étant donné un numéro valide jamais vu, quand il demande un code et le saisit
  correctement, alors un compte candidat est créé et une session ouverte.
- **CA-2** — Étant donné un numéro connu, quand il demande un code et le saisit correctement,
  alors il retrouve son compte existant — aucun doublon n'est créé.
- **CA-3** — Étant donné un code expiré depuis plus de 10 minutes, quand il est saisi, alors il
  est refusé et le message ne distingue pas « expiré » de « incorrect ».
- **CA-4** — Étant donné 3 codes déjà demandés dans l'heure pour un numéro, quand un quatrième
  est demandé, alors la demande est refusée et **aucun SMS n'est envoyé**.
- **CA-5** — Étant donné un numéro saisi au format local, quand il est enregistré, alors il est
  stocké au format international, et les deux formats mènent au même compte.
- **CA-6** — Étant donné un recruteur de l'organisation A, quand il demande une candidature de
  l'organisation B par son identifiant, alors la réponse est « introuvable », jamais « interdit ».
- **CA-7** — Étant donné un `lecteur`, quand il tente de publier une offre, alors l'action est
  refusée et journalisée.
- **CA-8** — Étant donné un administrateur TalVo consultant un profil candidat, quand il y
  accède, alors une entrée de journal nomme l'administrateur, le profil et l'horodatage.

## 9. Cas limites

Numéro porté d'un opérateur à l'autre · SMS reçu en retard alors qu'un nouveau code a été demandé
(seul le dernier est valide) · deux appareils demandant un code simultanément · candidat
saisissant un numéro fixe · appareil partagé en cybercafé · un même utilisateur membre de
plusieurs organisations.

## 10. Exigences non fonctionnelles

`NFR-01` accès selon le consentement · `NFR-02` cloisonnement entre organisations ·
`NFR-05` limitation de débit sur l'envoi de codes.

> Le point `NFR-05` a un effet financier direct : sans limitation, un attaquant peut faire
> exploser la facture SMS. Cette règle n'est pas seulement une protection de sécurité.

## 11. Télémétrie

`auth.code_demande`, `auth.code_envoye` (avec le coût unitaire), `auth.code_verifie`,
`auth.code_echoue`, `auth.compte_cree`, `auth.session_ouverte`, `auth.limite_atteinte`.
Alimentent : taux d'abandon à l'inscription, coût d'acquisition en SMS, tentatives d'abus.

## 12. Questions ouvertes

| # | Question | Bloquante | Responsable | Échéance |
|---|---|---|---|---|
| 1 | Téléphone ou e-mail comme identifiant principal — `ADR-003` | **Oui** | Les deux CTO | Fin M0 |
| 2 | Opérateur ou agrégateur SMS retenu, et coût unitaire réel | **Oui** | Direction | Fin M0 |
| 3 | Second facteur obligatoire pour les comptes professionnels ? | Non | CTO | M3 |
| 4 | Durée de conservation d'un compte inactif | Non | Juridique | M5 |

## 13. Historique

| Version | Date | Changement |
|---|---|---|
| 0.1 | 2026-09-23 | Création |
| 0.2 | 2026-09-23 | Ajout du cloisonnement inter-organisations et de la limitation de débit |
