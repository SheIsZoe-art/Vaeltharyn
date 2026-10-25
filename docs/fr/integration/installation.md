# Installer le plugin et le skill

Créateur : **SheIsZoe**. Plugin **0.5.0**, corpus **1.5.0**, structure **2.0.0**. Python 3.10+ est nécessaire pour la recherche ; aucune bibliothèque supplémentaire.

Télécharger la branche `feat/jurons-insultes-fr-en` du dépôt, puis ouvrir un terminal à sa racine. Le pointeur [latest.json](../../../distributions/latest.json) indique les paquets courants et leurs SHA-256. Éviter les anciennes distributions archivées.

## Plugin Codex

Le préparateur vérifie le paquet, extrait le corpus autonome et crée un catalogue local dédié :

```text
python scripts/installer_plugin.py
codex plugin marketplace add "<repository>/dist/vaeltharyn-0.5.0"
codex plugin add vaeltharyn-translator@vaeltharyn
codex plugin list --marketplace vaeltharyn --json
```
Remplacer `<repository>` par le chemin absolu du dépôt. Le nom du catalogue reste `vaeltharyn`, celui du plugin `vaeltharyn-translator`. Le plugin doit être installé et activé en version 0.5.0. Lancer un nouveau chat pour recharger ses instructions si nécessaire.

Une installation existante n’est pas écrasée par le préparateur : choisir un nouveau dossier avec `--destination`, ou sauvegarder puis remplacer le dossier **source** du catalogue existant. Utiliser ensuite les commandes Codex pour réinstaller. Ne pas modifier directement le cache des plugins.

## Skill seul

Vérifier le SHA-256 de [l’archive du skill](../../../distributions/vaeltharyn-skill-1.5.0-structure-2.0.0.zip), puis extraire son contenu dans `~/.codex/skills/vaeltharyn-traducteur/` : `SKILL.md` doit être directement dans ce dossier. Sauvegarder l’ancienne version avant remplacement. Invoquer `$vaeltharyn-traducteur`.

## Vérifier le corpus embarqué

```text
python <skill>/scripts/chercher.py --info
python <skill>/scripts/chercher.py --lang en "harmonic frequency" "exchange for mine"
```
Les paquets contiennent les 65 041 entrées et 416 fiches d’expression dans un index autonome. Les 719 renvois de l’inventaire et les notes de portée sont conservés. Le dépôt vivant n’est pas requis. Pour sélectionner explicitement le dépôt source : `--root <repository>` ou `VAELTHARYN_ROOT`. Une racine incorrecte provoque une erreur.

## Recompiler depuis les sources

```text
python scripts/build_distribution.py
python scripts/verifier_structure.py
python scripts/verifier_distribution.py
```
Les sources légères dans `integrations/` sont assemblées avec le moteur commun, les documents et l’index ; elles ne sont pas des installations autonomes avant compilation. Voir [la recherche](lookup.md) et [l’organisation](structure.md).
