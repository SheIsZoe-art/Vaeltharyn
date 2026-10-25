# Règles de référence

Le Vaeltharyn est une langue construite. Les définitions enregistrées priment une ressemblance sonore, une étymologie supposée ou une traduction mot à mot.

- Ordre neutre SVO ; VSO uniquement après la particule rituelle `ke`.
- Noms : pluriel `-i`, puis cas `-en`, `-or`, `-ath`, `-ul`. Seul le dernier élément d’un composé nominal est fléchi.
- Adjectifs postposés et invariables ; pas de genre grammatical automatique.
- Verbes : retirer exactement `ar`, puis ajouter marque de temps, mode et personne selon la conjugaison.
- `nu` nie le verbe ; `nul` quantifie le nom ; `sha` intensifie uniquement un adjectif.
- Respecter la valence enregistrée, les sujets des propositions et les antécédents des possessifs.
- Une homographie n’autorise pas à fusionner les sens. Une proposition non validée garde ce statut.
- Les métaphores ne redéfinissent pas les sens physiques. Les hypothèses et les emplacements d’un modèle doivent être résolus avant restitution.

Contrôles : `python scripts/verifier_corpus.py`, puis `python -m unittest discover -s tests`. Ils vérifient les identifiants, alignements FR/EN, références, alias, flexions et cas sémantiques. Les empreintes des données canoniques sont dans `data/provenance/integrity.json`.
