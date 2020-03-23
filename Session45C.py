# POLYNOMIAL/QUADRATIC REGRESSION

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error, r2_score


df = pd.read_csv('speeds.csv')
print(df)

X = df['hour'].values
Y = df['speed'].values

# ReShape Data so as to train the Mode with 2-D Array
# Transforming 1-D Array into 2-D Array
# X = X.reshape(len(X), 1)
# Y = Y.reshape(len(Y), 1)

# Transforming with numpy
X = X[:, np.newaxis]
Y = Y[:, np.newaxis]

# For sklearn, to work on PolynomialLinear Regression use PolynomialFeatures to transform data
polyFeatures = PolynomialFeatures(degree=2)
polyX = polyFeatures.fit_transform(X)

model = LinearRegression()

# Results into more errors
# model.fit(X, Y)
# y_pred = model.predict(X)

# Results into less errors i.e. highly optimized
model.fit(polyX, Y)
y_pred = model.predict(polyX)

b0 = model.intercept_
b1 = model.coef_

print("Interceptor:", b0)
print("Coefficient:", b1)

rootMeanSquaredError = np.sqrt(mean_squared_error(Y, y_pred))
r2 = r2_score(Y, y_pred)

print("rootMeanSquaredError:", rootMeanSquaredError)
print("r2:", r2)
