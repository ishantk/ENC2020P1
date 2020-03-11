"""
    Supervised Machine Learning Algo
    Linear Regression -> Predictive Modeling Technique

    Initial Data
    X = [1, 2, 3, 4, 5]
    Y = [2, 4, 5, 4, 5]

    Regression Line | Linear
    Y = b0 + b1X

    Primary Objective : To find the Slope of Line with given data points:)
    i.e. b1 -> since b1 is slope of line

    Mean of X [MX] = 3
    Mean of Y [MY] = 4

    Step1:
    ------------------------------------------------
    X   Y   X-MX    Y-MY    sq(X-MX)    (X-MX)(Y-MY)
    ------------------------------------------------
    1   2   -2      -2      4           4
    2   4   -1       0      1           0
    3   5    0       1      0           0
    4   4    1       0      1           0
    5   5    2       1      4           2
    ------------------------------------------------

    Step2:
    ------------------------------------------------
    Sum of sq(X-MX) =       10
    Sum of (X-MX)(Y-MY) =   6

    To find slope of line:
    b1 = [Sum of (X-MX)(Y-MY)] /  [Sum of sq(X-MX)]
    b1 = 6/10
    b1 = 0.6

    Step3:
    ------------------------------------------------
    Equation of Line is:
    Y = b0 + 0.6 X

    For b0:
    Put mean values of X and Y in equation :)

    4 = b0 + 3 * 0.6
    b0 = 2.2

    =======================
    Final Equation of Line:

    Y = 2.2 + 0.6 X
    =======================

    Now, in case we put a value for X as 6, we will come to know the value of Y
    i.e. Prediction shall work
    But is this prediction accurate or erroneous, i.e. not known to us !!

    Step4:
    ------------------------------------------------
    Calculate Errors
    We need to check if errors are more or less
    if errors are less we are good to go with our model, else we need to work on data or changing the model

    1. Mean Squared Error | MSE *
    2. R2
    3. Variance

    Y = 2.2 + 0.6 X
    For original values of X = [1, 2, 3, 4, 5]
    We will get predicted values of Y call them as Y'

    ------------------------------------------------
    X   Y   Y'   Y-MY    sq(Y-MY)    Y'-MY  Sq(Y'-MY)
    ------------------------------------------------
    1   2   2.8  -2      4          -1.2     1.44
    2   4   3.4   0      0          -0.6     0.36
    3   5   4     1      1           0       0
    4   4   4.6   0      0           0.6     0.36
    5   5   5.2   1      1           1.2     1.44
    ------------------------------------------------

    MSE: [Sum of  Sq(Y'-MY)] /  [Sum of sq(Y-MY)]
    MSE: 3.6/6
    MSE: 0.6

    MSE: 0 ~ 1

"""

import numpy as np

class LinearRegressionModel:

    """
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y
        self.b0 = 0
        self.b1 = 0
    """

    def __init__(self):
        self.b0 = 0
        self.b1 = 0
        self.mse = 0
        self.fitForPrediction = False

    """
    def fit(self, X, Y):
        self.X = X
        self.Y = Y

        meanX = np.mean(self.X)
        meanY = np.mean(self.Y)

        print("MeanX:{} MeanY:{}".format(meanX, meanY))

        valueX = self.X - meanX
        valueY = self.Y - meanY

        print(valueX)
        print(valueY)

        squareX = np.square(valueX)
        squareY = np.square(valueY)

        print(squareX)
        print(squareY)

        self.b1 = np.sum(valueX*valueY) / np.sum(squareX)
        print(">> b1 is:", self.b1)
    """

    def fit(self, X, Y):
        self.X = X
        self.Y = Y

        self.b1 = np.sum((self.X - np.mean(self.X)) * (self.Y - np.mean(self.Y))) / np.sum(np.square(self.X - np.mean(self.X)))
        self.b0 = np.mean(self.Y) - (self.b1 * np.mean(self.X))

        # yRef = lambda x: self.b0 + self.b1 * x
        # Y1 = self.predict(self.X)
        # print(Y1)

        self.mse = np.sum(np.square(self.predictYDash(self.X)-np.mean(self.Y))) / np.sum(np.square(self.Y-np.mean(self.Y)))

        print(">> b1 is:", self.b1)
        print(">> b0 is:", self.b0)
        print(">> Equation of Line: Y = {} + {}X".format(self.b0, self.b1))
        print(">> MSE:", self.mse)

        if self.mse >=0 and self.mse <=1:
            self.fitForPrediction = True
            print(">> Equation of Line: Y = {} + {}X is FIT for Predictions".format(self.b0, self.b1))
        else:
            print(">> Equation of Line: Y = {} + {}X is NOT FIT for Predictions".format(self.b0, self.b1))

    def predictYDash(self, X):
        Y = self.b0 + np.multiply(self.b1, X)
        return Y

    def predict(self, X):
        if self.fitForPrediction == True:
            Y = self.b0 + np.multiply(self.b1, X)
            return Y
        else:
            return -1



def main():
    X = [1, 2, 3, 4, 5]
    Y = [2, 4, 5, 4, 5]

    # Model Creation
    model = LinearRegressionModel()

    # Model Training
    model.fit(X, Y)

    predictedOutput = model.predict(6)
    print(">> Predicted Output for 6 is:", predictedOutput)

if __name__ == '__main__':
    main()
