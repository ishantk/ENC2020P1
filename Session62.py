"""
Regression with ANN
DataSet cars.csv -> Predicting sales value from the features

Data PreProcessing -> https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html

"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from tensorflow import keras

# Step1: Preparing and Pre-Processing the Data

df = pd.read_csv("cars.csv")
print(df)

dataSet = df.values

X = dataSet[:, 0:5]
Y = df.sales.values

print(">> FEATURES")
print(X)

print(">> TARGET")
print(Y)
print(Y.shape)

print("==RESHAPING Y==")

Y = np.reshape(Y, (-1, 1))

print(Y)
print(Y.shape)

scalerFeatures = MinMaxScaler()
scalerTarget = MinMaxScaler()

scalerFeatures.fit(X)
scalerTarget.fit(Y)

XScale = scalerFeatures.transform(X)
YScale = scalerTarget.transform(Y)

print(">> TRANSFORMED FEATURES")
print(XScale)

print(">> TRANSFORMED TARGET")
print(YScale)

# Preparing Training and Testing Data
X_train, X_test, Y_train, Y_test = train_test_split(XScale, YScale)

# Step2: Creating ANN Model for Regression
# Input Layer -> Hidden Layer -> Output Layer
# 5              4                1
# PS: If we choose any extra neurons, during the training process, with every epoch it gets optimized and unwanted neurons or layers are removed
#     We can always try to increase or decrease
#       1. neurons
#       2. hidden layers
#     To Achieve our desired results -> HIT and TRY

# Sequential -> ANN with Feed Forward and Back Propagation Algo
model = keras.Sequential()
model.add(keras.layers.Dense(12, input_dim=5, activation='relu'))   # Input Layer
model.add(keras.layers.Dense(8, activation='relu'))                 # Hidden Layer
model.add(keras.layers.Dense(1, activation='linear'))               # Hidden Layer

print("OUR ANN MODEL:")
print(model.summary())

# Compile the Model
model.compile(loss='mse', optimizer='adam', metrics=['mse', 'mae'])

# Training the Model -> We will get a history object
history = model.fit(XScale, YScale, epochs=25, batch_size=60, validation_split=0.2)

XToBePredicted = np.array([[40, 1, 15, 7254, 6472]])
XToBePredictedTransformed = scalerFeatures.transform(XToBePredicted)
YPredicted = model.predict(XToBePredictedTransformed) # it will be in MinMaxScaler i.e. range between 0 to 1

# Invert Normalization i.e. get the real value again
YPredicted = scalerTarget.inverse_transform(YPredicted)
print(">> FOR X:{} PREDICTION Y:{}".format(XToBePredicted, YPredicted))

print(history.history.keys())
# Plot the Losses with each epoch in our ANN Model
plt.plot(history.history['loss'], label='training')           # Loss with Training Data
plt.plot(history.history['val_loss'], label='validation')       # Loss with Testing/Validation Data
plt.legend()
plt.title("MODEL LOSS PLOT")
plt.xlabel('epoch')
plt.ylabel('loss')
plt.show()