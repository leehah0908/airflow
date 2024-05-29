from airflow import DAG
import pendulum
import datetime
from airflow.operators.python import PythonOperator

with DAG(
    dag_id = "dags_python_task_decorator_v2",
    schedule = "0 2 * * 1",
    start_date = pendulum.datetime(2024, 5, 1, tz = "Asia/Seoul"),
    catchup = False,
) as dag:

    def print_context(*op_args):
        print(*op_args[0])

    # operator 생성
    python_task_1 = PythonOperator(
        task_id = 'python_task_1',
        python_callable = print_context,  # 실행할 파이썬 함수
        op_args = ['todayy']
    )

    python_task_1