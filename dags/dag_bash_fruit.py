from airflow import DAG
import pendulum
import datetime
from airflow.operators.bash import BashOperator

with DAG(
    dag_id = "dags_bash_select_fruit",
    schedule = "10 0 * * 6#1",     # 매달 첫번째 토요일 0시 10분에 실행
    start_date = pendulum.datetime(2024, 5, 1, tz = "Asia/Seoul"),
    catchup = False
) as dag:
    
    t1_orange = BashOperator(
        task_id = "t1_orange",
        bash_command = "/opt/airflow/plugins/fruit.sh ORANGE",
    )

    t2_avocado = BashOperator(
        task_id = "t2_avocado",
        bash_command = "/opt/airflow/plugins/fruit.sh AVOCADO",
    )

    t1_orange >> t2_avocado