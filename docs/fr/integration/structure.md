# Organisation et migration

`corpus.json` est le point d’entrée pour les outils. Il donne versions, comptes, chemins des CSV et registres, ainsi que les documents FR/EN. Ne pas déduire la version du nom d’un dossier historique.

| Dossier | Fonction |
|---|---|
| `data/lexicon/{fr,en}/` | CSV détaillés et résumés faisant autorité |
| `data/expressions/` | Fiches, renvois, sources, contrôles et licences par extension |
| `docs/{fr,en}/` | Références, guides, exemples et intégration |
| `archives/` | Anciennes éditions, rapports et distributions |
| `integrations/` | Sources du plugin et du skill |
| `vaeltharyn/` | Moteur Python commun |
| `scripts/` | Compilation, installation et contrôles |
| `distributions/` | Paquets courants, sommes de contrôle et pointeur `latest.json` |
| `.cache/` | Index dérivé local, ignoré par Git |

Les fichiers de données sont déplacés sans modification de leurs octets. Les identifiants et statuts sont conservés. Les liens Markdown sont réadressés. Les chemins cités dans les données historiques restent des traces de provenance : [legacy-paths.json](../../../archives/legacy-paths.json) permet de les résoudre. L’ancienne API en ligne de commande `scripts/chercher_corpus.py` reste disponible ; les consommateurs de fichiers doivent migrer vers le manifeste.

L’index SQLite conserve les fiches FR/EN complètes et les fiches d’expression avec leurs renvois. Il n’est pas une nouvelle source linguistique. Dans le dépôt, il est reconstruit quand les caractéristiques des sources changent. Une distribution autonome contient l’index vérifié et les documents utiles, sans les volumes historiques ni la seconde copie des grands CSV. Pour éditer le corpus, utiliser le dépôt source.
