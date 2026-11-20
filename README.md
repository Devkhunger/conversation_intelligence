<div align="center">

# 🗣️ CONVERSATION INTELLIGENCE

### AI Analytical Platform

*A RAG-powered analytical engine for extracting insights, tracking schemas, and querying conversation transcripts with AI.*

[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![React](https://img.shields.io/badge/React-19-61DAFB?style=for-the-badge&logo=react)](https://react.dev/)
[![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?style=for-the-badge&logo=docker)](https://www.docker.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-pgvector-4169E1?style=for-the-badge&logo=postgresql)](https://postgresql.org/)
[![Gemini](https://img.shields.io/badge/Google_Gemini-AI-4285F4?style=for-the-badge&logo=google)](https://ai.google.dev/)

</div>

---

## 🤝 Origin & Credits

This project is based on the original **Conversation Intelligence** codebase by [vichitrarora](https://github.com/vichitrarora), released under the MIT License. The original copyright notice is preserved in the `LICENSE` file.

This repository is my working copy. I use it to study the architecture and to extend it with my own changes, which are listed below.

---

## 🛠️ My Contributions

> Fill this section in only with work you have actually done and committed.
> Each bullet should match a real commit or pull request in this repository.

- [ ] _Example: Added `<feature name>`, which does `<what it does>` (see commit `abc1234`)_
- [ ] _Example: Wrote unit tests for the `/chat` and `/transcript` endpoints_
- [ ] _Example: Fixed `<bug>` in `<file>`_
- [ ] _Example: Documented the API and added a `.env.example`_

---

## 📌 Problem Statement

Analyzing thousands of conversation transcripts manually to uncover customer intents, track resolution schemas, and extract nuanced analytical insights is extremely inefficient. **This platform** addresses this with a LangGraph-powered RAG agent running over a vector database of chunked transcripts. Users can upload transcripts, query conversational histories in natural language, and retrieve structured analytical intelligence backed by context citations.

---

## ✨ Key Features

| Feature | Description |
|---|---|
| **🧠 LangGraph RAG Agent** | Multi-stage reasoning to analyze queries, retrieve relevant transcript chunks, and generate accurate final answers. |
| **🔀 Multi-LLM Orchestration** | Model-agnostic support for Google Gemini, OpenAI, and HuggingFace models. |
| **🔍 Vector Search & Retrieval** | Transcripts are chunked, embedded with Sentence Transformers, and indexed in PostgreSQL using `pgvector` (`VECTOR(768)`). |
| **🗂️ Schema Tracking Engine** | A domain schema agent that maps transcripts to domains, intents, and issue categories. |
| **💬 Threaded Memory** | Agent state keeps context across a session, identifying past queries via `thread_id`. |
| **⚡ Responsive Interface** | A React 19 SPA built on Vite, with a chat-style UI, served via Nginx. |
| **📦 Containerized Setup** | Docker Compose setup with automatic database initialization. |

---

## 🏗️ Architecture

```text
┌──────────────────────────────────────────────────────────────────┐
│                        React 19 + Vite                          │
│               React Markdown │ @google/genai API                │
└────────────────────────────┬─────────────────────────────────────┘
                             │  REST API (JSON)
┌────────────────────────────▼─────────────────────────────────────┐
│                  FastAPI Backend Server                          │
│                                                                  │
│  ┌──────────────┐ ┌──────────────────┐ ┌──────────────────────┐  │
│  │ Chat/Agent   │ │ Transcript Loader│ │ Schema Analyzer      │  │
│  │ Endpoint     │ │ & Batch API      │ │ Service              │  │
│  └──────────────┘ └──────────────────┘ └──────────────────────┘  │
│  ┌──────────────────┐ ┌────────────────┐ ┌────────────────────┐  │
│  │ LangGraph RAG    │ │ External LLMs  │ │ Memory Saver       │  │
│  │ Orchestrator     │ │ (Gemini/OpenAI)│ │ (Checkpointer)     │  │
│  └──────────────────┘ └────────────────┘ └────────────────────┘  │
└──────────────────────────────────────────────────────────────────┘
                             │
                      ┌──────▼───────┐
                      │  PostgreSQL  │
                      │  (pgvector)  │
                      └──────────────┘
```

### Tech Stack

| Layer | Technology |
|---|---|
| **Frontend** | React 19, Vite, TypeScript |
| **Backend** | Python 3.11+, FastAPI, Uvicorn |
| **AI / Graph Engine** | LangGraph, LangChain |
| **Vector DB** | PostgreSQL (`pgvector` extension) |
| **Embeddings** | Sentence Transformers (768d vectors) |
| **LLMs** | Google Gemini (`langchain-google-genai`), OpenAI |
| **Deployment** | Docker, Docker Compose, Nginx |

---

## 📁 Project Structure

```text
project-root/
├── backend/                        # Python FastAPI backend
│   ├── agents/                     # LangGraph specialized agents (e.g. Schema Agent)
│   ├── llm/                        # LLM model configuration and integrations
│   ├── memory/                     # Agent state memory and long-term context
│   ├── nodes/                      # Logic nodes used in the LangGraph workflow
│   ├── utils/                      # DB pools and external connection helpers
│   ├── data/                       # Raw transcript JSON inputs
│   ├── main.py                     # FastAPI entry point and API router
│   ├── graph.py                    # LangGraph workflow definition and compilation
│   ├── state.py                    # Global application state models
│   ├── Dockerfile                  # Backend Docker image configuration
│   └── pyproject.toml              # Python dependencies and package config
├── frontend/                       # React + Vite SPA
│   ├── src/
│   │   ├── components/             # Reusable UI components
│   │   ├── services/               # Backend API client services
│   │   ├── App.tsx                 # Main application shell
│   │   └── types.ts                # Global TypeScript interfaces
│   ├── Dockerfile                  # Multi-stage production Nginx build
│   └── package.json                # Node modules and build scripts
├── init.sql                        # PostgreSQL initialization and vector setup
└── docker-compose.yml              # Multi-container orchestration config
```

---

## 🚀 Quick Start

### Prerequisites

- Docker and Docker Compose installed.
- A valid API key for Google Gemini or OpenAI.

### 1. Clone the Repository

```bash
git clone https://github.com/Devkhunger/conversation_intelligence.git
cd conversation_intelligence
```

### 2. Configure Environment

Create a `.env` file in the project root (it is git-ignored, so never commit it) with your credentials:

```bash
GOOGLE_API_KEY=your-google-api-key
OPENAI_API_KEY=your-openai-api-key
```

A `.env.example` file with placeholder values is a good thing to commit so others know which variables are required.

### 3. Start the Services

```bash
docker-compose up --build -d
```

Services will be available at:
- **Frontend Dashboard:** [http://localhost:8080](http://localhost:8080)
- **Backend API Docs:** [http://localhost:8010/docs](http://localhost:8010/docs)
- **Database Port:** `localhost:5434` (mapped to 5432 inside the container)

---

## 🔗 API Endpoints

| Prefix | Method | Description |
|---|---|---|
| `/chat` | `POST` | Core RAG query endpoint. Takes a `query` and keeps context using the `thread_id` memory tracker. |
| `/transcript` | `POST` | Returns a single full transcript by `transcript_id`. |
| `/transcripts/batch` | `POST` | Returns multiple transcript objects for a list of IDs. |
| `/schema/stats` | `GET` | Returns aggregate domain metadata, intent groupings, and tag vocabularies. |
| `/health` | `GET` | Basic health check for backend uptime. |

---

## 🗄️ Database Initialization

On first startup, Docker runs `init.sql` inside the Postgres `nlp_postgres` container, which enables semantic search:
1. `CREATE EXTENSION IF NOT EXISTS vector;`
2. Creates the tables `transcripts`, `transcript_chunks`, and `transcript_embeddings`.

*(Note: Populating these tables and generating embeddings is done with the ingest scripts in `data/scripts`, using the transcript files in the data folder.)*

---

## 📜 License

This project is licensed under the MIT License. See the `LICENSE` file for details. The original copyright notice must be retained.
