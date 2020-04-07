# https://www.tensorflow.org/tutorials
# ML Problems -> KERAS in Tensorflow

# tf.keras, a high-level API to build and train models in TensorFlow.

# https://www.tensorflow.org/tutorials/keras/classification
import tensorflow as tf
from tensorflow import keras    # for creating and training the model

import numpy as np
import matplotlib.pyplot as plt

# Fashion DataSet -> 70,000 GrayScaled Images
# 10 Categories -> eg: TShirt, Boot etc..
# Resolution is just 28 X 28

# Image Classification | training data and testing data
# 60,000 Images -> To Train the Model
# 10,000 Images -> To Test the Model


# Exploring DataSet
fashionDataSet = keras.datasets.fashion_mnist

# train_images, train_labels    | 60,000
# test_images, test_labels      | 10,000
(train_images, train_labels), (test_images, test_labels) = fashionDataSet.load_data()

print(len(train_images), len(train_labels))
print(len(test_images), len(test_images))

# labels -> 0 to 9

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

print("===Training Image 0===")
print(train_images[0])
print(train_images[0].shape)
print(train_labels[0])
print(class_names[train_labels[0]])

print(train_images[3])
print(train_images[3].shape)
print(train_labels[3])
print(class_names[train_labels[3]])

# Just execute a loop and see some samples in  the dataset :)
plt.subplot(2, 4, 1)
plt.imshow(train_images[0], cmap=plt.cm.gray_r)

plt.subplot(2, 4, 2)
plt.imshow(train_images[3])

# We have sort of obtained image values between the range of 0 to 1 | Fuzzy
train_images = train_images / 255.0
test_images = test_images / 255.0

print(train_images[0])
print(train_images[3])

# plt.show()

# CREATING MODEL

# Create ANN
# Input Layer | Hidden Layer | Output Layer

inputLayer = keras.layers.Flatten(input_shape=(28, 28))
hiddenLayer = keras.layers.Dense(32, activation=tf.nn.relu)
outputLayer = keras.layers.Dense(10, activation=tf.nn.softmax)

ann = [inputLayer, hiddenLayer, outputLayer]

model = keras.Sequential(ann)

# COMPILING MODEL
# https://towardsdatascience.com/adam-latest-trends-in-deep-learning-optimization-6be9a291375c
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# TRAIN THE MODEL
# But here, it is trained multiple times
model.fit(train_images, train_labels, epochs=5)

# Check for Losses and Accuracy of the Model
test_loss, test_acc = model.evaluate(test_images, test_labels)
print(">> Loss:", test_loss)
print(">> Accuracy:", test_acc)


print("===============")

probability_model = tf.keras.Sequential([model, tf.keras.layers.Softmax()])
predictions = probability_model.predict(test_images)

print(np.argmax(predictions[0]), class_names[np.argmax(predictions[0])])
print(test_labels[0], class_names[test_labels[0]])

# Try getting datasets from google exploration for some images on flowers or animals
#  and see of you can predict

"""
Vehicle Detector using Convolutional Neural Networks
Making a Predictive Keyboard using Recurrent Neural Networks
Human Activity Recognition
Credit Card Fraud Detection using Autoencoders in Keras
"""