# PERCEPTRON AS LOGICAL NOT OPERATION

class Perceptron:

    def __init__(self):

        self.weight = -1

        # Assuming Threshold
        self.theta = -0.5

        print(">> Perceptron Created")

    def setInputs(self, input):
        self.input = input

    # Sum of Inputs*Weights
    def summation(self):
        self.sum = self.input * self.weight
        # print(">> summation is:", self.sum)

    # Binary Step Activation Function
    def activation(self):
        if self.sum >= self.theta:
            return 1
        else:
            return 0


def main():

    # Create Perceptron
    perceptron = Perceptron()

    # Set Inputs
    perceptron.setInputs(input=0)
    perceptron.summation()
    print("For {} Result is: {}".format("0", perceptron.activation()))

    perceptron.setInputs(input=1)
    perceptron.summation()
    print("For {} Result is: {}".format("1", perceptron.activation()))

if __name__ == '__main__':
    main()