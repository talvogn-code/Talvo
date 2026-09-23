# TalVo — Registre des exigences

> Source de vérité de **ce qui doit être vrai** du produit. Chaque exigence porte un
> identifiant stable, une priorité, sa source, et la spec qui la couvre.

> Une exigence sans spec est un trou. Une spec qui ne couvre aucune exigence est du périmètre
> non décidé. Le contrôle `scripts/check_specs.py` vérifie que la correspondance tient.

**Priorités** — `P0` indispensable à la V1 · `P1` après validation du pilote · `P2` plus tard.


## Comptes et accès

| ID | Exigence | Prio | Source | Spec |
|---|---|---|---|---|
| `EXI-CPT-01` | Un candidat crée un compte et s'y connecte. | P0 | cadrage §7.1 | `SPEC-001` |
| `EXI-CPT-02` | Un candidat récupère l'accès à son compte sans adresse e-mail active. | P0 | angle mort A.1 | `SPEC-001` |
| `EXI-CPT-03` | Une entreprise ou un cabinet crée un compte professionnel. | P0 | cadrage §7.3 | `SPEC-005` |
| `EXI-CPT-04` | Une organisation professionnelle compte plusieurs membres avec des rôles distincts. | P0 | angle mort A.3 | `SPEC-005` |
| `EXI-CPT-05` | Un administrateur TalVo dispose d'un accès distinct et journalisé. | P0 | cadrage §12.4 | `SPEC-015` |
| `EXI-CPT-06` | Le statut Premium découle d'un abonnement actif, jamais d'un rôle. | P1 | cadrage §7.2 | `SPEC-017` |
| `EXI-CPT-07` | Une session se termine explicitement, y compris sur appareil partagé. | P1 | angle mort A.2 | `SPEC-001` |

## Profils

| ID | Exigence | Prio | Source | Spec |
|---|---|---|---|---|
| `EXI-PRF-01` | Un candidat crée et modifie son profil professionnel. | P0 | cadrage §7.1 | `SPEC-002` |
| `EXI-PRF-02` | Le niveau de complétude du profil est calculé et affiché. | P0 | cadrage §12.1 | `SPEC-002` |
| `EXI-PRF-03` | Un candidat consent explicitement à apparaître dans le vivier proposé aux recruteurs. | P0 | cadrage règle 8 | `SPEC-002` |
| `EXI-PRF-04` | Une entreprise renseigne le profil de son organisation. | P0 | cadrage §7.3 | `SPEC-005` |

## CV

| ID | Exigence | Prio | Source | Spec |
|---|---|---|---|---|
| `EXI-CV-01` | Un candidat importe un CV au format PDF ou DOCX. | P0 | cadrage §8.1 | `SPEC-003` |
| `EXI-CV-02` | Les informations principales sont extraites et préremplissent le profil. | P0 | cadrage §8.1 | `SPEC-003` |
| `EXI-CV-03` | Le candidat corrige manuellement les données extraites. | P0 | cadrage §8.1 | `SPEC-003` |
| `EXI-CV-04` | Un CV scanné ou photographié est traité comme un cas nominal. | P0 | angle mort §1.1 | `SPEC-003` |
| `EXI-CV-05` | Chaque champ extrait est rattaché à un extrait du document source. | P0 | docs/05 levier 2 | `SPEC-003` |
| `EXI-CV-06` | Un champ non rattachable à la source est rejeté ou marqué à valider. | P0 | docs/05 levier 2 | `SPEC-003` |
| `EXI-CV-07` | Un candidat crée un CV directement dans TalVo. | P0 | cadrage §8.2 | `SPEC-004` |
| `EXI-CV-08` | Un CV créé s'exporte en PDF fidèle à l'aperçu, pagination et accents compris. | P0 | cadrage §8.2 | `SPEC-004` |
| `EXI-CV-09` | Un candidat Premium adapte son CV à une offre. | P1 | cadrage §8.3 | `SPEC-017` |
| `EXI-CV-10` | Un CV adapté ne contient que des informations présentes dans la source. | P1 | cadrage règle 3 | `SPEC-017` |
| `EXI-CV-11` | Les éléments manquants au regard de l'offre sont signalés au candidat. | P1 | cadrage §8.3 | `SPEC-017` |

## Offres

| ID | Exigence | Prio | Source | Spec |
|---|---|---|---|---|
| `EXI-OFF-01` | Une entreprise crée une offre avec ses critères de recrutement. | P0 | cadrage §9 | `SPEC-006` |
| `EXI-OFF-02` | Une entreprise non validée ne peut pas publier d'offre publique. | P0 | cadrage règle 1 | `SPEC-006` |
| `EXI-OFF-03` | Une offre se publie, se modifie, se met en pause et s'archive. | P0 | cadrage §9 | `SPEC-006` |
| `EXI-OFF-04` | Une offre dispose d'une page publique indexable. | P0 | cadrage §9 | `SPEC-006` |
| `EXI-OFF-05` | Le candidat gratuit ne voit que le secteur d'activité de l'entreprise. | P0 | cadrage §9.1 | `SPEC-006` |
| `EXI-OFF-06` | Le candidat Premium voit le nom de l'entreprise et les informations disponibles. | P1 | cadrage §9.1 | `SPEC-017` |
| `EXI-OFF-07` | Un candidat recherche et filtre les offres. | P0 | cadrage §7.1 | `SPEC-006` |
| `EXI-OFF-08` | L'entreprise coche « tests requis » et sélectionne les tests à l'offre. | P0 | cadrage §11.1 | `SPEC-010` |

## Candidatures

| ID | Exigence | Prio | Source | Spec |
|---|---|---|---|---|
| `EXI-CND-01` | Un candidat postule à une offre en ligne. | P0 | cadrage §6.1 | `SPEC-007` |
| `EXI-CND-02` | Un candidat ne postule qu'une fois à une même offre. | P0 | modèle de données | `SPEC-007` |
| `EXI-CND-03` | Un candidat suit l'état de sa candidature. | P0 | cadrage §6.1 | `SPEC-007` |
| `EXI-CND-04` | L'entreprise voit les candidats ayant postulé à son offre. | P0 | cadrage §17 | `SPEC-007` |
| `EXI-CND-05` | Les notes internes du recruteur restent privées. | P0 | cadrage règle 5 | `SPEC-007` |
| `EXI-CND-06` | Le pipeline de recrutement suit des états explicites. | P1 | cadrage §12.2 | `SPEC-011` |

## Matching et sourcing

| ID | Exigence | Prio | Source | Spec |
|---|---|---|---|---|
| `EXI-MCH-01` | Un score de correspondance est calculé entre un profil et une offre. | P0 | cadrage §10 | `SPEC-008` |
| `EXI-MCH-02` | Le score combine compétences, expérience, fonction, formation et localisation selon des poids configurables. | P0 | cadrage §10.2 | `SPEC-008` |
| `EXI-MCH-03` | Chaque score s'accompagne du détail des éléments qui l'ont produit. | P0 | cadrage §12.3 | `SPEC-008` |
| `EXI-MCH-04` | Le score est reproductible à version d'algorithme constante. | P0 | docs/02 §6 | `SPEC-008` |
| `EXI-MCH-05` | Un score est présenté comme une aide à la décision, jamais comme une décision. | P0 | cadrage règle 7 | `SPEC-008` |
| `EXI-MCH-06` | Aucun critère de tri n'encode d'attribut discriminatoire. | P0 | docs/02 §6 | `SPEC-008` |
| `EXI-MCH-07` | Les candidatures sont classées selon les critères du poste. | P0 | cadrage §17 | `SPEC-008` |
| `EXI-MCH-08` | TalVo identifie des profils pertinents n'ayant pas postulé. | P1 | cadrage §10.3 | `SPEC-009` |
| `EXI-MCH-09` | Les profils sourcés sont présentés dans un espace distinct des candidatures. | P1 | cadrage règle 6 | `SPEC-009` |
| `EXI-MCH-10` | Le vocabulaire des compétences, fonctions et diplômes est normalisé par un référentiel. | P0 | docs/04 §1.2 | `SPEC-013` |

## Tests en ligne

| ID | Exigence | Prio | Source | Spec |
|---|---|---|---|---|
| `EXI-TST-01` | TalVo invite automatiquement les candidats concernés à passer un test. | P0 | cadrage §11.1 | `SPEC-010` |
| `EXI-TST-02` | Un candidat passe un test en ligne dans un délai défini. | P0 | cadrage §11.1 | `SPEC-010` |
| `EXI-TST-03` | Le score est calculé et associé à une tentative identifiable et horodatée. | P0 | cadrage règle 9 | `SPEC-010` |
| `EXI-TST-04` | Un candidat n'est jamais présenté comme ayant passé un test qu'il n'a pas réalisé. | P0 | cadrage règle 4 | `SPEC-010` |
| `EXI-TST-05` | Le décompte du temps fait autorité côté serveur. | P0 | angle mort B.1 | `SPEC-010` |
| `EXI-TST-06` | Chaque réponse est enregistrée immédiatement et la tentative reprend après coupure réseau. | P0 | angle mort B.2 | `SPEC-010` |
| `EXI-TST-07` | Les questions servies sont tirées aléatoirement dans une banque nettement plus large. | P0 | angle mort B.3 | `SPEC-010` |
| `EXI-TST-08` | Les résultats de tests alimentent la présélection. | P0 | cadrage §11.1 | `SPEC-011` |
| `EXI-TST-09` | Un candidat passe volontairement un test de certification de compétence. | P1 | cadrage §11.3 | `SPEC-010` |
| `EXI-TST-10` | Un score de certification volontaire est distinct d'un test demandé par une entreprise. | P1 | cadrage §11.3 | `SPEC-010` |
| `EXI-TST-11` | Un badge de compétence vérifiée s'affiche sur le profil. | P1 | cadrage §11.3 | `SPEC-010` |
| `EXI-TST-12` | Une tentative contestée peut être rejouée et arbitrée. | P1 | angle mort B.5 | `SPEC-010` |

## Présélection

| ID | Exigence | Prio | Source | Spec |
|---|---|---|---|---|
| `EXI-PRS-01` | TalVo produit une shortlist de candidats pertinents. | P0 | cadrage §10.4 | `SPEC-011` |
| `EXI-PRS-02` | La fiche candidat présente le score, son explication, les expériences, compétences, formations et résultats de tests. | P0 | cadrage §12.3 | `SPEC-011` |
| `EXI-PRS-03` | Le recruteur présélectionne, contacte, demande un entretien ou écarte un candidat. | P0 | cadrage §12.3 | `SPEC-011` |

## Tableaux de bord

| ID | Exigence | Prio | Source | Spec |
|---|---|---|---|---|
| `EXI-DSH-01` | Le candidat dispose d'un tableau de bord de ses candidatures, CV, tests et notifications. | P0 | cadrage §12.1 | `SPEC-012` |
| `EXI-DSH-02` | L'entreprise dispose d'un tableau de bord de ses offres, candidatures, tests et shortlists. | P0 | cadrage §12.2 | `SPEC-012` |

## Administration

| ID | Exigence | Prio | Source | Spec |
|---|---|---|---|---|
| `EXI-ADM-01` | Un administrateur valide ou refuse une entreprise, avec motif. | P0 | cadrage §12.4 | `SPEC-005` |
| `EXI-ADM-02` | Un administrateur gère le catalogue de tests et les questions. | P0 | cadrage §12.4 | `SPEC-015` |
| `EXI-ADM-03` | Un administrateur gère les référentiels métiers, compétences et secteurs. | P0 | cadrage §12.4 | `SPEC-013` |
| `EXI-ADM-04` | Un signalement d'offre ou de profil est traité et tracé. | P0 | angle mort D.1 | `SPEC-015` |
| `EXI-ADM-05` | Toute action de modération ou de modification importante est journalisée. | P0 | cadrage règle 10 | `SPEC-015` |

## Monétisation

| ID | Exigence | Prio | Source | Spec |
|---|---|---|---|---|
| `EXI-MON-01` | Un candidat souscrit, renouvelle et résilie un abonnement Premium. | P1 | cadrage §13.1 | `SPEC-017` |
| `EXI-MON-02` | Un candidat Premium contacte la RH via TalVo pour une offre. | P1 | cadrage §13.1 | `SPEC-018` |
| `EXI-MON-03` | Un candidat Premium reçoit des offres recommandées correspondant à son profil. | P1 | cadrage §13.1 | `SPEC-017` |
| `EXI-MON-04` | Une messagerie relie candidat et recruteur dans le cadre d'un recrutement. | P1 | cadrage §7.3 | `SPEC-018` |

## Exigences non fonctionnelles

| ID | Exigence | Prio | Source | Spec |
|---|---|---|---|---|
| `NFR-01` | Les données personnelles ne sont accessibles que selon les droits et le cadre de consentement applicables. | P0 | cadrage règle 8 | `SPEC-001` |
| `NFR-02` | Un recruteur d'une organisation n'accède jamais aux données d'une autre organisation. | P0 | angle mort C.3 | `SPEC-001` |
| `NFR-03` | Tout fichier déposé est analysé, son type réel vérifié, sa taille bornée, et son traitement isolé. | P0 | angle mort C.1 | `SPEC-003` |
| `NFR-04` | Les fichiers ne sont jamais servis publiquement : accès par URL signée à durée courte. | P0 | angle mort C.1 | `SPEC-003` |
| `NFR-05` | L'envoi de codes de connexion est limité en débit par numéro et par adresse. | P0 | angle mort C.2 | `SPEC-001` |
| `NFR-06` | Une page publique d'offre s'affiche en moins de 1,5 s sur un profil réseau 3G. | P0 | angle mort I.1 | `SPEC-006` |
| `NFR-07` | 95 % des CV déposés sont traités en moins de trois minutes. | P0 | docs/presentation/pipeline | `SPEC-003` |
| `NFR-08` | Les sauvegardes sont automatiques et leur restauration est testée périodiquement. | P0 | angle mort E.1 | `SPEC-016` |
| `NFR-09` | La profondeur de la file et l'âge du plus vieux travail sont surveillés et alertés. | P0 | angle mort E.2 | `SPEC-016` |
| `NFR-10` | Les événements nécessaires au calcul des indicateurs sont émis dès la V1. | P0 | angle mort G | `SPEC-016` |
| `NFR-11` | Le modèle de données porte le pays sur les entités géographiques, offres, organisations et abonnements. | P0 | docs/04 §4.3 | `SPEC-013` |
| `NFR-12` | Les dates sont stockées en UTC et affichées en heure locale. | P0 | angle mort I.4 | `SPEC-016` |
| `NFR-13` | L'interface est traduisible dès la V1, même avec une seule langue active. | P1 | angle mort I.3 | `SPEC-012` |
| `NFR-14` | Aucun texte destiné à l'utilisateur n'est écrit en dur dans le code. | P0 | convention | `SPEC-012` |
| `NFR-15` | Les appels aux fournisseurs externes passent par une interface interne remplaçable. | P0 | docs/05 §1 | `SPEC-003` |
| `NFR-16` | Toute modification des poids de matching change la version d'algorithme et est journalisée. | P0 | docs/02 §6 | `SPEC-008` |
| `NFR-17` | Aucune donnée de production n'est copiée dans un autre environnement. | P0 | pipeline §environnements | `SPEC-016` |
| `NFR-18` | Les conditions générales, la politique de confidentialité et le registre des traitements existent avant la mise en ligne. | P0 | angle mort J | `SPEC-015` |

---

**90 exigences enregistrées**, dont **72 en P0** — le périmètre à couvrir avant la mise en service pilote de janvier 2027.

Les exigences issues des « angles morts » ne figurent pas au cahier des charges d'origine :
elles ont été ajoutées après analyse et sont signalées comme telles dans la colonne source.
