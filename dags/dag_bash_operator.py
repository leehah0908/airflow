import pendulum
import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator

with DAG(
    dag_id = "dags_bash_operator",     # DAG의 이름 - DAG 파일명과 일치시키는 것이 좋음
    schedule = "0 0 * * *",     # 분 시 일 월 요일
    start_date = pendulum.datetime(2024, 5, 1, tz = "Asia/Seoul"),
    catchup = False,     # start_date와 현재 날짜 사이의 기간동안 돌릴것이냐? False는 안돌린다.
    # 몇분 이상 돌면 타임아웃 오류나게 설정
    # dagrun_timeout = datetime.timedelta(minutes = 60),
    # dag를 찾기 쉽게 만들어주는 태그
    # tags = ["example", "example2"],
    # task에서 공통으로 쓰이는 파라미터 지정
    # params = {"example_key" : "example_value"},
) as dag:
    bash_t1 = BashOperator(
        task_id = "bash_t1",
        bash_command = "echo whoami",
    )

    bash_t2 = BashOperator(
        task_id = "bash_t2",
        bash_command = "echo $HOSTNAME",
    )

    # task 수행 순서
    bash_t1 >> bash_t2
