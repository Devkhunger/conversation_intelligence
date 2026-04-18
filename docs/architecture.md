# Architecture Overview

Initial system diagram and service boundaries for backend, ingestion scripts, and database.

## Backend Service
Handles REST endpoints, conversation parsing, and query aggregation.

## Data Flow
Raw transcripts -> `data/scripts` -> PostgreSQL (`init.sql`) -> Backend API.
