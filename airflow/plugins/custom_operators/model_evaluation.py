from airflow.operators.python_operator import PythonOperator
from airflow.utils.decorators import apply_defaults
from airflow.exceptions import AirflowException

from scripts.eval_model import eval_model

class ModelEvaluationOperator(PythonOperator):
    @apply_defaults
    def __init__(self, model, x_test, y_test, *args, **kwargs):
        super(ModelEvaluationOperator, self).__init__(*args, **kwargs)
        self.model = model
        self.x_test = x_test
        self.y_test = y_test
    
    def execute(self, context):
        try:
            # Evaluate the model
            eval_model(self.model, self.x_test, self.y_test)
        except Exception as e:
            raise AirflowException(f'Error while evaluating model: {e}')
