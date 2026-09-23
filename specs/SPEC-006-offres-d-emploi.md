---
id: SPEC-006
titre: Offres d'emploi
statut: brouillon
version: 0.1
jalon: M3
priorite: P0
exigences: [EXI-OFF-01, EXI-OFF-02, EXI-OFF-03, EXI-OFF-04, EXI-OFF-05, EXI-OFF-07, NFR-06]
depend_de: [SPEC-005, SPEC-013]
auteur: ""
derniere_maj: 2026-09-23
---

# SPEC-006 — Offres d'emploi

> **Brouillon.** Les règles et critères ci-dessous sont des amorces issues du cahier des charges
> et de l'analyse. Ils doivent être complétés et revus avant approbation.

## 1. Objectif

Publier une offre structurée, la rendre trouvable, et masquer l'identité de l'entreprise selon le statut du candidat.

## 2. Hors périmètre

Candidatures (`SPEC-007`) · configuration des tests (`SPEC-010`) · visibilité Premium (`SPEC-017`).

## 3. Règles métier pressenties

- **RG-1** — Les compétences d'une offre sont choisies dans le référentiel, jamais saisies en texte libre — sans quoi le classement n'est pas calculable.
- **RG-2** — Chaque compétence est marquée `requise` ou `souhaitée`.
- **RG-3** — Le nom de l'entreprise est masqué au candidat gratuit sur **tous** les points d'accès : page, résultats de recherche, notifications, page indexable.
- **RG-4** — La page publique d'une offre est rendue côté serveur et indexable par les moteurs de recherche.
- **RG-5** — La recherche s'appuie sur l'index plein texte de la base, sans moteur externe.

## 4. Critères d'acceptation amorcés

- **CA-1** — Étant donné un candidat gratuit, quand il consulte une offre par n'importe quel chemin, alors il voit le secteur et jamais le nom de l'entreprise.
- **CA-2** — Étant donné une offre publiée, quand sa page est demandée sans exécution de script, alors son contenu est présent dans la réponse.
- **CA-3** — Étant donné une offre publiée, quand sa page est mesurée sur un profil réseau 3G, alors elle s'affiche en moins de 1,5 seconde.
- **CA-4** — Étant donné une offre archivée, quand un candidat ouvre son ancien lien, alors il obtient une page explicite et non une erreur.

## 5. À compléter avant revue

Acteurs et déclencheurs · parcours nominal détaillé · modèle de données touché · interfaces et
écrans concernés · cas limites et erreurs · exigences non fonctionnelles applicables · télémétrie.

## 6. Questions ouvertes

| # | Question | Bloquante | Responsable | Échéance |
|---|---|---|---|---|
| 1 | Une offre expirée reste-t-elle indexée pour le référencement ? | Non | Produit | M3 |
| 2 | Quels filtres de recherche à la V1 ? | Non | Produit | M3 |

## 7. Historique

| Version | Date | Changement |
|---|---|---|
| 0.1 | 2026-09-23 | Création |
