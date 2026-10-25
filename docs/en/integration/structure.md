# Structure and migration

`corpus.json` is the machine entry point: versions, counts, CSV and registry paths, and FR/EN documents. Do not infer the current version from a historical folder name.

| Directory | Purpose |
|---|---|
| `data/lexicon/{fr,en}/` | Authoritative detailed and summary CSVs |
| `data/expressions/` | Extension records, aliases, sources, checks and licenses |
| `docs/{fr,en}/` | References, guides, examples and integration |
| `archives/` | Earlier editions, reports and releases |
| `integrations/` | Plugin and standalone skill sources |
| `vaeltharyn/` | Shared Python runtime |
| `scripts/` | Build, installation and verification |
| `distributions/` | Current packages, checksums and `latest.json` pointer |
| `.cache/` | Derived local index, excluded from Git |

Data files are relocated byte for byte; IDs and status are preserved. Markdown links are updated. Paths quoted inside historical data remain provenance: resolve them with [legacy-paths.json](../../../archives/legacy-paths.json). The existing `scripts/chercher_corpus.py` CLI is retained; direct file consumers should migrate to the manifest.

The SQLite index retains complete FR/EN records and expression records with their routes. It is derived data, not a new linguistic authority. In a source checkout, changed source characteristics trigger a rebuild. Standalone distributions include the verified index and reference documents, omitting historical volumes and duplicate large CSVs. Edit the corpus in the source repository.
