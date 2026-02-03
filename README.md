# AI Project Template

Reusable template for AI application development projects (LLM apps, RAG, agents).

## Setup
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
# AI Analytics Copilot (Starter)

An **Analytics Copilot for Data Platforms** that converts natural language questions into **SQL + dashboard-ready insights**.

This repo is part of my full-time transition into:
- **AI Product Manager (Data & AI)**
- **AI Application Developer (GenAI / LLM Apps)**

Focused niche: **Data Platforms + Analytics Copilots** (NL→SQL, RAG, Insights).

---

## 🚀 What this Copilot will do (Roadmap)
**Input:** Business question (natural language)  
**Output:** SQL + explanation + insights (and later, charts)

Planned capabilities:
- **NL → SQL generation** for analytics questions
- **SQL execution** on sample datasets (SQLite)
- **Insight summarization** (trend detection, anomalies)
- **RAG Data Dictionary Assistant** (grounded metric definitions)
- Guardrails: SQL validation + safe query patterns
- Evaluation: accuracy checks and test cases

---

## 🧱 Current Status
✅ Day 1 complete:
- Professional repo structure (`src/`, `tests/`, `docs/`, `notebooks/`)
- Starter entry point (`src/main.py`)
- Prompt + SQL output simulation (next: real LLM + SQLite)

---

## 📂 Repo Structure
```text
src/         Application code (copilot logic)
tests/       Unit tests (reliability + guardrails)
notebooks/   Experiments (prompt testing, RAG exploration)
docs/        PRD + architecture notes
