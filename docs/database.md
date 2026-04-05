# Database Schema Notes

Documenting tables initialized via `init.sql` and indexing strategy.

## Indexing Strategy
- Index `conversation_id` for fast thread lookups.
- Index `created_at` for time-range filtering.
