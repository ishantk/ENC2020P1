import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

from sklearn.model_selection import train_test_split
from sklearn import metrics

#pip install statsmodels :)
import statsmodels.api as sm


df = pd.read_csv("companies.csv")
print(df)

# Lets Plot Data to Validate Linearity in it :)
"""
plt.scatter(df['R&DSpend'], df['Profit'])
plt.title('R&DSpend VS Profit', fontsize=14)
plt.xlabel('R&DSpend', fontsize=14)
plt.ylabel('Profit', fontsize=14)
plt.grid(True)
plt.show()

plt.scatter(df['MarketingSpend'], df['Profit'])
plt.title('MarketingSpend VS Profit', fontsize=14)
plt.xlabel('MarketingSpend', fontsize=14)
plt.ylabel('Profit', fontsize=14)
plt.grid(True)
plt.show()
"""

# X is independent variable
# Represents x1 and x2 to determine y
X = df[['R&DSpend', 'MarketingSpend']]
Y = df['Profit']

print("X is:")
print(X)

print()

print("Y is:")
print(Y)

# We are suppose to solve this equation
# Y = b0 + b1*X1 + b2*X2
# Profit = b0 + b1*R&DSpend + b2*MarketingSpend

# Create a Linear Regression Model
model = LinearRegression()

# SPLIT DATASET
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=1)

# Train the Model with Data
# PS: X is basically x1, x2
# model.fit(X, Y)

model.fit(x_train, y_train)

y_pred = model.predict(x_test)
print(y_pred)

# May not work for every model in the same manner :(
# Percentage Score :) How Accurate the Model IS ?
# print(">> Accuracy Score:", metrics.accuracy_score(y_test, y_pred))

print("Interceptor:", model.intercept_)
print("Coefficients:", model.coef_)

print("Profit = {} + {}*R&DSpend + {}*MarketingSpend".format(model.intercept_, model.coef_[0], model.coef_[1]))

RDSpend = 144372.41
MKSpend = 383199.62

predictedProfit = model.predict([[RDSpend, MKSpend]])
print(predictedProfit)  # REAL VALUE: 182901.99 | PREDICTED VALUE: 173441.30


# PS: https://en.wikipedia.org/wiki/Linear_least_squares
# OLS, WLS, GLS | Statistical Mathematics :)

# Stats Model, adds up constants to our inputs to work

print(X)
print("~~~~~~~~~~~~~~~~~~")
X = sm.add_constant(X)
print("~~~~~~~~~~~~~~~~~~")
print(X)

smModel = sm.OLS(Y, X).fit()        # Remember : input (Y), output(X) in API
predctions = smModel.predict(X)

printModel = smModel.summary()
print(printModel)