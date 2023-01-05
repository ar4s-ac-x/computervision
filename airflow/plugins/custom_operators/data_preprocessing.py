from airflow.operators.python_operator import PythonOperator
from airflow.utils.decorators import apply_defaults
from airflow.exceptions import AirflowException

from scripts.preprocess_data import preprocess_data

class DataPreprocessingOperator(PythonOperator):
    @apply_defaults
    def __init__(self, input_path, output_path, *args, **kwargs):
        super(DataPreprocessingOperator, self).__init__(*args, **kwargs)
        self.input_path = input_path
        self.output_path = output_path
    
    def execute(self, context):
        try:
            # Preprocess the data
            preprocess_data(self.input_path, self.output_path)
        except Exception as e:
            raise AirflowException(f'Error while preprocessing data: {e}')
