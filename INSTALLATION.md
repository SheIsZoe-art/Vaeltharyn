# Installer le traducteur Vaeltharyn

**Plugin 0.4.0 · corpus 1.5.0 · français, anglais et Vaeltharyn.**

Créateur du plugin : **SheIsZoe**.

Le paquet contient le skill de traduction, la grammaire, les deux lexiques détaillés, les 79 expressions initiales, les 226 fiches expressives et les 111 nouvelles fiches sur le son, le corps et les images. Il dispose d’une copie autonome du corpus : aucun compte GitHub ni accès à Obsidian n’est nécessaire après téléchargement. Les dernières propositions linguistiques restent signalées comme non validées.

Le plugin guide une traduction assistée. Son script recherche des mots et des expressions ; ce script ne traduit pas automatiquement une chanson complète. Le paquet n’installe pas de serveur MCP et ne demande aucune clé API.

## Télécharger

- [Paquet complet : vaeltharyn-translator-0.4.0.zip](distributions/vaeltharyn-translator-0.4.0.zip).
- [Empreinte SHA-256 du paquet](distributions/vaeltharyn-translator-0.4.0.zip.sha256).
- [Manifeste du plugin](plugins/vaeltharyn-translator/plugin.json) et [instructions du skill](plugins/vaeltharyn-translator/skills/translate-vaeltharyn/SKILL.md) consultables directement dans le dépôt.

La version du **plugin** et celle du **corpus** sont distinctes : 0.4.0 désigne le paquet ; 1.5.0 désigne l’édition linguistique. Le corpus embarqué provient de la révision [`d30199a`](https://github.com/SheIsZoe-art/Vaeltharyn/commit/d30199ad5a2595aea63688881f301cb6988be21b), sur `feat/jurons-insultes-fr-en`. À la publication de ce guide, cette extension n’est pas encore intégrée à `main`.

## Installer le plugin dans Codex

Prévoir Git, Python 3.10 ou plus récent, et une version de Codex proposant la commande `codex plugin`. L’assistant utilise uniquement la bibliothèque standard Python. Sur Windows, remplacer `python` par `py -3` si c’est la commande disponible.

### 1. Récupérer le dépôt et préparer le paquet

Dans un terminal, depuis le dossier où ranger le projet :

```sh
git clone --branch feat/jurons-insultes-fr-en https://github.com/SheIsZoe-art/Vaeltharyn.git
cd Vaeltharyn
python scripts/installer_plugin.py
```

Si le dépôt existe déjà, utiliser sa copie à jour sur la branche contenant ce guide. Ne pas changer de branche ou écraser des modifications personnelles sans les avoir examinées.

L’assistant vérifie l’empreinte du ZIP, extrait le paquet et crée un catalogue local dans `dist/vaeltharyn-0.4.0/`. Il affiche les deux commandes suivantes avec le chemin absolu approprié. Il ne modifie pas les réglages de Codex et ne remplace pas des fichiers différents déjà présents.

Un emplacement durable peut être choisi explicitement :

```sh
python scripts/installer_plugin.py --destination "/chemin/vers/mes-plugins/vaeltharyn"
```

Sur Windows, un exemple de destination est `"C:\MesPlugins\Vaeltharyn"`. Garder ce dossier après installation : le catalogue local y pointe.

### 2. Ajouter le catalogue et installer

Exécuter les commandes affichées par l’assistant. À partir de la racine du dépôt et avec la destination par défaut, elles correspondent à :

```sh
codex plugin marketplace add ./dist/vaeltharyn-0.4.0
codex plugin add vaeltharyn-translator@vaeltharyn
```

Dans l’application de bureau, rouvrir l’application si le catalogue n’apparaît pas, puis ouvrir les plugins et sélectionner le catalogue **Vaeltharyn**. Cette procédure suit le [format officiel des catalogues locaux Codex](https://developers.openai.com/plugins/build/plugins#install-a-local-plugin-manually).

**Si « Traducteur Vaeltharyn » est déjà installé et affiche 0.4.0, il est déjà à jour pour ce corpus.** Le catalogue local présenté ici permet notamment une installation sur une autre machine. Activer la version souhaitée pour éviter deux traductions concurrentes proposées par deux exemplaires du même plugin.

### 3. Vérifier et utiliser

```sh
codex plugin list --json
```

Vérifier l’entrée `vaeltharyn-translator`, sa version `0.4.0` et son activation. Ouvrir une nouvelle conversation pour charger ses instructions, puis demander par exemple :

```text
Utilise le plugin Traducteur Vaeltharyn pour traduire : « Putain, j’ai faim ! »
```

Le skill fourni s’appelle `translate-vaeltharyn`. Le nom du skill personnel historique, `vaeltharyn-traducteur`, est différent ; il peut aussi être utilisé lorsqu’il est installé séparément.

## Utiliser seulement le ZIP

Après extraction du ZIP, le dossier du plugin doit contenir directement `plugin.json`, `.codex-plugin/` et `skills/`. Ne pas déplacer uniquement `SKILL.md` : les scripts et le corpus sous `references/` lui sont nécessaires.

Pour installer ce dossier dans un client compatible avec les plugins Agent Plugins, utiliser son mécanisme d’import. L’import d’un ZIP n’est pas disponible dans tous les clients ; dans Codex, la procédure par catalogue local ci-dessus évite cette dépendance.

Pour Codex sans clonage Git, créer un dossier dédié de la forme :

```text
mon-catalogue/
  .agents/plugins/marketplace.json
  plugins/vaeltharyn-translator/
    plugin.json
    .codex-plugin/plugin.json
    skills/translate-vaeltharyn/...
```

Extraire le ZIP dans `plugins/vaeltharyn-translator/`, puis créer `marketplace.json` ainsi :

```json
{
  "name": "vaeltharyn",
  "interface": {"displayName": "Vaeltharyn"},
  "plugins": [{
    "name": "vaeltharyn-translator",
    "source": {"source": "local", "path": "./plugins/vaeltharyn-translator"},
    "policy": {"installation": "AVAILABLE", "authentication": "ON_INSTALL"},
    "category": "Productivity"
  }]
}
```

Ajouter ensuite le dossier `mon-catalogue` avec `codex plugin marketplace add`, puis installer `vaeltharyn-translator@vaeltharyn`. Le chemin `source.path` est relatif au dossier du catalogue, pas au fichier JSON.

## Installer uniquement le skill

Cette alternative convient à une installation Codex personnelle sans plugin. Copier le dossier **complet** `skills/translate-vaeltharyn/` du ZIP extrait vers :

- Windows : `%USERPROFILE%\.codex\skills\translate-vaeltharyn\` ;
- macOS/Linux : `~/.codex/skills/translate-vaeltharyn/`.

Le résultat doit contenir `SKILL.md`, `agents/`, `scripts/` et `references/`. Conserver une sauvegarde avant de remplacer une installation existante. Ouvrir une nouvelle conversation et invoquer `$translate-vaeltharyn`.

Ce dossier n’est pas le skill personnel `vaeltharyn-traducteur` déjà installé sur la machine d’origine. Ne pas écraser l’un avec l’autre en changeant seulement le nom du dossier : le nom déclaré dans `SKILL.md` doit correspondre au skill installé.

## Recherche et choix du corpus

Le paquet fonctionne avec son corpus embarqué. Sur la machine d’origine, le script peut utiliser en priorité le dépôt vivant situé dans `C:/Users/user/Documents/ChatGPT/Vaeltharyn/publication-github`. Ailleurs, choisir explicitement un corpus avec `--root` ou `VAELTHARYN_ROOT` pour éviter toute ambiguïté.

Depuis le dossier du skill :

```sh
python scripts/chercher.py --root references/corpus --lang vh slusoemar
python scripts/chercher.py --root references/corpus --lang en badass
python scripts/chercher.py --root references/corpus --lang fr --contains faim
```

La première commande doit retrouver `slusoemar`, verbe transitif « se préoccuper de ». La deuxième doit proposer une lecture admirative de `badass` avec ses notes de sens. `--contains` cherche des candidats ; il ne garantit pas leur équivalence.

Pour un corpus vivant situé ailleurs :

```sh
python scripts/chercher.py --root "/chemin/vers/Vaeltharyn" --lang fr faim
```

Le corpus choisi doit contenir les deux lexiques détaillés et les fichiers d’expressions de l’édition 1.5.0. Une erreur de lecture ne déclenche pas de retour silencieux à une édition ancienne.

## Mettre à jour et résoudre un problème

Pour une nouvelle version, télécharger son paquet et le préparer dans un nouveau dossier dédié, puis utiliser le mécanisme de mise à jour du client. Un catalogue local ne télécharge pas tout seul les nouveaux ZIP du dépôt ; actualiser uniquement le dictionnaire sur GitHub ne modifie pas la copie embarquée.

- **Ancienne description dans une conversation** : vérifier la version installée, puis ouvrir une nouvelle conversation.
- **Catalogue absent** : vérifier la commande `codex plugin marketplace list`, le chemin du catalogue et l’existence de `.agents/plugins/marketplace.json`.
- **`python` introuvable** : utiliser Python 3 installé sur la machine, par exemple `py -3` sur Windows ou `python3` sur macOS/Linux.
- **« Corpus incomplet ou illisible »** : vérifier que tout le ZIP a été extrait ; essayer `--root references/corpus` depuis le dossier du skill.
- **Terme absent** : chercher une expression complète ou employer `--contains`, puis lire les définitions et les notes. Ne pas attribuer arbitrairement un sens français ou anglais à un mot voisin.

## Sources et licence

Le paquet conserve [la licence du projet](LICENSE.md), les [sources et licences linguistiques](18_Sources_et_licences.md), et les [références de l’extension expressive](registres/inventaire-2026-10-25/references/sources.json). Les définitions issues du Wiktionnaire gardent leurs crédits propres. Les scripts et les instructions ne nécessitent pas de redistribution d’identifiants, de clés ou de configuration personnelle.
