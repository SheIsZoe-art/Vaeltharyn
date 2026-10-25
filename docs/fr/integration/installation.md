# Installer le plugin et le skill

Créateur : **SheIsZoe**. Plugin **0.8.0**, corpus **1.6.0**, structure **4.1.0**. Python 3.11+ suffit, sans dépendance supplémentaire.

Télécharger les paquets depuis la [Release courante](https://github.com/SheIsZoe-art/Vaeltharyn/releases/latest). Les empreintes SHA-256 et les URL de téléchargement sont aussi dans [release.json](../../../integrations/release.json).

## Plugin Codex

Depuis la racine d’une copie de `main`, le préparateur récupère le paquet courant si nécessaire et vérifie son empreinte :

```text
python scripts/installer_plugin.py
codex plugin marketplace add "<repository>/dist/vaeltharyn-0.8.0"
codex plugin add vaeltharyn-translator@vaeltharyn
codex plugin list --marketplace vaeltharyn --json
```
Remplacer `<repository>` par le chemin absolu du dépôt. Pour une archive déjà téléchargée, ajouter `--archive <chemin-du-zip>`. Une installation différente n’est pas écrasée : choisir un nouveau dossier avec `--destination`, ou sauvegarder puis remplacer la source du catalogue existant avant réinstallation officielle. Ne pas modifier le cache géré par Codex.

## Skill seul

Vérifier l’empreinte de `vaeltharyn-skill-0.8.0.zip`, puis extraire son contenu dans `~/.codex/skills/vaeltharyn-traducteur/`, avec `SKILL.md` directement dans ce dossier. Sauvegarder la version précédente et invoquer `$vaeltharyn-traducteur`. Le plugin contient le même skill sous le nom `translate-vaeltharyn`.

## Vérifier l’installation

```text
python <skill>/scripts/chercher.py --info
python <skill>/scripts/chercher.py --lang en "harmonic frequency" "exchange for mine"
```
Le dépôt vivant n’est pas requis : les paquets sont autonomes. `--root <repository>` ou `VAELTHARYN_ROOT` sélectionne explicitement un autre corpus. Une racine invalide échoue sans repli silencieux. Un nouveau chat peut être nécessaire pour charger les instructions mises à jour. L’application ChatGPT hébergée est une installation distincte du plugin Codex.

## Recompiler et contrôler

```text
python scripts/build_distribution.py
python scripts/verifier_corpus.py
python -m unittest discover -s tests
python scripts/verifier_distribution.py
```
Les ZIP sont produits dans `dist/releases/`, puis publiés comme pièces jointes de la Release. Ils ne sont pas enregistrés dans Git. Les sources dans `integrations/` doivent être compilées avant installation. Voir [la recherche](lookup.md) et [l’organisation](structure.md).
