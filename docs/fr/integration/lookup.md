# Recherche pour les outils

Depuis la racine du dépôt :

```text
python -m vaeltharyn --info
python -m vaeltharyn --lang en "synthesizer" "harmonic frequency"
python -m vaeltharyn --lang vh "saevron" --full
python -m vaeltharyn --lang fr "faim" --limit 4
python -m vaeltharyn --lang en "synth" --prefix
python -m vaeltharyn --lang en "waiting height" --contains
python scripts/chercher_corpus.py --lang en "badass"
```
La sortie JSON contient `edition`, `structure_version`, `mode` et `results`. Chaque terme garde ses comptes `total` et `expression_total`, même quand la réponse est limitée. `entries` donne les définitions bilingues, valence, registre, sources, notes et statut ; `expressions` conserve les réserves et les alias correspondants. `--full` restitue les champs canoniques de la langue sélectionnée et les alias neutres.

La recherche est exacte par défaut, après normalisation Unicode NFC, casse, espaces, apostrophe courbe et ponctuation terminale. `--prefix` cherche les débuts de champs ; `--contains` parcourt aussi définitions et notes, donc coûte davantage. Ces modes trouvent des candidats, pas une preuve d’équivalence. Ils ne lemmatisent pas les formes fléchies. Limite : 8 par défaut, 1 à 100 par type de résultat. Grouper plusieurs termes dans un appel réduit le travail répété et le contexte chargé.

Sélection du corpus : `--root`, puis `VAELTHARYN_ROOT`, puis manifeste près du moteur, puis dossier courant. Une sélection explicite invalide produit une erreur, sans repli silencieux. Les paquets cherchent leur propre `references/corpus/corpus.json` et fonctionnent hors du dépôt. `--build-index` reconstruit l’index du dépôt source. Les recherches suivantes ouvrent l’index en lecture seule. Python 3.11+ suffit, sans dépendance externe.

API Python : `vaeltharyn.search.lookup(root, lang, terms, limit=8, mode='exact', full=False)`. `root` est un `pathlib.Path`. Codes CLI : 0 succès, 2 erreur ou corpus incomplet. Les recherches ne modifient pas les données linguistiques ; seul le cache du dépôt source peut être créé ou rafraîchi.
