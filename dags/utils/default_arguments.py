from datetime import datetime, timedelta


def get_default_arguments():
    """Retrieve default arguments for DAGs, useful for generic settings. By putting it in a method,
    this can be conditioned on the environment

    Returns:
        dict: keyword arguments that are passed to DAGs
    """
    default_arguments = {
        'owner': 'Jan van der Vegt',
        'depends_on_past': False,
        'start_date': datetime(2020, 11, 25),
        'email': ['jan.vegt@gmail.com'],
        'email_on_failure': False,
        'email_on_retry': False,
        'retries': 1,
        'retry_delay': timedelta(minutes=1),
    }
    return default_arguments
