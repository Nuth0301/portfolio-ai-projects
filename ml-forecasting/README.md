# ML Demand Forecasting & Auto-Insights (Personal Project)

**Goal:** Forecast demand (daily/hourly) and generate driver insights with SHAP + narrative summaries.

**Stack:** Snowflake, dbt, Airflow, Databricks (or Python), Power BI

## Flow
1. Ingest historical demand + weather/calendar into Snowflake.
2. dbt creates clean `dim_*`, `fct_*`, and feature tables.
3. Databricks trains models (e.g., XGBoost/Prophet) and writes predictions back to Snowflake.
4. Power BI reads forecasts, error bands, and SHAP drivers for executive dashboards.
5. Airflow orchestrates hourly/daily runs.

## Commands
```bash
# dbt
cd dbt
pip install -r requirements.txt
dbt run && dbt test
```
