"""
    K-Fold Validation
    We have DataSet, assume 100 observations
    Observation eg:
    [1, 2]  [1]

    x1, x2, y
    1, 2,   1

    We will divide the data set into 4 parts randomly

    FOLD  Number of Observation
    fold1 25
    fold2 25
    fold3 25
    fold4 25

    We will train the model with all the 4 folds
    so as to have a much better accuracy as compared to previous approaches

    For 100 observations,
    70:30
    70 for training and 30 for testing

    In K-Fold Approach
    We are using all the records and dividing further 4 of the records as testing and training

    DataSet:
    x1, x2, y
0   1, 2,   1
1   3, 4,   2
2   1, 2,   3
3   3, 4,   4

DataSet spit happens on the basis of the indexes

"""

import numpy as np
from sklearn.model_selection import KFold



X = np.array([[1, 2], [3, 4], [1, 2], [3, 4]]) # Input Features
Y = np.array([1, 2, 3, 4])                     # Targets

kFold = KFold(n_splits=2)
print("Splits:", kFold.get_n_splits())

for train_index, test_index in kFold.split(X, Y):

    print("~~~~~~~~~~Indexes~~~~~~~~~~~~")
    print(train_index, test_index)
    print("~~~~~~~~~~~~~~~~~~~~~~")

    X_train, X_test = X[train_index], X[test_index]
    Y_train, Y_test = Y[train_index], Y[test_index]

    print("~~~~~~~~~~FOLD~~~~~~~~~~~~")
    print(X_train, X_test)
    print(Y_train, Y_test)
    print("~~~~~~~~~~~~~~~~~~~~~~")

    print()
