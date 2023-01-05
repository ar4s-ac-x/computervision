# Machine Learning Model Deployment For ComputerVision

This repository contains scripts and workflows for deploying a machine learning model for computer vision on a Linux based OS.

## Requirements

The following requirements must be installed to run the scripts and workflows:

TensorFlow 2.4.1
OpenCV 4.5.0
NumPy 1.19.4
Node-RED 1.3.6
Airflow 2.0.0

##Setup

1. Clone the repository:

git clone https://github.com/user/repository.git

2. Navigate to the repository directory:

cd repository

3. Install the requirements:

pip install -r requirements.txt


##Workflows

The workflows for training and deploying the model are defined in the model_training_pipeline.py script and can be run using Airflow.

To start the Airflow webserver and scheduler, run the following commands:

airflow webserver
airflow scheduler

The workflows can be accessed and triggered through the Airflow web UI at http://localhost:8080.

##Scripts

The following scripts are included in the repository:

- install_dependencies.sh: Installs the necessary dependencies for running the scripts.
- download_model.sh: Downloads the pre-trained machine learning model.
- preprocess_data.py: Preprocesses the data for training the model.
- train_model.py: Trains the machine learning model on the preprocessed data.
- eval_model.py: Evaluates the performance of the trained model on a test set.
- export_model.py: Exports the trained model for deployment.

##Deployment

The trained model can be deployed using Node-RED. To start the Node-RED server, run the following command:

node-red

The Node-RED flow can be accessed and modified through the web UI at http://localhost:1880.

To deploy the model, follow these steps:

Import the model_exporter.json file into Node-RED. This file contains the exported model and the necessary nodes to deploy it.
Modify the input and output nodes to fit your specific deployment needs.
Deploy the flow by clicking the "Deploy" button in the top right corner of the UI.
The deployed model will now be available for use.

##Notes

Notes
The Dockerfile and docker-compose.yml files are included for deploying the workflows and scripts in a Docker container.
The custom operators for the Airflow workflows are located in the airflow/plugins/custom_operators directory.
The Node-RED settings can be modified in the /node-red/settings.js file.

##Credits

The pre-trained machine learning model was obtained from the TensorFlow Model Zoo.
The computer vision code is based on the OpenCV Python tutorial.
