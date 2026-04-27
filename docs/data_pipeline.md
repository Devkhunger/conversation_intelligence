# Data Ingestion Pipeline

Notes for running batch scripts inside `data/scripts/`.

## Preprocessing Steps
1. Normalize timestamps to UTC.
2. Strip malformed speaker tags.
3. Deduplicate message IDs.

## Error Handling
Failed batches are logged with offset checkpoints for idempotent retries.

## Performance Benchmarks
Batch inserts tuned to 100 rows per transaction to reduce DB lock contention.
