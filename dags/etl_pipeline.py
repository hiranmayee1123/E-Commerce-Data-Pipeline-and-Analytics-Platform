from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
from src.ingestion.extract import extract_data
from src.ingestion.transform import transform_data
from src.ingestion.load import load_data

default_args = {"owner": "airflow", "start_date": datetime(2025, 2, 10)}

dag = DAG("ecommerce_etl", default_args=default_args, schedule_interval="@daily")

extract_task = PythonOperator(task_id="extract", python_callable=extract_data, dag=dag)
transform_task = PythonOperator(task_id="transform", python_callable=transform_data, dag=dag)
load_task = PythonOperator(task_id="load", python_callable=load_data, dag=dag)

extract_task >> transform_task >> load_task
