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

X = indiaDF['Date'].values
cases = indiaDF['Confirmed'].values


# As per Data Pre-Processing, we will convert date into day of year hence, making it a mathematical number :)
days = []

for date in X:
    print(date)
    print(pd.Period(date, freq='D').dayofyear)
    days.append(pd.Period(date, freq='D').dayofyear)

days = np.array(days)
print(days)

# Solve the above use case with lambdas

# Formatting Date on X Axis for our Graph :)
# fig, ax = plt.subplots()
# ax.plot_date(days, cases, marker='', linestyle='-.')
# fig.autofmt_xdate()
# plt.grid(True)
# plt.show()


# we gonna have 100 decision trees on our model who shall work with bagging technique
model = RandomForestRegressor(n_estimators=100)

days = days[:, np.newaxis]
x_train, x_test, y_train, y_test = train_test_split(days, cases, test_size=0.2, random_state=1)


# Train the model with day as X and cases as Y
model.fit(x_train, y_train)
y_pred = model.predict(x_test)

print(x_test)
print(y_pred)

print("~~~~~~~~~~~~~~~~~~~")

futurePredictionDays = np.array([12, 24, 48, 96, 120])
futurePredictionDays = futurePredictionDays[:, np.newaxis]

futureConfirmedCasesPredictions = model.predict(futurePredictionDays)
print(futurePredictionDays)
print(futureConfirmedCasesPredictions)

# Conclusion : Predictions are not accurate.
# Since as per our dataset, we do have exponential behaviour in our data.
# So we need to do some more of pre-processing


