# API Specification

## `GET /health`
Returns service status and DB connectivity.

## `POST /conversations/ingest`
Accepts structured transcript payloads for processing.

## `GET /conversations/{id}/insights`
Returns extracted topics, sentiment, and summary metrics.

## Error Responses
Standardized `400`, `404`, and `422` JSON payloads with error codes.
