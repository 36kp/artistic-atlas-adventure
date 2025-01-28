import os
import numpy as np
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array



def get_color_means(directory):
    means = []

    print("Calculating color means for images in directory: ", directory)
    for subdir, _, files in os.walk(directory):
        for file in files:
            if file.endswith(('jpeg', 'jpg', 'png')):
                img_path = os.path.join(subdir, file)
                img = load_img(img_path, target_size=(150, 150))
                img_array = img_to_array(img) / 255.0
                means.append(img_array.mean(axis=(0, 1)))


    print("Means: ", means)             
    return np.array(means)