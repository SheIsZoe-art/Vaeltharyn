# Vaeltharyn · SheIsZoe

Langue construite pour la traduction et la chanson · A constructed language for translation and songwriting.

**[Français](docs/fr/README.md) · [English](docs/en/README.md)**

Corpus **1.6.0** · structure **4.1.0** · plugin **0.8.0**.
**65 045 entrées / entries**, 65 042 graphies / spellings, 6 539 verbes / verbs.
Les statuts de validation sont propres à chaque fiche. / Each record retains its own approval status.

| Besoin / Need | Accès / Access |
|---|---|
| Télécharger / Download | [Release courante / Current release](https://github.com/SheIsZoe-art/Vaeltharyn/releases/latest) |
| Installer / Install | [FR](docs/fr/integration/installation.md) · [EN](docs/en/integration/installation.md) |
| Traduire / Translate | [FR](docs/fr/integration/agents.md) · [EN](docs/en/integration/agents.md) |
| Rechercher / Lookup | [FR](docs/fr/integration/lookup.md) · [EN](docs/en/integration/lookup.md) |
| Grammaire / Grammar | [FR](docs/fr/reference/grammar.md) · [EN](docs/en/reference/grammar.md) |
| Données / Data | [corpus.json](corpus.json) · [data/](data/) |
| Sources et licences / Sources and licenses | [FR](docs/fr/reference/sources-and-licenses.md) · [EN](docs/en/reference/sources-and-licenses.md) · [LICENSE](LICENSE.md) |

```text
python -m vaeltharyn --lang en "synthesizer" "harmonic frequency"
python -m vaeltharyn --lang fr "faim"
python -m vaeltharyn --info
```

Python 3.11+ ; bibliothèque standard uniquement / standard library only.
Le dépôt crée son index au premier accès. Les paquets autonomes sont préindexés.
The checkout builds its index on first lookup; standalone packages are preindexed.

Une seule branche de référence : `main`. Les ZIP et vues CSV simplifiées sont générés ; ils ne sont pas stockés dans Git.
One canonical branch: `main`. ZIP packages and summary CSVs are generated, not tracked in Git.
