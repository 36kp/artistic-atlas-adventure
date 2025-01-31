from gradio import Image
import keras
from keras import layers
from sklearn.model_selection import train_test_split
from PIL import Image
from tensorflow.keras.preprocessing import image
import numpy as np

def getName(index):
    """
    Returns the name of the class corresponding to the given index.
    
    Parameters:
        index (int): The index of the class name to retrieve. Valid values are 0 to 5.
    Returns:
        str: The name of the class if the index is valid, otherwise "Unknown".
    """
    classNames = ["Buildings", "Forest", "Glacier", "Mountain", "Sea", "Street"]
    if index < 0 or index > 5:
        return "Unknown"
    return classNames[index]

def get_optimal_model():
    """
    Creates and compiles a Keras Sequential model with the following architecture:
    - Conv2D layer with 160 filters, kernel size of 3, ReLU activation, and input shape of (150, 150, 3)
    - MaxPooling2D layer with pool size of 2
    - Conv2D layer with 128 filters, kernel size of 3, and ReLU activation
    - MaxPooling2D layer with pool size of 2
    - Conv2D layer with 256 filters, kernel size of 5, and ReLU activation
    - Flatten layer
    - Dense layer with 96 units and ReLU activation
    - Dense layer with 64 units and ReLU activation
    - Dense layer with 1 unit and softmax activation

    The model is compiled with Adam optimizer (learning rate of 0.0001), categorical crossentropy loss, and accuracy metric.

    Returns:
        keras.Sequential: The compiled Keras model.
    """
    model = keras.Sequential()
    model.add(layers.Conv2D(160, 3, activation='relu', input_shape=(150, 150, 3)))
    model.add(layers.MaxPooling2D(2))
    model.add(layers.Conv2D(128, 3, activation='relu'))
    model.add(layers.MaxPooling2D(2))
    model.add(layers.Conv2D(256, 5, activation='relu'))
    model.add(layers.Flatten())
    model.add(layers.Dense(96, activation='relu'))
    model.add(layers.Dense(64, activation='relu'))
    model.add(layers.Dense(1, activation='softmax'))
    model.compile(optimizer=keras.optimizers.Adam(learning_rate=0.0001), loss='categorical_crossentropy', metrics=['accuracy'])
    
    return model

def load_model(fileName):
    """
    Loads a Keras model from a file.

    Args:
        fileName (str): The name of the file (without extension) from which to load the model. The file is expected to be in the '../../model/' directory and have a '.keras' extension.

    Returns:
        keras.Model: The loaded Keras model.
    """
    return keras.models.load_model(fileName)

def run_prediction(filePath):
    """
    Runs image classification on the provided image file.

    Args:
        filePath (str): The path to the image file to be classified.

    Returns:
        str: A string describing the predicted class and the confidence level.
    """
    print("Running prediction")
    model = load_model("../model/tuned_model_randomsearch.keras")

    img = Image.open(filePath)
    img = img.resize((150, 150))

    img_array = image.img_to_array(img)
    img_array = img_array / 255.0 
    img_array = np.expand_dims(img_array, axis=0)

    shape = img_array.shape
    dtype = (img_array.dtype)

    predictions = model.predict(img_array)
    confidence = np.max(predictions)
    predicted_class = np.argmax(predictions)
    return f"""AAA image classification identifies the provided image to be {getName(predicted_class)} with {(confidence*100):.2f}% confidence"""