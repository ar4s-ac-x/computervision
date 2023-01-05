#!/usr/bin/env bash

# Update package manager and install dependencies
apt-get update
apt-get install -y python3 python3-pip python3-dev build-essential libssl-dev libffi-dev libpq-dev

# Install Node.js and npm
curl -sL https://deb.nodesource.com/setup_14.x | bash -
apt-get install -y nodejs

# Install TensorFlow and other Python packages
pip3 install tensorflow==2.4.0
pip3 install numpy pandas scikit-learn matplotlib opencv-python

# Install Airflow and its dependencies
pip3 install apache-airflow[postgres,redis]

# Install Node-RED
npm install -g --unsafe-perm node-red

# Create the airflow home directory and set the correct permissions
mkdir /usr/local/airflow
chown -R airflow:airflow /usr/local/airflow
