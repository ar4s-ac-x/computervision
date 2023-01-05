from airflow.operators.python_operator import PythonOperator
from airflow.utils.decorators import apply_defaults
from airflow.exceptions import AirflowException

from scripts.train_model import train_model

class ModelTrainingOperator(PythonOperator):
    @apply_defaults
    def __init__(self, model, x_train, y_train, epochs, *args, **kwargs):
        super(ModelTrainingOperator, self).__init__(*args, **kwargs)
        self.model = model
        self.x_train = x_train
        self.y_train = y_train
        self.epochs = epochs
    
    def execute(self, context):
        try:
            # Train the model
            train_model(self.model, self.x_train, self.y_train, self.epochs)
        except Exception as e:
            raise AirflowException(f'Error while training model: {e}')
