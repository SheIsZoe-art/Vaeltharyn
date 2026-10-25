# Integrations / Intégrations

- `plugin/`: plugin identity, interface and embedded skill instructions.
- `skill/`: standalone skill instructions.
- Shared runtime: `../vaeltharyn/`; canonical data discovery: `../corpus.json`.

Les deux variantes utilisent le même moteur et le même corpus indexé. / Both variants use the same runtime and indexed corpus.
Build both with `python scripts/build_distribution.py` from the repository root.
[FR](../docs/fr/integration/installation.md) · [EN](../docs/en/integration/installation.md).
