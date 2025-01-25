from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
import subprocess

# Define default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
dag = DAG(
    'ecommerce_etl_pipeline',
    default_args=default_args,
    description='ETL pipeline for E-commerce data',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2025, 1, 1),
    catchup=False,
)

# Define Python functions for each task
def run_data_ingestion():
    subprocess.run(['python', 'data_ingestion.py'], check=True)

def run_data_transformation():
    subprocess.run(['python', 'data_transformation.py'], check=True)

# Define tasks
ingestion_task = PythonOperator(
    task_id='data_ingestion',
    python_callable=run_data_ingestion,
    dag=dag,
)

transformation_task = PythonOperator(
    task_id='data_transformation',
    python_callable=run_data_transformation,
    dag=dag,
)

# Set task dependencies
ingestion_task >> transformation_task
