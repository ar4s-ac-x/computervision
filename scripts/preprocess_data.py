import os
import cv2
import numpy as np
import pandas as pd

def preprocess_image(image_path):
    # Read the image and resize it to the desired size
    image = cv2.imread(image_path)
    image = cv2.resize(image, (224, 224))
    
    # Normalize the image
    image = image / 255.0
    
    # Convert the image to a numpy array
    image = np.array(image)
    
    return image

def preprocess_data(data_dir):
    # Read the metadata file
    metadata = pd.read_csv(os.path.join(data_dir, 'metadata.csv'))
    
    # Preprocess the images and labels
    images = []
    labels = []
    for index, row in metadata.iterrows():
        image_path = os.path.join(data_dir, 'images', row['image_filename'])
        image = preprocess_image(image_path)
        images.append(image)
        labels.append(row['label'])
        
    # Convert the images and labels to numpy arrays
    images = np.array(images)
    labels = np.array(labels)
    
    return images, labels

if __name__ == '__main__':
    # Set the data directory
    data_dir = './data/raw'
    
    # Preprocess the data
    images, labels = preprocess_data(data_dir)
    
    # Save the preprocessed data to numpy arrays
    np.save('./data/processed/images.npy', images)
    np.save('./data/processed/labels.npy', labels)
