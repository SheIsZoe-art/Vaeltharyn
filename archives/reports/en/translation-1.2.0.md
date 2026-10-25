> Historical archive: its scope and counts belong to its edition. Use the root `corpus.json` manifest and indexed lookup for the current corpus.

# English translation report

Date: **24 October 2026**. Source: the public French Vaeltharyn corpus, working edition 1.2.0 with the six-entry kingdom supplement.

## Scope

The English edition covers all **65,007 current entries**, the full documentation, direct and reverse historical dictionary volumes, verb paradigms, examples, workshop material, editorial reports, contribution guidance and licence information. New English-sorted and Vaeltharyn-sorted lookup indexes include the six later additions. Historical dictionary volumes keep their original 65,001-entry scope.

Canonical Vaeltharyn forms, lexical IDs, IPA, syllable segmentation, paradigms, original song text and source URLs are retained. French headwords, source definitions, source-definition JSONL and historical JSON reports are intentionally kept as provenance data. Filenames correspond to those of the French edition.

## How the translation was produced

Pronunciation, grammar, conjugation, word formation, the song guide, meaning distinctions, the overview, dictionary overview, six-entry supplement, attribution, licence and contribution guidance were directly translated and checked against the source.

Bulk lexical definitions and the remaining chapters were translated locally with the [Argos Translate](https://github.com/argosopentech/argos-translate) French–English 1.9 model, using CTranslate2. Text was segmented for translation; code, explicit language forms, IDs and source links were protected. The English word indexes were rebuilt from the translated data rather than relabelling a French-sorted index.

**Bulk translations and lookup labels have not all been individually reviewed.** A complete translated edition is not an individually edited English dictionary. Some specialised terms, awkward source definitions or provisional lookup labels may need correction. Read the full definition and compare the French source when uncertain. The translation does not validate the underlying automatically allocated lexical proposals.

## English CSV schema

Files are UTF-8 with semicolon delimiters.

`lexique.csv` contains: `word`, `category`, `domain`, `meaning`, `valency`, `id`. Its first five fields correspond to the five French source fields; the English edition appends the stable ID.

`lexique_detaille.csv` translates human-readable fields and uses English column names. In particular:

| Field | Content |
|---|---|
| word | Unchanged canonical Vaeltharyn lemma |
| id | Unchanged stable lexical identifier |
| category | Unchanged category code |
| meaning | English rendering of the original meaning field |
| definition_en | English rendering of the source definition |
| english_headword | Provisional English lookup label; bounded by the full definition |
| french_headword | Retained French source headword |
| definition_fr_source | Retained French source definition |
| valency_en | English rendering of any expanded source valency description |
| example | Unchanged Vaeltharyn illustrative form or sentence |
| translation | English translation of that example |
| ipa / syllables | Original pronunciation data |
| source / source_sense | Original provenance and selected source sense |
| source_license | Attribution and licence notice; original notices remain in the French edition |
| review | Review status of the underlying lexical entry |
| translation_status | Review status of the English translation |

## Verification

The publication checks compare entry IDs and canonical forms between editions, require a non-empty English definition for every current entry, verify unchanged language and pronunciation fields, verify the verb tables and song text, and check local Markdown links and lexical anchors. Both new indexes must contain every current ID exactly once in each direction.

Machine checks establish coverage and structural consistency; they do not establish perfect semantic equivalence for every definition. The machine-readable publication manifest is [translation_manifest.json](../../audits/en-translation-manifest-1.2.0.json); completed check results are in [translation_checks.json](../../audits/en-translation-checks-1.2.0.json).

## Corrections

Report the lexical ID, English passage, French source and proposed correction. Keep form changes separate from translation changes. See [CONTRIBUTING.md](../../../docs/en/contributing.md).
