# POLYNOMIAL/QUADRATIC REGRESSION

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('speeds.csv')
print(df)

X = df['hour'].values
Y = df['speed'].values

# To Validate sample input size and output size
# print(len(X), len(Y))

npModel = np.poly1d(np.polyfit(X, Y, 3))
print(npModel)

# Taking some 100 unknown data points between hour 1 to 24
linearInputPoints = np.linspace(1, 24, 100)
print(linearInputPoints)

# For 100 unknown data points we got predicted output in the form of speed
predictedOutputs = npModel(linearInputPoints)
print(predictedOutputs)

plt.scatter(X, Y, color='red')
plt.plot(linearInputPoints, predictedOutputs, color='green')
plt.show()