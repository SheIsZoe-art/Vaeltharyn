# Using the dictionary

Both detailed CSVs are aligned by stable ID. Discover paths through `corpus.json` and query with `python -m vaeltharyn --lang en "term"`; use `--lang fr` or `--lang vh` for the other directions.

Read the full definition, category, valency, register, status, pronunciation and notes. A lookup label does not broaden the definition. A root, compound and inflected form are not interchangeable entries.

`source` retains a lexical URL or the `PROJECT` code. `source_license`/`source_licence` resolves through `data/provenance/references.json`. Original French source definitions are also retained in the provenance JSONL. Review fields distinguish proposals, written checks and undocumented validation.

Plural precedes case. Adjectives are invariant and postnominal. Do not infer a passive from an intransitive verb. Sentence models require contextual pronouns, tense and antecedents.

Generate lightweight views with `python scripts/export_summaries.py` under `dist/exports/`. Do not present all proposed words as individually approved. Written checks do not establish audio performance.
