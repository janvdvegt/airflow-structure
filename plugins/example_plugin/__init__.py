from airflow.plugins_manager import AirflowPlugin
from example_plugin.operators.example_operator import ExampleOperator


class ExamplePlugin(AirflowPlugin):
    name = "example_plugin"
    operators = [ExampleOperator]
    sensors = []
    hooks = []
    executors = []
    macros = []
    admin_views = []
    flask_blueprints = []
    menu_links = []
    appbuilder_views = []
    appbuilder_menu_items = []
    global_operator_extra_links = []
    operator_extra_links = []