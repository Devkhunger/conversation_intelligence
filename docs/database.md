# Database Schema Notes

Documenting tables initialized via `init.sql` and indexing strategy.

## Indexing Strategy
- Index `conversation_id` for fast thread lookups.
- Index `created_at` for time-range filtering.

## Data Retention
Raw payloads archived after aggregation; processed metrics retained indefinitely.

## Migrations
Keep `init.sql` aligned with incremental schema updates during early dev.
