import numpy as np

# PERCEPTRON AS LOGICAL AND/OR OPERATION

class Perceptron:

    def __init__(self):

        self.weights = np.array([1, 1])

        # Assuming Threshold
        self.theta = 0

        print(">> Perceptron Created")

    def setInputs(self, inputs):
        self.inputs = inputs

    # Sum of Inputs*Weights
    # External Bias as Input
    def summation(self, bias):
        self.sum = np.dot(self.inputs, self.weights) + bias
        # print(">> summation is:", self.sum)

    # Binary Step Activation Function
    def activation(self):
        if self.sum >= self.theta:
            return 1
        else:
            return 0


def main():
    # Array Of Inputs
    #                  X1 X2
    input1 = np.array([0, 0])
    input2 = np.array([0, 1])
    input3 = np.array([1, 0])
    input4 = np.array([1, 1])

    # Create Perceptron
    perceptron = Perceptron()

    # Assumption
    # bias = -1.5   #LOGICAL AND
    bias = -0.5       #LOGICAL OR
    # Set Inputs
    perceptron.setInputs(input1)
    perceptron.summation(bias)
    print("For {} Result is: {}".format("0, 0", perceptron.activation()))

    perceptron.setInputs(input2)
    perceptron.summation(bias)
    print("For {} Result is: {}".format("0, 1", perceptron.activation()))

    perceptron.setInputs(input3)
    perceptron.summation(bias)
    print("For {} Result is: {}".format("1, 0", perceptron.activation()))

    perceptron.setInputs(input4)
    perceptron.summation(bias)
    print("For {} Result is: {}".format("1, 1", perceptron.activation()))

if __name__ == '__main__':
    main()

# Assignment: Implement Logical NOT with bias :)