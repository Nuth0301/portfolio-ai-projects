# RAG Copilot (Personal Project)

**Goal:** Retrieval-Augmented Generation assistant over public documents with sources/citations.

**Stack:** Snowflake, dbt, Airflow, Databricks, OpenAI, Streamlit

## Flow
1. Ingest PDFs/HTML/CSV into Snowflake (staged via S3/local).
2. dbt builds `staging` → `intermediate` → `marts` (chunks + embeddings tables).
3. Databricks notebook generates embeddings and writes to Snowflake.
4. Streamlit app retrieves top-k chunks and calls LLM to generate answers with citations.
5. Airflow orchestrates daily ingestion, embedding refresh, and dbt runs.

## Commands
```bash
# dbt
cd dbt
pip install -r requirements.txt
dbt run && dbt test

# App
cd ../app
streamlit run app.py
```
