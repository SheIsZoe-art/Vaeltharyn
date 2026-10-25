# Reference rules

Vaeltharyn is a constructed language. Recorded definitions take precedence over sound resemblance, assumed etymology or word-for-word replacement.

- Neutral order is SVO; VSO is licensed only after ritual `ke`.
- Nouns take plural `-i` before case `-en`, `-or`, `-ath`, `-ul`. Nominal compounds inflect at the right edge.
- Adjectives follow nouns and remain invariant; no automatic grammatical gender.
- Remove exactly `ar` from infinitives, then apply tense, mood and person according to the conjugation rules.
- `nu` negates a verb, `nul` quantifies a noun, and `sha` intensifies an adjective only.
- Preserve recorded valency, clause subjects and possessive antecedents.
- Homographs do not license merging senses. Unvalidated proposals retain their status.
- Metaphors do not redefine physical senses. Resolve model assumptions and slots before delivery.

Run `python scripts/verifier_corpus.py` and `python -m unittest discover -s tests` to check IDs, bilingual alignment, references, aliases, inflection and semantic cases. Canonical source hashes are in `data/provenance/integrity.json`.
