# Measured performance

Local comparison with the pre-refactor linear scanner (`90cbfb4`), using the same data. Full CLI wall time including Python startup; one warm-up followed by the median of three measured runs. Results do not guarantee the same timing on another machine.

| Language | Before (ms) | Indexed (ms) | Ratio |
|---|---:|---:|---:|
| fr | 840.43 | 104.62 | ×8.0 |
| en | 1060.29 | 102.96 | ×10.3 |
| vh | 624.72 | 104.68 | ×6.0 |

These measurements cover exact lookup after index construction. `--contains` remains a slower scan. A source checkout builds its index on first access; packages are preindexed. The uncompressed local index is about 337 MB; each downloadable archive is about 36 MB. The optimization targets lookup time and assistant context usage rather than reduced disk space.

Default output is limited to eight records per type and retains useful fields. Complete records remain available with `--full`. The main skill is a concise guide routing to the rules and distinctions needed for the task.

[Measurements and method](../../../distributions/benchmark.json) · Reproduce: `python scripts/benchmark_lookup.py`.
