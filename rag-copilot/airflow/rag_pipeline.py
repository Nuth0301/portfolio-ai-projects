from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

def ingest_docs():
    print("TODO: load docs to Snowflake/S3")

def generate_embeddings():
    print("TODO: call Databricks job to embed chunks")

def run_dbt():
    print("TODO: dbt run && dbt test")

with DAG(
    dag_id="rag_copilot_pipeline",
    start_date=datetime(2025, 1, 1),
    schedule_interval="@daily",
    catchup=False,
) as dag:
    t1 = PythonOperator(task_id="ingest_docs", python_callable=ingest_docs)
    t2 = PythonOperator(task_id="generate_embeddings", python_callable=generate_embeddings)
    t3 = PythonOperator(task_id="run_dbt", python_callable=run_dbt)
    t1 >> t2 >> t3
