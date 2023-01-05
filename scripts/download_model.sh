#!/usr/bin/env bash

# Download the model !!!REPLACE THE URL WITH YOUR MODEL-URL!!!
curl -L -o model.tar.gz https://storage.googleapis.com/my-model-bucket/model.tar.gz

# Extract the model
tar -xzvf model.tar.gz -C ./models/tensorflow

# Remove the tarball
rm model.tar.gz
