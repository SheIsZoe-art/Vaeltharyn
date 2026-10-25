# Vaeltharyn · SheIsZoe

Langue construite pour la traduction et la chanson · A constructed language for translation and songwriting.

**[Français](docs/fr/README.md) · [English](docs/en/README.md)**

Corpus **1.5.0** · organisation / structure **2.0.0** · plugin **0.5.0**.
65 041 entrées / entries · 65 038 graphies / spellings · 6 538 verbes / verbs.
Les statuts de validation restent propres à chaque fiche. / Approval status belongs to each record.

| Besoin / Need | Accès / Access |
|---|---|
| Installer / Install | [FR](docs/fr/integration/installation.md) · [EN](docs/en/integration/installation.md) |
| Traduire / Translate | [FR](docs/fr/integration/agents.md) · [EN](docs/en/integration/agents.md) |
| Rechercher / Lookup | [FR](docs/fr/integration/lookup.md) · [EN](docs/en/integration/lookup.md) |
| Règles / Rules | [Grammaire](docs/fr/reference/grammar.md) · [Grammar](docs/en/reference/grammar.md) |
| Données / Data | [corpus.json](corpus.json) · [data/](data/) |
| Sources et licences / Sources and licenses | [FR](docs/fr/reference/sources-and-licenses.md) · [EN](docs/en/reference/sources-and-licenses.md) · [LICENSE](LICENSE.md) |
| Anciennes adresses / Old paths | [FR](docs/fr/integration/structure.md) · [EN](docs/en/integration/structure.md) |

```text
python -m vaeltharyn --lang en "synthesizer" "harmonic frequency"
python -m vaeltharyn --lang fr "faim"
python -m vaeltharyn --info
```

Python 3.10+ ; bibliothèque standard uniquement / standard library only.
Premier accès au dépôt : construction automatique de l’index. Les distributions contiennent déjà cet index.
First source lookup builds the index automatically. Distributions include a prebuilt index.

Les nouveautés sont publiées sur `feat/jurons-insultes-fr-en`, dans [PR #2](https://github.com/SheIsZoe-art/Vaeltharyn/pull/2), avant intégration à `main`.
The current additions are published on that branch and PR, pending merge into `main`.
