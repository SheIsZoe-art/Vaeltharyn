# Structure and schema

`corpus.json` declares schema, versions, counts and canonical paths. `main` is the reference branch.

| Path | Purpose |
|---|---|
| `data/lexicon/{fr,en}/entries.csv` | Bilingual records aligned by ID |
| `data/expressions/` | Register expressions, senses, constructions and neutral aliases |
| `data/provenance/references.json` | Shared source and license catalogue |
| `data/provenance/definitions-sourcees.jsonl` | Source definitions and per-ID attribution |
| `docs/{fr,en}/` | Rules and functional guides |
| `tests/` | Grammatical and semantic regressions |
| `vaeltharyn/` | Shared lookup runtime |
| `integrations/` | Plugin and skill sources, download metadata |
| `dist/`, `.cache/` | Generated local outputs, excluded from Git |

Packages embed the index, reference catalogue and translation documents declared by the manifest. CSVs, alias tables and JSON records remain authoritative; the index retains their lookup fields. Reference hashes cover these canonical inputs only.
