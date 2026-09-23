#!/usr/bin/env python3
"""Contrôle de cohérence de la documentation spec-driven de TalVo.

Vérifie, sans rien exécuter d'applicatif :
  1. chaque spec porte un en-tête complet et un statut connu ;
  2. chaque exigence du registre est couverte par une spec qui la déclare ;
  3. chaque exigence déclarée par une spec existe au registre ;
  4. chaque dépendance entre specs pointe vers une spec existante ;
  5. aucune spec « approuvée » ne conserve une question ouverte bloquante ;
  6. chaque décision technique porte un statut et un jalon connus.

Usage : python3 scripts/check_specs.py [--index]
        --index régénère specs/README.md à partir des en-têtes.
"""
import re, sys, pathlib, collections

ROOT = pathlib.Path(__file__).resolve().parent.parent
SPECS = ROOT / "specs"
ADRS = ROOT / "docs" / "adr"
REGISTRE = ROOT / "docs" / "10-registre-exigences.md"

STATUTS = {"brouillon", "en revue", "approuvée", "implémentée", "obsolète"}
STATUTS_ADR = {"proposée", "acceptée", "remplacée"}
JALONS = {f"M{i}" for i in range(8)}
CHAMPS = ["id", "titre", "statut", "version", "jalon", "priorite", "exigences", "depend_de"]

erreurs, avertissements = [], []


def entete(path):
    txt = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", txt, re.S)
    if not m:
        return None, txt
    meta = {}
    for ligne in m.group(1).splitlines():
        if ":" not in ligne:
            continue
        cle, _, val = ligne.partition(":")
        val = val.strip()
        if val.startswith("[") and val.endswith("]"):
            val = [x.strip() for x in val[1:-1].split(",") if x.strip()]
        meta[cle.strip()] = val
    return meta, txt


def main():
    exigences_registre = set()
    if REGISTRE.exists():
        exigences_registre = set(re.findall(r"`((?:EXI|NFR)-[A-Z]*-?\d+)`", REGISTRE.read_text(encoding="utf-8")))
    else:
        erreurs.append("docs/10-registre-exigences.md est introuvable")

    specs, couvertes = {}, collections.defaultdict(list)
    for f in sorted(SPECS.glob("SPEC-*.md")):
        meta, txt = entete(f)
        if meta is None:
            erreurs.append(f"{f.name} : en-tête absent")
            continue
        for champ in CHAMPS:
            if champ not in meta:
                erreurs.append(f"{f.name} : champ « {champ} » manquant dans l'en-tête")
        if meta.get("statut") not in STATUTS:
            erreurs.append(f"{f.name} : statut « {meta.get('statut')} » inconnu")
        if meta.get("jalon") not in JALONS:
            erreurs.append(f"{f.name} : jalon « {meta.get('jalon')} » inconnu")
        specs[meta.get("id")] = (f, meta, txt)
        for e in meta.get("exigences", []):
            couvertes[e].append(meta.get("id"))
            if exigences_registre and e not in exigences_registre:
                erreurs.append(f"{f.name} : l'exigence {e} n'existe pas au registre")
        if meta.get("statut") == "approuvée":
            bloquantes = [l for l in txt.splitlines() if l.startswith("|") and "Oui" in l and "Bloquante" not in l]
            if bloquantes:
                erreurs.append(f"{f.name} : statut « approuvée » avec une question bloquante ouverte")
        if not re.search(r"\*\*CA-1\*\*", txt):
            avertissements.append(f"{f.name} : aucun critère d'acceptation CA-1 trouvé")

    for sid, (f, meta, _) in specs.items():
        for d in meta.get("depend_de", []):
            if d not in specs:
                erreurs.append(f"{f.name} : dépendance {d} introuvable")

    for e in sorted(exigences_registre - set(couvertes)):
        erreurs.append(f"exigence {e} : couverte par aucune spec")

    for f in sorted(ADRS.glob("ADR-*.md")):
        meta, _ = entete(f)
        if meta is None:
            erreurs.append(f"{f.name} : en-tête absent")
            continue
        if meta.get("statut") not in STATUTS_ADR:
            erreurs.append(f"{f.name} : statut « {meta.get('statut')} » inconnu")
        if meta.get("jalon_de_decision") not in JALONS:
            erreurs.append(f"{f.name} : jalon de décision inconnu")

    if "--index" in sys.argv:
        ecrire_index(specs)

    par_statut = collections.Counter(m.get("statut") for _, m, _ in specs.values())
    print(f"{len(specs)} specs · {len(exigences_registre)} exigences · "
          f"{len(list(ADRS.glob('ADR-*.md')))} décisions")
    print("  " + " · ".join(f"{k} : {v}" for k, v in sorted(par_statut.items())))
    for a in avertissements:
        print(f"  avertissement — {a}")
    for e in erreurs:
        print(f"  ERREUR — {e}")
    return 1 if erreurs else 0


def ecrire_index(specs):
    lignes = [
        "# Spécifications\n",
        "Index généré par `python3 scripts/check_specs.py --index`. Ne pas modifier à la main.\n",
        "La méthode est décrite dans [`CONTRIBUTING.md`](../CONTRIBUTING.md), les exigences dans",
        "[`docs/10-registre-exigences.md`](../docs/10-registre-exigences.md), les jalons dans",
        "[`docs/09-jalons.md`](../docs/09-jalons.md) et les décisions dans [`docs/adr/`](../docs/adr/).\n",
        "| Spec | Titre | Statut | Jalon | Prio | Exigences | Dépend de |",
        "|---|---|---|---|---|---|---|",
    ]
    for sid in sorted(specs):
        f, m, _ = specs[sid]
        exi = ", ".join(f"`{x}`" for x in m.get("exigences", [])) or "—"
        dep = ", ".join(f"`{x}`" for x in m.get("depend_de", [])) or "—"
        lignes.append(f"| [`{sid}`]({f.name}) | {m.get('titre')} | `{m.get('statut')}` | "
                      f"`{m.get('jalon')}` | {m.get('priorite')} | {exi} | {dep} |")
    lignes += [
        "\n## Statuts\n",
        "| Statut | Signification |", "|---|---|",
        "| `brouillon` | En cours d'écriture, incomplète |",
        "| `en revue` | Complète, soumise en pull request |",
        "| `approuvée` | **L'implémentation peut commencer** |",
        "| `implémentée` | Le code la satisfait, tous les critères passent |",
        "| `obsolète` | Remplacée ou abandonnée |\n",
        "Une spec ne passe pas en `approuvée` s'il lui reste une question ouverte bloquante ;",
        "le contrôle ci-dessus le vérifie.",
    ]
    (SPECS / "README.md").write_text("\n".join(lignes) + "\n", encoding="utf-8")


if __name__ == "__main__":
    sys.exit(main())
