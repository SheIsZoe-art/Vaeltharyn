# Recherche et performances

Les recherches exactes et par préfixe utilisent un index SQLite local. Elles ne relisent pas les grands CSV. Grouper plusieurs termes par appel réduit le travail répété et le contexte chargé ; huit fiches par type sont renvoyées par défaut, avec accès aux champs complets par `--full`.

`--contains` parcourt aussi définitions et notes : ce mode reste plus lent. Le premier accès au dépôt crée l’index ; les paquets sont préindexés. L’index occupe davantage de place non compressée que les CSV : l’objectif est le temps de consultation et la fidélité des données.

`python scripts/benchmark_lookup.py` compare les recherches exactes à un parcours linéaire des mêmes fiches, sans ancien commit ni dépendance réseau. Les mesures incluent le démarrage de Python : un passage de chauffe, puis médiane de trois mesures. Le rapport est généré dans `docs/quality/lookup-benchmark.json`. Les temps dépendent de la machine et de son cache.
