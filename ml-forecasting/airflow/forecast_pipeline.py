from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

def load_sources():
    print("TODO: load demand/weather/calendar to Snowflake")

def run_dbt():
    print("TODO: dbt run && dbt test")

def train_and_score():
    print("TODO: call Databricks notebook or local job")

with DAG(
    dag_id="ml_forecasting_pipeline",
    start_date=datetime(2025, 1, 1),
    schedule_interval="@daily",
    catchup=False,
) as dag:
    t1 = PythonOperator(task_id="load_sources", python_callable=load_sources)
    t2 = PythonOperator(task_id="run_dbt", python_callable=run_dbt)
    t3 = PythonOperator(task_id="train_and_score", python_callable=train_and_score)
    t1 >> t2 >> t3
