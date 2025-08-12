# Portfolio AI Projects

This repo contains two end-to-end **personal** projects demonstrating AI/ML + the modern data stack.

## Projects
- **rag-copilot/** — Retrieval-Augmented Generation (RAG) assistant over public documents using Snowflake + dbt + Airflow + Databricks + Streamlit.
- **ml-forecasting/** — Time-series demand forecasting with SHAP-based insights using Snowflake + dbt + Airflow + Databricks + Power BI.

> **Note:** All code is templated for personal use: no company code/data. Replace placeholders with your credentials and dataset paths.

---

## Quickstart

### 1) Clone & set up
```bash
git clone <YOUR_REPO_URL>.git
cd portfolio-ai-projects
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

### 2) Environment variables (create `.env` in project root)
```
SNOWFLAKE_ACCOUNT=<acct>
SNOWFLAKE_USER=<user>
SNOWFLAKE_PASSWORD=<password>
SNOWFLAKE_ROLE=<role>
SNOWFLAKE_WAREHOUSE=<warehouse>
SNOWFLAKE_DATABASE=<database>
SNOWFLAKE_SCHEMA=<schema>
OPENAI_API_KEY=<key>
```

### 3) Airflow (local, via Docker) – optional
Use `airflow/` in each project for example DAGs. Replace connections in the DAGs or use Airflow UI to set them.

### 4) dbt
Inside each project's `dbt/` folder:
```bash
cd <project>/dbt
pip install -r requirements.txt
dbt debug
dbt run
dbt test
```

### 5) Databricks
Import notebooks from `databricks/` into Community Edition or link via repo integration.

### 6) Apps/Dashboards
- `rag-copilot/app/` — Streamlit app: `streamlit run app.py`
- `ml-forecasting/powerbi/` — Open the PBIX template and point to Snowflake.

---

## Pushing to GitHub
```bash
git init
git add .
git commit -m "Initial commit: RAG + Forecasting portfolio projects"
git branch -M main
git remote add origin https://github.com/<your-username>/portfolio-ai-projects.git
git push -u origin main
```

## License
MIT — see `LICENSE`.

