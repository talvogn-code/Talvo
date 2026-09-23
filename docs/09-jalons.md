# TalVo — Jalons

Huit jalons, de la fin du cadrage à la V1.5. Chacun a un **objectif**, des **specs à livrer**,
des **décisions à trancher** et surtout des **critères de sortie** vérifiables : on ne passe pas
au jalon suivant tant qu'ils ne sont pas tous verts.

Les décisions référencées (`ADR-00x`) sont dans `docs/adr/`. Un jalon ne se ferme pas avec une
décision de son périmètre encore en statut `proposée`.

---

## M0 — Cadrage et décisions · *sept. → oct. 2026*

**Objectif** — figer le périmètre, poser la méthode, et réunir les éléments qui permettent de
décider de la chaîne de lecture des CV sur des mesures plutôt que sur des impressions.

**Livrables**
- Documents de cadrage, modèle de données, moteur de matching, chaîne documentaire *(faits)*
- Infrastructure spec-driven : registre, specs, ADR, modèles de PR et d'issue *(fait)*
- Specs `SPEC-001` à `SPEC-016` au moins en `brouillon`, les P0 du socle en `approuvée`
- **Corpus de 150 à 200 CV réels**, dont 50 annotés en vérité terrain
- Banc de mesure comparant 3 à 4 chaînes de lecture

**Décisions à trancher** — `ADR-001` découpage applicatif · `ADR-003` identifiant de compte ·
`ADR-004` chaîne de lecture · `ADR-005` modèles ouverts ou API

**Critères de sortie**
- [ ] Le corpus existe, est annoté, et son accès est restreint et tracé
- [ ] Les quatre chaînes candidates ont été mesurées sur les cinq mêmes axes
- [ ] `ADR-001`, `ADR-003`, `ADR-004`, `ADR-005` sont en statut `acceptée`
- [ ] Les entreprises pilotes ont répondu sur la localisation des données
- [ ] Les maquettes des parcours candidat et entreprise sont validées

**Risque principal** — le corpus glisse et bloque tout le reste. C'est le seul livrable de M0
qui ne dépend d'aucune décision : il doit démarrer immédiatement.

---

## M1 — Socle · *nov. 2026*

**Objectif** — un squelette déployable, sécurisé et observable, sur lequel tout le reste
s'empile. Aucune fonctionnalité produit visible.

**Specs** — `SPEC-001` comptes et identité · `SPEC-013` référentiels · `SPEC-016` observabilité

**Livrables**
- Schéma de base et migrations versionnées, réversibles
- Authentification, rôles, organisations multi-utilisateurs
- Stockage objet, URLs signées, analyse antivirus des dépôts
- Chaîne de livraison : CI, recette automatique, production sur bouton
- **Barrière d'évaluation de l'extraction branchée sur le corpus**
- Générateur de données synthétiques
- Journalisation, suivi des erreurs, alertes

**Décisions** — `ADR-002` hébergement · `ADR-006` stockage et localisation des données

**Critères de sortie**
- [ ] Un compte se crée, se connecte, se récupère — sur téléphone comme sur poste
- [ ] Une migration s'applique et se retire sans coupure, vérifié en recette
- [ ] La CI complète passe sous dix minutes
- [ ] Une sauvegarde a été **restaurée** au moins une fois, chronométrée
- [ ] Un changement de consigne d'extraction déclenche le rejeu sur le corpus
- [ ] Le cloisonnement entre deux organisations est couvert par des tests

---

## M2 — CV et profils · *nov. → déc. 2026*

**Objectif** — la brique qui porte toute la valeur : déposer un CV et en obtenir un profil
exploitable et corrigé par le candidat.

**Specs** — `SPEC-002` profil candidat · `SPEC-003` import et lecture de CV ·
`SPEC-004` créateur et export de CV

**Critères de sortie**
- [ ] Un PDF natif, un PDF scanné, un DOCX et une photo produisent chacun un profil exploitable
- [ ] Chaque champ extrait porte son extrait source ; un champ non ancré est marqué à valider
- [ ] Le candidat corrige, et la correction est enregistrée comme donnée d'entraînement
- [ ] Un CV créé dans TalVo s'exporte en PDF fidèle à l'aperçu, accents compris
- [ ] L'exactitude mesurée sur le corpus dépasse le seuil fixé en M0

---

## M3 — Offres et candidatures · *déc. 2026*

**Objectif** — le circuit entreprise : publier, recevoir, suivre.

**Specs** — `SPEC-005` entreprises et validation · `SPEC-006` offres · `SPEC-007` candidatures

**Critères de sortie**
- [ ] Une entreprise non validée ne peut pas publier — vérifié par test
- [ ] Le nom de l'entreprise est masqué au candidat gratuit sur tous les points d'accès
- [ ] Une offre publique est indexée et servie rendue serveur, sous 1,5 s en 3G simulée
- [ ] Un candidat postule une seule fois par offre, et suit l'état de sa candidature

---

## M4 — Matching et tests · *déc. 2026 → janv. 2027*

**Objectif** — ce qui distingue TalVo d'un site d'annonces.

**Specs** — `SPEC-008` matching et scoring · `SPEC-009` sourcing · `SPEC-010` tests en ligne ·
`SPEC-011` shortlist et fiche candidat

**Décisions** — `ADR-007` canal de notification

**Critères de sortie**
- [ ] Le score est reproductible : mêmes entrées, même version d'algorithme, même résultat
- [ ] Chaque score s'accompagne du détail qui l'explique, rendu en langage naturel
- [ ] Les profils sourcés apparaissent dans un espace distinct des candidatures
- [ ] Une coupure réseau pendant un test ne perd aucune réponse — testé en conditions dégradées
- [ ] Le chronomètre résiste à une manipulation de l'horloge du client
- [ ] La banque de questions atteint le ratio prévu sur les tests du pilote
- [ ] Une shortlist se produit, se consulte et se transmet

---

## M5 — V1 pilote · *janv. 2027*

**Objectif** — mise en service réelle avec 5 à 10 entreprises.

**Livrables** — conditions générales et politique de confidentialité · procédure d'incident ·
canal de support · validation manuelle des entreprises · tableau de bord des indicateurs

**Critères de sortie**
- [ ] Les 18 critères d'acceptation du cahier des charges sont couverts par des tests qui passent
- [ ] Revue de sécurité passée, corrections bloquantes traitées
- [ ] Documents juridiques publiés
- [ ] Les indicateurs du cadrage sont réellement mesurés, pas seulement définis
- [ ] Test de charge passé sur le parcours de dépôt de CV
- [ ] Une personne identifiée répond au support

---

## M6 — Stabilisation · *févr. 2027*

**Objectif** — corriger ce que le réel a révélé, et mesurer la promesse.

**Critères de sortie**
- [ ] Le temps de tri réellement économisé par les recruteurs est mesuré et comparé au tri manuel
- [ ] Les seuils de matching sont réajustés d'après les retours d'entretien
- [ ] Les scores de tests sont corrélés aux avis des recruteurs
- [ ] Aucun incident de niveau critique ouvert depuis deux semaines

---

## M7 — V1.5 · *mars 2027*

**Objectif** — ouvrir la monétisation et le sourcing.

**Specs** — `SPEC-017` Premium et visibilité · `SPEC-018` messagerie · `SPEC-015` administration

**Décisions** — `ADR-009` paiement mobile money

**Critères de sortie**
- [ ] Un candidat Premium voit le nom de l'entreprise et contacte la RH
- [ ] Un abonnement se souscrit, se renouvelle et **se résilie immédiatement**
- [ ] Le sourcing propose des profils qui n'ont pas postulé, avec consentement vérifié

---

## Règles de passage

1. **Aucun jalon ne se ferme avec un critère de sortie non coché.** Un critère qui ne peut pas
   être atteint se renégocie explicitement, il ne se contourne pas.
2. **Aucune spec n'entre en développement avant d'être `approuvée`.**
3. **Aucun jalon ne se ferme avec une décision de son périmètre encore `proposée`.**
4. Le travail éditorial — banque de questions, référentiel, formulations — court **en parallèle**
   de M1 à M4. C'est le chemin critique le plus souvent oublié.
