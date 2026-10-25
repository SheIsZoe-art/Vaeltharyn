# Lookup and performance

Exact and prefix searches use a local SQLite index instead of rereading large CSVs. Batch terms to reduce repeated work and assistant context; default output is eight records per type, with complete records available through `--full`.

`--contains` also scans notes and definitions and remains slower. First source lookup builds the index; packages are preindexed. Uncompressed index size exceeds the CSV size: the goal is lookup speed and data fidelity.

`python scripts/benchmark_lookup.py` compares exact searches with a linear scan of the same records, without historical commits or network access. Measurements include Python startup: one warm-up and the median of three measured runs. Results are generated in `docs/quality/lookup-benchmark.json` and depend on the machine and its cache.
