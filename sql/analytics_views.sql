-- Aggregated reporting views and index helpers for conversation intelligence
CREATE INDEX IF NOT EXISTS idx_conversations_created_at
    ON conversations (created_at DESC);

CREATE OR REPLACE VIEW v_daily_conversation_stats AS
SELECT
    DATE(created_at) AS activity_date,
    COUNT(*) AS total_conversations
FROM conversations
GROUP BY DATE(created_at)
ORDER BY activity_date DESC;

CREATE OR REPLACE VIEW v_recent_conversations AS
SELECT *
FROM conversations
WHERE created_at >= NOW() - INTERVAL '30 days'
ORDER BY created_at DESC;
