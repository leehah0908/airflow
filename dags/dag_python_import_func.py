from airflow import DAG
import pendulum
import datetime
from airflow.operators.python import PythonOperator
from py_func.print import get_print

with DAG(
    dag_id = "dags_python_import_func",
    schedule = "30 6 * * *",
    start_date = pendulum.datetime(2024, 5, 1, tz = "Asia/Seoul"),
    catchup = False
) as dag:

    task_get_print = PythonOperator(
        task_id = 'task_get_print',
        python_callable = get_print
    )