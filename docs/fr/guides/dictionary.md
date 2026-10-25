# Utiliser le dictionnaire

Les deux CSV détaillés sont alignés par identifiant stable. Consulter les chemins dans `corpus.json` et rechercher une fiche avec `python -m vaeltharyn --lang fr "terme"` ; utiliser `--lang en` ou `--lang vh` pour les autres directions.

Lire la définition complète, la catégorie, la valence, le registre, le statut, la prononciation et les notes. Le libellé de recherche n’élargit pas la définition. Une racine, un composé et une forme fléchie ne sont pas des entrées interchangeables.

`source` conserve l’URL lexicale ou le code `PROJECT`. `source_licence`/`source_license` renvoie au catalogue commun `data/provenance/references.json`. Les sources des définitions françaises sont aussi conservées dans le JSONL de provenance. Les champs de relecture distinguent une proposition, une fiche contrôlée à l’écrit et une validation non documentée.

Le pluriel précède le cas. Les adjectifs sont invariables et postposés. Ne pas déduire un passif d’un verbe intransitif. Les modèles de phrase demandent l’adaptation des pronoms, temps et antécédents au contexte.

Les vues simplifiées sont générées par `python scripts/export_summaries.py` dans `dist/exports/`. Les mots proposés ne doivent pas être présentés comme tous validés individuellement. La réalisation audio ne se déduit pas d’un contrôle écrit.
