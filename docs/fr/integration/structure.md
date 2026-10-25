# Organisation et schéma

`corpus.json` décrit le schéma, les versions, les comptes et les chemins canoniques. `main` est la branche de référence.

| Chemin | Fonction |
|---|---|
| `data/lexicon/{fr,en}/entries.csv` | Fiches bilingues alignées par ID |
| `data/expressions/` | Expressions, sens, constructions et alias neutres |
| `data/provenance/references.json` | Catalogue commun des sources et licences |
| `data/provenance/definitions-sourcees.jsonl` | Définitions sources et attributions par ID |
| `docs/{fr,en}/` | Règles et guides fonctionnels |
| `tests/` | Régressions grammaticales et sémantiques |
| `vaeltharyn/` | Moteur commun |
| `integrations/` | Sources du plugin et du skill, métadonnées de téléchargement |
| `dist/`, `.cache/` | Résultats locaux générés, exclus de Git |

Les paquets embarquent l’index, le catalogue des références et les documents de traduction déclarés dans le manifeste. Les CSV, tables d’alias et fiches JSON restent les sources canoniques ; l’index en conserve les champs nécessaires à la consultation. Les empreintes contrôlent ces seules données.
