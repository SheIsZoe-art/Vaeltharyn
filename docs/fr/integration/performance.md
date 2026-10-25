# Performances mesurées

Comparaison locale avec la recherche linéaire avant refonte (`90cbfb4`), sur les mêmes données. Temps complet de la commande, démarrage Python inclus ; un passage de chauffe puis médiane de trois mesures. Ces résultats ne garantissent pas les mêmes temps sur une autre machine.

| Langue | Avant (ms) | Index (ms) | Rapport |
|---|---:|---:|---:|
| fr | 840.43 | 104.62 | ×8.0 |
| en | 1060.29 | 102.96 | ×10.3 |
| vh | 624.72 | 104.68 | ×6.0 |

Ces mesures concernent les recherches exactes, après construction de l’index. `--contains` reste un parcours plus lent. Dans le dépôt source, le premier accès construit l’index ; les paquets sont préindexés. Le fichier local non compressé occupe environ 337 Mo ; chaque archive téléchargeable environ 36 Mo. L’optimisation vise surtout le temps de recherche et le contexte chargé par l’assistant, pas une réduction de la taille sur disque.

Les réponses courantes sont limitées à huit fiches par type et renvoient les champs utiles. Les enregistrements complets restent disponibles avec `--full`. Le skill principal devient un guide court qui oriente vers les règles et les distinctions utiles.

[Données et méthode](../../../distributions/benchmark.json) · Reproduire : `python scripts/benchmark_lookup.py`.
