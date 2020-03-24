"""

    Decision Trees
        1. As Classifier
           For Categorical DataSets, where predictions are classes
        2. As Regresser
           For Numerical DataSets, where predictions are real numbers

    Decision Tree Algos:
        To decide which attribute has more information to form tree
        1. Entropy/Information Gain
        2. Gini Index
        3. Chi Square

        1. -> Already Done

        2. Gini Index
            Gini Says, if we select 2 items from a population randomly
            then they must be of same class and probability for this is 1 if population is pure

            eg: Categorical DataSets -> Either target as Play or No Play
                                                         Success or Failure
                                                         Positive or Negative

        Calculation if Gini Index:
            Sum of Square of Probability of P(s)Success and P(f)Failure
            P(s)*P(s) + P(f)*P(f)

            On the Basis of Gender
            Female: P(s) = 0.20
                    P(f) = 0.80 i.e. 1-P(s)
            Male  : P(s) = 0.65
                    P(f) = 0.35 i.e. 1-P(s)

            Gini for Attribute Gender
            Female: (0.20*0.20) + (0.80*0.80) = 0.68
            Male:   (0.65*0.65) + (0.35*0.35) = 0.55

            >> Calculate Weighted Gini for Gender Split
             Weighted Gini = ((10/30) * 0.68) + ((20/30) * 0.55)
                           = 0.59

             Similarly, weighted gini for Class is: 0.51

            [ Gini Impurity = 1 - Gini ]


        3. Chi Square
            Shall find out statistical difference between children and parent node

            Nodes   Play  NotPlay Total ExpectedPlay ExpectedNotPlay
            Female  2     8       10    5            5
            Male    13    7       20    10           10

            Nodes   DeviationPlay(play-expectation)   DeviationNotPlay(not play - expectation)
            Female  -3                                3
            Male     3                               -3

            Chi Square of Node = sqrt (((Actual-Expected) * (Actual-Expected))/Expected )

            Nodes    PlayCricket     NotPlayCricket
            Female   1.34            1.34
            Male     0.95            0.95

            Chi Square of Node Female for Play Cricket -> sqrt ((2 - 5) * (2 - 5))/5
                                                       -> sqrt 9/5
                                                       -> sqrt 1.8
                                                       -> 1.34

            TOTAL CHI SQUARE For Attribute GENDER = 1.34 + 1.34 + 0.95 + 0.95
                                                  = 4.5

            Similarly, Total Chi Square for Class is: 1.45

"""

import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeRegressor
import matplotlib.pyplot as plt
from sklearn import datasets

# Please use other DataSets and explore your DecisionTreeRegressor
# bostonDataSet = datasets.load_boston()
# print(bostonDataSet)

df = pd.read_csv("corona-india-cases.csv")
print(df)

X = df["Day"].values
y = df["Cases"].values

# Transform X and Y
X = X[:, np.newaxis]
y = y[:, np.newaxis]

# Create the Model
model = DecisionTreeRegressor()

# Train the Model
model.fit(X, y)

Y = model.predict(X)

print("Original Cases")
print(y)

print("Predicted Cases")
print(Y)

print("Model Score:", model.score(X, Y))

predictCasesToday = model.predict([[12]])
print(">> Corona Cases Today may be:", predictCasesToday)

plt.figure(figsize=(16, 8))
plt.scatter(X, y, color="red")
plt.plot(X, Y, color="green")
plt.xlabel("Days")
plt.ylabel("Cases")
plt.show()