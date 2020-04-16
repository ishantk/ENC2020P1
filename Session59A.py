import pandas as pd
import numpy as np
import math
import random


class DataSetHelper:

    def __init__(self):
        print(">> [DataSetHelper] Preparing DataSet...")

    """
        Read the CSV File
        Prepare X and Y
        Preapre number of Classes -> len(Y)

        We can even normalize the data
    """

    def readCSVFile(self, file, target, noramlize=False):

        print(">> [DataSetHelper] Processing", file, "to prepare X, Y and numOfClasses")

        # Reading CSV File
        df = pd.read_csv(file)
        # print(df)

        targetIndexes = {target: idx for idx, target in enumerate(sorted(list(set(df[target].values))))}
        # print(targetIndexes)

        X = df.drop([target], axis=1).values
        # print(X)

        Y = np.vectorize(lambda x: targetIndexes[x])(df[target].values)
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

    # n is number of observations in the data set
    # folds -> how many spits we want
    def kFoldCrossValidation(self, n, folds):

        print(">> [DataSetHelper] Creating", folds,"- FOLDS for", n, "records")

        np.random.seed(1)  # Starting number from where randoms shall be generated
        indexes = np.random.permutation(n)

        nFold = int(n / folds)

        indexFolds = []

        for i in range(folds):
            startIdx = i * nFold
            endIdx = min([(i + 1) * nFold, n])

            indexFolds.append(indexes[startIdx:endIdx])

        return indexFolds


class ANN:

    """
        Build the Neural Network
    """
    def __init__(self, input, output, hidden):
        self.input = input
        self.output = output
        self.hidden = hidden
        self.network = []

        print(">> [ANN] MODEL CREATED")
        print(">> [ANN] MODEL DETAILS INPUT {} OUTPUT {} HIDDEN {}".format(input, output, hidden))
        print(">> [ANN] MODEL NETWORK: ", self.network, len(self.network))

    def fit(self, X, Y, epochs):
        pass

    def predict(self, X):
        pass

    # How Model shall work by exchanging data in between the layers
    def feedForward(self):
        pass

    def feedBackward(self):
        pass

    def updateWeights(self):
        pass

    def summation(self, inputs, weights):
        """
        :param inputs:  [1, 2, 3, 4, 5]
        :param weights: [1, 1, 2, 1, 2]

        zip -> [[1, 1], [2, 1], [3, 2], [4, 1], [5, 2]]

        """
        # Dot Product
        return sum([i * w for(i, w) in zip(inputs, weights)])

    def sigmoidActivation(self, sum):
        return 1.0 / (1.0 + math.exp(-sum))

    def sigmoidActivationDerivation(self, sigmoid):
        return sigmoid * (1.0 - sigmoid)

    def oneHotEncoding(self):
        pass


def main():

    fileName = "seeds.csv"

    dsHelper = DataSetHelper()
    X, Y, numberOfClasses = dsHelper.readCSVFile(file=fileName, target="y", noramlize=True)

    print("~~~~~~seeds data set~~~~~~")

    print("X Shape is:", X.shape)
    print("X is:")
    print(X)

    print("Y Shape is:", Y.shape)
    print("Y is:")
    print(Y)

    print("numberOfClasses is:")
    print(numberOfClasses)

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~")

    print()

    numberOfObservations, inputFeatures = X.shape
    print("numberOfObservations:", numberOfObservations)    # 210
    print("inputFeatures:", inputFeatures)                  # 7

    print("ALL Indexes: ")
    index_all = np.arange(0, numberOfObservations)
    print(index_all)    # for 210 records we have indexes as in 0 to 209

    index_folds = dsHelper.kFoldCrossValidation(n=numberOfObservations, folds=4)

    # We got 4 random folds indexes with which we can prepare our data set
    print("FOLD Indexes: ")
    print(index_folds)
    print("FOLDS:", len(index_folds))

    print("~~~~~~~~~~Iterating in FOLDS~~~~~~~~~~")

    accuracyTrainingScores = []
    accuracyTestingScores = []

    # We are iterating in index_folds
    # i will range from 0 to 3 as we have 4 folds
    # index_test will have the random array indexes in the fold
    for i, index_test in enumerate(index_folds):
        print(i)
        print(index_test)
        print()

        # index_test is array for testing data set
        # training data set would be all - test i.e. index_all - index_test

        index_train = np.delete(index_all, index_test)
        print(index_train)

        # We will have 4 folds where we are having our data set randomly divided
        # with testing and training data set
        X_train, Y_train = X[index_train], Y[index_train]
        X_test, Y_test = X[index_test], Y[index_test]

        # CREATING the MODEL
        # inputFeatures   -> 7
        # numberOfClasses -> 3
        model = ANN(input=inputFeatures, output=numberOfClasses, hidden=[5])

        # TRAINING the MODEL
        model.fit(X=X_train, Y=Y_train, epochs=25)

        # Make Predictions for Training Data Set and Testing Data Set
        # i.e. Original Y and Predicted Y on both training and testing
        YPrediction_train = model.predict(X_train)
        YPrediction_test = model.predict(X_test)

        accuracyTrainingScore = 100 * np.sum(Y_train == YPrediction_train) / len(Y_train)
        accuracyTestingScore = 100 * np.sum(Y_test == YPrediction_test) / len(Y_test)

        print(">> MODEL ACCURACY TRAINING for ", i, ":", accuracyTrainingScore)
        print(">> MODEL ACCURACY TESTING for ", i, ":", accuracyTestingScore)

        accuracyTrainingScores.append(accuracyTrainingScore)
        accuracyTestingScores.append(accuracyTestingScore)


    print("OVERALL MODEL ACCURACY OVER 4 ITERATIONS")
    print(">> MODEL ACCURACY TRAINING:", sum(accuracyTrainingScores) / len(accuracyTrainingScores))
    print(">> MODEL ACCURACY TESTING:", sum(accuracyTestingScores) / len(accuracyTestingScores))


if __name__ == '__main__':
    main()