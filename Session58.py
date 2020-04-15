"""
    Prepare DataSet for ANN
"""

import pandas as pd
import numpy as np

class DataSetHelper:

    def __init__(self):
        print("Preparing DataSet...")

    """
        Read the CSV File
        Prepare X and Y
        Preapre number of Classes -> len(Y)
        
        We can even normalize the data
    """
    def readCSVFile(self, file, target, noramlize=False):

        # Reading CSV File
        df = pd.read_csv(file)
        # print(df)

        targetIndexes = {target: idx for idx, target in enumerate(sorted(list(set(df[target].values))))}
        # print(targetIndexes)

        X = df.drop([target], axis=1).values
        # print(X)

        Y = np.vectorize(lambda x : targetIndexes[x])(df[target].values)
        # print(Y)

        classes = targetIndexes.keys()
        # print(classes)

        numberOfClasses = len(targetIndexes)
        # print(numberOfClasses)

        if noramlize:
            # Standardization
            X = (X - X.mean(axis=0)) / X.std(axis=0)

        return X, Y, numberOfClasses


    """
        Make Your Data available as testing and training
        Algo to perform k-Fold CrossValidation (Read More on sklearn)
    """
    def kFoldCrossValidation(self, n, folds):
        np.random.seed(1)   # Starting number from where randoms shall be generated
        indexes = np.random.permutation(n)

        nFold = int(n/folds)

        indexFolds = []

        for i in range(folds):
            startIdx = i*nFold
            endIdx = min([(i+1) * nFold, n])
            indexFolds.append(indexes[startIdx:endIdx])

        return indexFolds
