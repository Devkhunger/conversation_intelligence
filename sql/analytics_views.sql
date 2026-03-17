-- Aggregated reporting views for conversation intelligence metrics
CREATE OR REPLACE VIEW v_daily_conversation_stats AS
SELECT
    DATE(created_at) AS activity_date,
    COUNT(*) AS total_conversations
FROM conversations
GROUP BY DATE(created_at)
ORDER BY activity_date DESC;
