---
name: vaeltharyn-traducteur
description: Traduire entre français, anglais et Vaeltharyn avec le corpus indexé 1.6.0, sa grammaire et ses expressions contextualisées ; vérifier une traduction ou préparer des paroles.
---

# Vaeltharyn translator · SheIsZoe

Translate between French, English and Vaeltharyn, preserving meaning, register and grammatical roles. Respond in the user's language and requested format. Corpus **1.6.0**, structure **4.1.0**; entries retain their individual approval status. The canonical source is the repository’s `main` branch. This package is a versioned snapshot; do not claim it is the latest release without checking.

## Find only what the translation needs

The self-contained snapshot is `references/corpus/`; its `corpus.json` lists all resource paths, versions and counts. Start with `python <skill>/scripts/chercher.py --info` if the selected edition is uncertain. `--root` or `VAELTHARYN_ROOT` explicitly selects another corpus; an invalid selection fails without silently falling back. There is no personal filesystem path or network dependency.

Batch exact lookups first; read definitions, valency, register, notes and status. Do not load entire CSVs or archives into context.

```text
python <skill>/scripts/chercher.py --lang en "synthesizer" "harmonic frequency"
python <skill>/scripts/chercher.py --lang fr "faim" "putain de"
python <skill>/scripts/chercher.py --lang vh "saevron" --full
```

Use `--prefix` or `--contains` only to find candidates; the latter scans notes and is slower. Neither proves semantic equivalence or automatically analyzes inflections. Default limit 8, maximum 100. `--full` returns the complete source record. The SQLite snapshot retains all bilingual lexical fields, expression caveats and neutral aliases. A lookup label does not broaden the recorded sense. For corpus editing, use the source repository, not the derived index.

## Read the relevant rules

Paths below are relative to the selected corpus root (bundled: `references/corpus/`). Before a nontrivial translation, read `docs/fr/reference/grammar.md` and `conjugation.md`, or their English equivalents under `docs/en/reference/`. For derivation or lyrics, consult `word-formation.md` and `phonology.md`. For emotion, gestures and dialogue, read `docs/fr/guides/emotions-and-dialogue.md` or its English counterpart. Lexical alias matches carry sense limits; ability is not automatically permission, and silence or desire does not imply consent. Route nuanced meanings to `docs/fr/expressions.md` (English equivalents available). Read `references/translation-cautions.md` for detailed expressive and technical distinctions when relevant.

- SVO; VSO only after ritual `ke`. No automatic grammatical gender. Adjectives follow nouns and remain invariant.
- Noun plural `-i` precedes case `-en/-or/-ath/-ul`. Compound inflection is on the right edge. Pronoun case forms use a hyphen; spatial prepositions take the locative. `ko` means with, not comparative like.
- Remove exactly `ar` from the infinitive. Present endings `em/es/e/om/os/en`; past `ra-`, future `vi-`, moods `ir/el`. Do not drop vowels: `Ti veles`, not `Ti vele`. Shared-subject modal + infinitive; passive only with licensed transitive valency.
- `nu` negates the finite verb; `nul` quantifies a noun; `sha` intensifies an adjective only. Check reflexive possession and clause subjects.
- Fill every angle-bracket slot in `schema_a_completer` before delivery. Distinguish an attested entry, productive formation and proposed neologism. Preserve unestablished senses; never fabricate cultural or sexual facts to translate an insult.

Back-check agents, targets, tense, negation, imagery and intensity. Prefer an attested paraphrase to an improvised root. Keep song sections and repetitions; adapt rhyme or meter only without losing meaning or with an explicit tradeoff. Put French and English under each line when asked. Distinguish performance hints from canonical spelling; written checks do not establish how audio sounds.

Retain attribution in exports: `LICENSE.md` and `docs/{fr,en}/reference/sources-and-licenses.md`. Use the attribution catalogue and license notice for exports. Lookup does not authorize changing the corpus, updating remote files or publishing a translation.
