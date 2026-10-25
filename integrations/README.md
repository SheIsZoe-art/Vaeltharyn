# Integrations / Intégrations

- `plugin/plugin.json`: canonical plugin identity and interface, creator **SheIsZoe**.
- `skill/`: the single skill source, with shared instructions, caveats and lookup wrapper.
- `release.json`: current package URLs, versions and SHA-256 hashes.

`python scripts/build_distribution.py` generates both standalone packages, their shared runtime and indexed corpus, plus the Codex compatibility manifest. The embedded skill name is `translate-vaeltharyn`; the standalone name is `vaeltharyn-traducteur`. Their linguistic content is identical.

Les deux variantes sont construites depuis une seule source. Les paquets sont publiés dans une Release ; `dist/` reste hors Git.
[FR](../docs/fr/integration/installation.md) · [EN](../docs/en/integration/installation.md).
