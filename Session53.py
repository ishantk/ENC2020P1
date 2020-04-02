import numpy as np

# PERCEPTRON AS LOGICAL AND/OR OPERATION

class Perceptron:

    def __init__(self):

        # Assuming Weights: Pereptron as Logical AND
        # self.weights = np.array([0.5, 0.5])

        # Assuming Weights: Pereptron as Logical OR
        self.weights = np.array([1.1, 1.1])

        # Weights may be assumed by hit and trial method to get our expected outputs
        # We can also manipulate threshold theta to get our expected outputs
        # We can even add an external input called bias to manipulate results as per our expectation

        # Assuming Threshold
        self.theta = 1

        print(">> Perceptron Created")

    def setInputs(self, inputs):
        self.inputs = inputs

    # Sum of Inputs*Weights
    def summation(self):
        self.sum = np.dot(self.inputs, self.weights)
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

    # Set Inputs
    perceptron.setInputs(input1)
    perceptron.summation()
    print("For {} Result is: {}".format("0, 0", perceptron.activation()))

    perceptron.setInputs(input2)
    perceptron.summation()
    print("For {} Result is: {}".format("0, 1", perceptron.activation()))

    perceptron.setInputs(input3)
    perceptron.summation()
    print("For {} Result is: {}".format("1, 0", perceptron.activation()))

    perceptron.setInputs(input4)
    perceptron.summation()
    print("For {} Result is: {}".format("1, 1", perceptron.activation()))

if __name__ == '__main__':
    main()