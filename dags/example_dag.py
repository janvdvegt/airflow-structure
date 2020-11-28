from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator

from airflow.operators.example_plugin import ExampleOperator

from utils.default_arguments import get_default_arguments


with DAG('example_dag', default_args=get_default_arguments()) as dag:
    hello_world_bash = BashOperator(task_id="hello_world_bash",
                                    bash_command="echo hello_world")
    hello_world_python = PythonOperator(task_id="hello_world_python",
                                        python_callable=lambda: print("Hello world"))
    hello_world_custom = ExampleOperator(task_id="hello_world_custom",
                                         custom_parameter="custom world")
                                        
    hello_world_bash >> hello_world_python
    hello_world_bash >> hello_world_custom
