from airflow.operators.python_operator import PythonOperator
from airflow.utils.decorators import apply_defaults


def print_parameter(custom_parameter):
    print(f"Hello {custom_parameter}")


class ExampleOperator(PythonOperator):
    @apply_defaults
    def __init__(
            self,
            custom_parameter: str,
            *args,
            **kwargs) -> None:
        self.custom_parameter = custom_parameter
        super().__init__(python_callable=print_parameter,
                         op_kwargs={"custom_parameter": custom_parameter},
                         *args,
                         **kwargs)
