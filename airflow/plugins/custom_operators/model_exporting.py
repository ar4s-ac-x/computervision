from airflow.operators.python_operator import PythonOperator
from airflow.utils.decorators import apply_defaults
from airflow.exceptions import AirflowException

from scripts.export_model import export_model

class ModelExportingOperator(PythonOperator):
    @apply_defaults
    def __init__(self, model, output_path, *args, **kwargs):
        super(ModelExportingOperator, self).__init__(*args, **kwargs)
        self.model = model
        self.output_path = output_path
    
    def execute(self, context):
        try:
            # Export the model
            export_model(self.model, self.output_path)
        except Exception as e:
            raise AirflowException(f'Error while exporting model: {e}')
