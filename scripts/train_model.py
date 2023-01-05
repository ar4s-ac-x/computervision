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

def train_model(model, x_train, y_train, x_val, y_val):
    # Train the model
    model.fit(x_train, y_train, validation_data=(x_val, y_val), epochs=10)
    
    # Save the model weights
    model.save_weights('./models/tensorflow/weights.h5')

if __name__ == '__main__':
    # Load the data
    x_train = np.load('./data/tf_records/x_train.npy')
    y_train = np.load('./data/tf_records/y_train.npy')
    x_val = np.load('./data/tf_records/x_val.npy')
    y_val = np.load('./data/tf_records/y_val.npy')
    
    # Create the model
    model = create_model(input_shape=(224, 224, 3))
    
    # Train the model
    train_model(model, x_train, y_train, x_val, y_val)
