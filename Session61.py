import pandas as pd
import numpy as np
import math
import random

# 1. Helper Class to Read Data Set and Noramalize the Data
# 2. Create X, Y and Classes from the Data Set
# 3. Make folds of the Data Set

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

        # List of Layers where every Layer is a List of Nodes :)
        # [i, h, o]
        # [[n1, n2, n3, n4, n5, n6, n7], [n1, n2, n3, n4, n5], [n1, n2, n3]]
        self.network = []

        print(">> [ANN] MODEL CREATED")
        print(">> [ANN] MODEL DETAILS INPUT {} OUTPUT {} HIDDEN {}".format(input, output, hidden))
        print(">> [ANN] MODEL NETWORK: ", self.network, len(self.network))

        # In case we have no Hidden Layers:
        if len(hidden) == 0:
            self.network.append(self.createLayer(self.input, self.output))
        # In Case we Have Hidden Layers
        else:
            self.network.append(self.createLayer(self.input, self.hidden[0]))
            # Iterate in Remaining Hidden Layers
            for i in range(1, len( self.hidden)):
                self.network.append(self.createLayer(self.hidden[i-1], self.hidden[i]))

            # Last Hidden Layer must be connected to the Output Layer
            self.network.append(self.createLayer(self.hidden[-1], self.output))


    # Creates A Layer with Nodes :)
    def createLayer(self, input, output):

        random.seed(1)

        layer = []

        for i in range(output):
            weights = [random.random() for _ in range(input)] # Random Weights for Inputs
            node = {
                    "weights": weights,
                    "output": None,
                    "delta": None
                   }
            layer.append(node)

        print(">> [ANN] Layer:", layer)
        print(">> [ANN] CreatedLayer between", input, "and", output)
        return layer

    # Train the Model
    def fit(self, X, Y, epochs):

        # Iterate in n number of epochs to train the model
        for i in range(epochs):
            for (x, y) in zip(X, Y):
                # 1. Feed Forward the Data
                self.feedForward(x)
                # Target converted into one hot encding i.e. where we have target it will be 1 and otherwise 0
                y_one_hot = self.oneHotEncoding(y, self.output)

                self.feedBackward(y_one_hot)
                self.updateWeights(x)

    # Give us Prediction for a particular Input
    def predict(self, X):
        yPred = np.array([np.argmax(self.feedForward(x)) for x in X], dtype=np.int)
        return yPred

    # How Model shall work by exchanging data in between the layers
    def feedForward(self, x):
        # Iterate in Layers
        for layer in self.network:
            output = []

            for node in layer:
                sum = self.summation(inputs=x, weights=node["weights"])
                node["output"] = self.sigmoidActivation(sum)
                output.append(node["output"])

            # Now, we are making x as output which in next iteration serves as input to the next layer
            x = output

        # Final Output of the network shall be returned back :)
        return x

    # Please study the blogs which i shared over the group :)
    # sigmoid and sigmoid derivative
    # Evaluate node[delta] -> sig' = fxn(sig)
    def feedBackward(self, y_one_hot):

        numOfLayers = len(self.network)

        # Iterating Backward
        for i in reversed((range(numOfLayers))):
            # Last Layer
            if i == numOfLayers-1:
                # Iterating in the Last Layer for all the nodes
                for j, node in enumerate(self.network[i]):
                    #       measured - actual
                    error = node['output'] - y_one_hot[j]
                    node['delta'] = error * self.sigmoidActivationDerivation(node['output'])
            # Remaining Previous Layers: Propagate the error backward in the network and compute the delta for the nodes
            else:
                for j, node in enumerate(self.network[i]):
                    #       measured - actual
                    # error = node['output'] - y_one_hot[j]
                    error = sum([ n['weights'][j] * n['delta'] for n in self.network[i+1]])
                    node['delta'] = error * self.sigmoidActivationDerivation(node['output'])


    # Totally based in node['delta']
    def updateWeights(self, x):

        learningRate = 0.5  # This is the amount in which we will update weights

        for i, layer in enumerate(self.network):
            # Read Input Values
            # For 1st Layer inputs are x
            if i == 0:
                inputs = x
            # For remaining layers inputs of current layer become outputs of the previous layer
            else:
                inputs = [node['output'] for node in self.network[i-1]]

            # Update Wights
            # newWeight = - learningRate * (error * activationFxn) * input

            for node in layer:
                for j, input in enumerate(inputs):
                    node['weights'][j] += -learningRate * node['delta'] * input


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

    def oneHotEncoding(self, index, output):
        x = np.zeros(output, dtype=np.int)
        x[index] = 1
        return x

    def printNetwork(self):
        # Print Layers
        for layer in self.network:
            print(">> LAYER DETAILS")
            for node in layer:
                print(node)
            print("~~~~~~~~~~~~~~~")


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

    numberOfObservations, inputFeatures = X.shape           #(210, 7)
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

    # CREATING the MODEL
    # inputFeatures   -> 7
    # numberOfClasses -> 3
    # hidden -> [5] -> only 1 hidden layer with 5 nodes
    # hidden -> [5, 5, 4] -> 3 hidden layer with 1st having 5 nodes, 2nd having 5 nodes, 3rd having 4 nodes
    # model = ANN(input=inputFeatures, output=numberOfClasses, hidden=[5])
    # model.printNetwork()

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

        print("X_train: ", X_train)
        print("X_test", X_test)

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

        print("YPrediction_train", YPrediction_train)
        print("YPrediction_test", YPrediction_test)

        accuracyTrainingScore = 100 * np.sum(Y_train == YPrediction_train) / len(Y_train)
        accuracyTestingScore = 100 * np.sum(Y_test == YPrediction_test) / len(Y_test)

        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(">> MODEL ACCURACY TRAINING for ", i, ":", accuracyTrainingScore)
        print(">> MODEL ACCURACY TESTING for ", i, ":", accuracyTestingScore)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

        accuracyTrainingScores.append(accuracyTrainingScore)
        accuracyTestingScores.append(accuracyTestingScore)

    print()
    print("OVERALL MODEL ACCURACY OVER 4 ITERATIONS")
    print(">> MODEL ACCURACY TRAINING:", sum(accuracyTrainingScores) / len(accuracyTrainingScores))
    print(">> MODEL ACCURACY TESTING:", sum(accuracyTestingScores) / len(accuracyTestingScores))


if __name__ == '__main__':
    main()