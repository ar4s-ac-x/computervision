import tensorflow as tf

def create_model(input_shape):
    # Create the model
    model = tf.keras.Sequential()
    
    # Add the input layer and the first hidden layer
    model.add(tf.keras.layers.Input(shape=input_shape))
    model.add(tf.keras.layers.Conv2D(32, kernel_size=(3, 3), activation='relu'))
    model.add(tf.keras.layers.MaxPooling2D(pool_size=(2, 2)))
    
    # Add the second hidden layer
    model.add(tf.keras.layers.Conv2D(64, kernel_size=(3, 3), activation='relu'))
    model.add(tf.keras.layers.MaxPooling2D(pool_size=(2, 2)))
    
    # Flatten the output of the convolutional layers
    model.add(tf.keras.layers.Flatten())
    
    # Add the output layer
    model.add(tf.keras.layers.Dense(10, activation='softmax'))
    
    # Compile the model
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    
    return model

def export_model(model, export_path):
    # Save the model as a TensorFlow SavedModel
    tf.saved_model.save(model, export_path)

if __name__ == '__main__':
    # Load the model weights
    model = create_model(input_shape=(224, 224, 3))
    model.load_weights('./models/tensorflow/weights.h5')
    
    # Export the model
    export_model(model, './models/tensorflow/saved_model')
