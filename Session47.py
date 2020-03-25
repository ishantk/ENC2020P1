"""

    Random Forest Algorithm
    1. n -> How many Decision Trees to be Used
    2. DataSet to be divided in n number of instances

    eg: DataSet with 100 records
    choose n as 3 i.e. 3 DecisionTrees
    T1 -> 33
    T2 -> 33
    T3 -> 34

    Prediction from T1, T2 and T3 will be used to make a final prediction

"""

# Working on COVID-19 DataSet
# https://github.com/datasets/covid-19

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import numpy as np

df = pd.read_csv("covid19-world.csv")
print(df)

indiaDF = df[df['Country'] == 'India']
print(indiaDF)

X = indiaDF['Date']
Y = indiaDF['Confirmed']

print("Data for X:", len(X))
print(X)

print()

print("Data for Y:", len(Y))
print(Y)

# plt.plot(X, Y)
# plt.xlabel("Date")
# plt.ylabel("Confirmed Cases")
# plt.grid(True)
# plt.show()

# Formatting Date on X Axis for our Graph :)
fig, ax = plt.subplots()
ax.plot_date(X, Y, marker='', linestyle='-.')
fig.autofmt_xdate()
plt.grid(True)
plt.show()

# we gonna have 100 decision trees on our model who shall work with bagging technique
model = RandomForestRegressor(n_estimators=100)

# Transform X into 2-D Array
X = X[:, np.newaxis]
# model.fit(X, Y) -> Generates Error with X
# Here X is date which is String and we will get error if we train the model with string
# Data Pre Processing
# Before we train the model, refine your data-set optimally so that model works perfectly fine

X1 = pd.to_datetime(indiaDF['Date'], infer_datetime_format=True)
# X1 = pd.to_datetime(indiaDF['Date'], format='%Y-%m-%d')

# We change data type string to datetime which shall be mathematical :)
X1 = X1[:, np.newaxis]
print(X1)
print(type(X1))


x_train, x_test, y_train, y_test = train_test_split(X1, Y, test_size=0.2, random_state=1)

# Train the Model
# model.fit(X1, Y)

model.fit(x_train, y_train)
print(">> Model Trained")

y_pred = model.predict(x_test)
print(x_test)
print(y_pred)

# Convert String dates into DateTime Objects for sklearn
futurePredictionDates = pd.Series(['2020-01-12', '2020-02-12', '2020-03-12', '2020-04-12', '2020-05-12'])
futurePredictionDates = pd.to_datetime(futurePredictionDates, infer_datetime_format=True)

print("~~~~~~~~~~~~~~~~")

# 2-D Array
futurePredictionDates = futurePredictionDates[:, np.newaxis]
futureConfirmedCasesPredictions = model.predict(futurePredictionDates)

print(futurePredictionDates)
print(futureConfirmedCasesPredictions)


# Conclusion : Predictions are not accurate.
# Since as per our dataset, we do have exponential behaviour in our data.
# So we need to do some more of pre-processing

