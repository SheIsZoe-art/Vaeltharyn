# Dictionary guide

Version 1.1.0 — 2026-10-24, with English-edition notes. Back: [Overview](00_Accueil.md).

## What an entry contains

The **lemma** is the citation form: a singular direct-case noun, an invariable adjective or a verb infinitive in `-ar`. The **meaning** delimits its use. **Valency** indicates whether a verb accepts an object; a beneficiary is dative under the [grammar](02_Grammaire.md). For an unsettled complex construction, write an explanatory proposal rather than copying French or English prepositions.

The French source `lexique.csv` retains its original five columns. The English version uses their English equivalents and appends `id`. The detailed English CSV adds type, base, rule, status, illustrative construction, translation and usage note, plus pronunciation, provenance and translation-review fields. Markdown tables can be read without an Obsidian extension. See [the English schema](TRANSLATION.md).

## Roots, derivatives and compounds

- **Inherited 1.0.0:** a preserved starting entry; the label does not claim that every inherited word is a simple root.
- **Proposed root:** a new registered lemma with a stable definition. A form may echo other words without establishing a decomposition or new rule. Do not confuse proposed lexical units with transparent hyphenated compounds. Any later resegmentation requires a versioned decision.
- **Derivative:** application of an existing rule, with the base and suffix identified. Meaning remains compositional.
- **Compound:** two independent nouns, modifier then head, joined by a hyphen. Only the final element receives number and case.

For later additions, prefer derivation or a transparent compound before inventing a lemma. A registered lexicalised entry retains its meaning even if a tempting decomposition appears possible afterwards.

## Inflection: a complete system, indexes limited to lemmas

Nouns yield ten regular forms: two numbers and five cases. `sael`, `saelen`, `saelor`, `saelath`, `saelul`; `saeli`, `saelien`, `saelior`, `saeliath`, `saeliul`. Pronouns retain their hyphens. Proper names follow their specific rule.

Each verb yields 54 finite forms in [Verb paradigms](09_Paradigmes_des_verbes.md). Imperatives and participles are shown separately. Aspects remain independent words and do not artificially multiply lexical counts. A passive participle requires transitive valency; an intransitive verb does not gain an object merely through suffixation.

## Derivation and limits of meaning

`-eth` on a verb stem names a process, not automatically its product: the act of creating is not the created work. `-or` names a participant in an action, not necessarily a profession. `-va` means “relating to” without turning a noun into an evaluative quality. `-is` expresses manner without adding spatial or temporal meaning. Prefix `ul-` never replaces verbal negation `nu`.

Collisions between new forms and existing lemmas are recorded in `controle_coherence.json`. An occupied form is not automatically overwritten or redefined. Homography with an inflected form may remain possible: readers use context or rephrase; the report lists such cases.

## Register, gender and technical vocabulary

Person nouns do not mark grammatical gender. `nayrvan` can mean a brother or sister; specify gender or kinship when useful. Agent roles do not create reserved professional titles.

Scientific words denote explicitly defined notions, without becoming medical, legal or technical recommendations. Magical words describe a fictional world without asserting real phenomena. Nordic and Celtic vocabulary is an artistic evocation, never historical attestation.

## Writing a text

1. Find the precise sense in the [English index](English_index.md).
2. Read the full definition and category in the linked direct entry; compare the French source if needed.
3. Check valency, case, conjugation and word order.
4. If the sense is missing, try a paraphrase or propose a compound with a definition.
5. Keep the meaning translation; distinguish canonical text from singing transcription.
6. Record each new decision in [Canon and checks](08_Canon_et_controles.md).

Extension 1.1.0 does not constitute individual validation of every proposal. The development request authorised drafting without attributing unmade lexical decisions to the creator.

## Comprehensive edition 1.2.0

The 1.1.0 core remains available. The [comprehensive dictionary](15_Grand_dictionnaire.md) adds a sourced sense, category, calculated pronunciation and review state. Not every entry has a reviewed natural sentence. IPA and stem segmentation are written proposals. Preserve definitions and attribution when sharing. English translation adds another review layer; do not treat a provisional English lookup label as authority to broaden an entry's meaning.

## Valency codes

`tr`: transitive; `intr`: intransitive; `tr/intr`: both uses; `modal`: modal verb; `copule` in retained source data: copula. The English detailed CSV provides `valency_en` for expanded English descriptions while retaining original `valency` data for comparison.

---
[French source](../10_Guide_du_dictionnaire.md). English working translation; see [translation status](TRANSLATION.md).
