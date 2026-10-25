# Install the plugin and skill

Creator: **SheIsZoe**. Plugin **0.8.0**, corpus **1.6.0**, structure **4.1.0**. Python 3.11+ is sufficient, with no additional dependencies.

Download packages from the [current Release](https://github.com/SheIsZoe-art/Vaeltharyn/releases/latest). [release.json](../../../integrations/release.json) also contains exact download URLs and SHA-256 hashes.

## Codex plugin

From a checkout of `main`, the preparer retrieves the current package when needed and verifies its hash:

```text
python scripts/installer_plugin.py
codex plugin marketplace add "<repository>/dist/vaeltharyn-0.8.0"
codex plugin add vaeltharyn-translator@vaeltharyn
codex plugin list --marketplace vaeltharyn --json
```
Replace `<repository>` with the absolute checkout path. For an already downloaded archive, add `--archive <zip-path>`. Different local files are never silently overwritten: choose a new `--destination`, or back up and replace the existing marketplace source before reinstalling through Codex. Do not edit the managed cache.

## Standalone skill

Verify the hash of `vaeltharyn-skill-0.8.0.zip`, then extract it into `~/.codex/skills/vaeltharyn-traducteur/`, with `SKILL.md` directly inside that directory. Back up the previous version and invoke `$vaeltharyn-traducteur`. The plugin embeds the same skill as `translate-vaeltharyn`.

## Verify installation

```text
python <skill>/scripts/chercher.py --info
python <skill>/scripts/chercher.py --lang en "harmonic frequency" "exchange for mine"
```
Packages are self-contained; no live checkout is required. `--root <repository>` or `VAELTHARYN_ROOT` explicitly selects another corpus. Invalid roots fail without silent fallback. A new chat may be needed to load updated instructions. The hosted ChatGPT app is a separate installation from the Codex plugin.

## Build and verify

```text
python scripts/build_distribution.py
python scripts/verifier_corpus.py
python -m unittest discover -s tests
python scripts/verifier_distribution.py
```
ZIPs are generated under `dist/releases/` and published as Release assets rather than tracked in Git. Build the lean `integrations/` sources before installing. See [lookup](lookup.md) and [structure](structure.md).
