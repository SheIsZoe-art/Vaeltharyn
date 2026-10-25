# Lookup for tools

From the repository root:

```text
python -m vaeltharyn --info
python -m vaeltharyn --lang en "synthesizer" "harmonic frequency"
python -m vaeltharyn --lang vh "saevron" --full
python -m vaeltharyn --lang fr "faim" --limit 4
python -m vaeltharyn --lang en "synth" --prefix
python -m vaeltharyn --lang en "waiting height" --contains
python scripts/chercher_corpus.py --lang en "badass"
```
JSON output contains `edition`, `structure_version`, `mode` and `results`. Each term retains `total` and `expression_total` even when output is limited. `entries` includes bilingual definitions, valency, register, sources, notes and status. `expressions` retains caveats and matching source routes. `--full` returns every original column for the selected language and all expression fields.

Default matching is exact after Unicode NFC, case, whitespace, curly apostrophe and terminal punctuation normalization. `--prefix` matches field beginnings; `--contains` also scans definitions and notes and is consequently slower. These modes find candidates, not proven equivalences. Inflected forms are not lemmatized automatically. Default limit: 8; allowed range: 1–100 per result type. Batch several terms in one invocation to reduce repeated work and context usage.

Corpus selection: `--root`, then `VAELTHARYN_ROOT`, then a manifest near the runtime, then the current directory. Invalid explicit selection fails without silent fallback. Packages find their own `references/corpus/corpus.json` and work outside the checkout. `--build-index` rebuilds a source checkout index. Subsequent lookups open it read-only. Python 3.10+ is sufficient; no external dependencies.

Python API: `vaeltharyn.search.lookup(root, lang, terms, limit=8, mode='exact', full=False)`, with `root` a `pathlib.Path`. CLI exit codes: 0 success, 2 error or incomplete corpus. Lookups do not change linguistic data; only the source checkout cache may be created or refreshed.
