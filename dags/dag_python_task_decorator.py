from airflow import DAG
import pendulum
from airflow.decorators import task

with DAG(
    dag_id = "dags_python_task_decorator",
    schedule = "0 2 * * 1",
    start_date = pendulum.datetime(2024, 5, 1, tz = "Asia/Seoul"),
    catchup = False,
) as dag:
    
    @task(task_id = "python_task_1")
    def print_context(some_input):
        print(some_input)

    python_task_1 = print_context('task_decorator 실행')

    # # 기존 코드였다면?
    # def print_context(*op_args):
    #     print(*op_args[0])

    # # operator 생성
    # python_task_1 = PythonOperator(
    #     task_id = 'python_task_1',
    #     python_callable = print_context,  # 실행할 파이썬 함수
    #     op_args = ['task_decorator 실행']
    # )

    # python_task_1