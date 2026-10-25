# Install the plugin and standalone skill

Creator: **SheIsZoe**. Plugin **0.5.0**, corpus **1.5.0**, structure **2.0.0**. Lookup requires Python 3.10+ and no additional libraries.

Download repository branch `feat/jurons-insultes-fr-en` and open a terminal at its root. [latest.json](../../../distributions/latest.json) identifies the current packages and SHA-256 hashes. Archived releases are historical.

## Codex plugin

The preparer verifies the package, extracts the standalone corpus and creates a dedicated local marketplace:

```text
python scripts/installer_plugin.py
codex plugin marketplace add "<repository>/dist/vaeltharyn-0.5.0"
codex plugin add vaeltharyn-translator@vaeltharyn
codex plugin list --marketplace vaeltharyn --json
```
Replace `<repository>` with the absolute checkout path. Marketplace name remains `vaeltharyn`; plugin name remains `vaeltharyn-translator`. Check that version 0.5.0 is installed and enabled. Start a new chat if necessary to reload instructions.

The preparer does not overwrite an existing different installation. Select a new folder with `--destination`, or back up and replace the **source** directory in the existing marketplace. Then reinstall using supported Codex commands. Do not edit the managed plugin cache directly.

## Standalone skill

Verify the SHA-256 of the [skill archive](../../../distributions/vaeltharyn-skill-1.5.0-structure-2.0.0.zip), then extract its contents into `~/.codex/skills/vaeltharyn-traducteur/`, with `SKILL.md` directly inside that folder. Back up the previous version before replacement. Invoke `$vaeltharyn-traducteur`.

## Verify the bundled corpus

```text
python <skill>/scripts/chercher.py --info
python <skill>/scripts/chercher.py --lang en "harmonic frequency" "exchange for mine"
```
Packages contain all 65,041 entries and 416 expression records in a standalone index. The 719 inventory routes and scope notes are retained. A live checkout is not required. Select the source repository explicitly with `--root <repository>` or `VAELTHARYN_ROOT`. An invalid root fails.

## Build from source

```text
python scripts/build_distribution.py
python scripts/verifier_structure.py
python scripts/verifier_distribution.py
```
The lean sources in `integrations/` are assembled with the shared runtime, documents and index; build them before installing. See [lookup](lookup.md) and [structure](structure.md).
