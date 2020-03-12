from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import pandas as pd

table = pd.read_csv("advertising.csv")
print(table)

X = table.TV.values
Y = table.Sales.values

# X and Y are 1-D Arrays | 200, 0
print(X, X.shape)
print(Y, Y.shape)

# (scikit library) sklearn shall work on 2d arrays
X = X.reshape(len(X), 1)
Y = Y.reshape(len(Y), 1)

# converted X and Y as 200, 1
print(X, X.shape)
print(Y, Y.shape)

model = LinearRegression()
model.fit(X, Y)

b0 = model.intercept_
b1 = model.coef_

print("Interceptor is:", b0)
print("Coefficient is:", b1)

Y1 = model.predict(X)
print(Y1, Y1.shape)

score = r2_score(Y, Y1)
print(">> R2 Score is:", score)

print(">> Equation of Line: Y = {} + {}X".format(b0, b1))

# You can now directly use this above technique on IPL Data Set