import pandas as pd
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
import numpy as np

# For DataSet
# https://www.kaggle.com/uciml/forest-cover-type-dataset
# https://archive.ics.uci.edu/ml/datasets/Covertype

df = pd.read_csv("covtype.csv")
print(df)

# Extract Features from DataSet
X = df[df.columns[:54]]     # -> 0 to 53

# Target Variable (Classes)
Y = df.Cover_Type

# Split the Data
x_train, x_test, y_train, y_test = train_test_split(X, Y, train_size=0.7, random_state=90)

# Create ANN Model
# Input Layer | Hidden Layer | Output Layer
inputLayer = keras.layers.Dense(64, activation=tf.nn.relu, input_shape=(x_train.shape[1], )) # Shape is Number of Features in your training dat aset
hiddenLayer = keras.layers.Dense(32, activation=tf.nn.relu)
outputLayer = keras.layers.Dense(8, activation=tf.nn.softmax)    #8 classes to be predicted

ann = [inputLayer, hiddenLayer, outputLayer]

model = keras.Sequential(ann)

# Compile the Model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Training the Model
# We are training in 3 iterations. Every iteration will have some results.
history = model.fit(x_train, y_train, epochs=3, batch_size=60)

# history will contain information about loss and accuracy details over each epoch
print("===HISTORY===")
print(history.history.keys())
print(history.history)


print("===OVERALL METRICS===")
# Check for Losses and Accuracy of the OverAll Model
test_loss, test_acc = model.evaluate(x_test, y_test)
print(">> Loss:", test_loss)
print(">> Accuracy:", test_acc)

epochs = [0, 1, 2]
accuracyOverEpochs = history.history["accuracy"]

plt.plot(epochs, accuracyOverEpochs)
plt.xlabel("Epochs")
plt.ylabel("Accuracy")

plt.show()

# Making Predictions
probabilityModel = tf.keras.Sequential([model, tf.keras.layers.Softmax()])
predictions = probabilityModel.predict([x_test])
print(predictions[0])            # List of Probabilities
print(np.argmax(predictions[0])) # Class of Forest

# Assignment:
# Write the same program with a different data set :)