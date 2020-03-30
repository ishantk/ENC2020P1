# class Input:
#
#     def __init__(self, input, weight):
#         self.input = input
#         self.weight = weight

class Perceptron:

    def __init__(self, inputs=None):
        self.inputs = inputs
        print(">> Perceptron Created with Inputs")
        print(inputs)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


    def summationFunction(self):
        self.sum = 0

        for i in range(len(self.inputs)):
            self.sum += self.inputs[i][0]*self.inputs[i][1]

        print(">> Summation Function Output", self.sum)


    def activationFunction(self):

        threshold = 1

        if self.sum >= threshold:
            print(">> Output is 1")
            print(">> Decision Taken")
        else:
            print(">> Output is 0")
            print(">> Decision Not Taken")


    def activationFunctionLinear(self):
        pass

    def activationFunctionBinary(self):
        pass

    def activationFunctionSigmoid(self):
        pass

    def activationFunctionTanh(self):
        pass

    def activationFunctionRelu(self):
        pass

    def activationFunctionSoftmax(self):
        pass


def main():
    # [input weight]
    inputs = [
        [0, 0],
        [0, 1],
        [1, 0],
        [1, 1]
    ]

    perceptron = Perceptron(inputs)
    perceptron.summationFunction()
    perceptron.activationFunction()


if __name__ == '__main__':
    main()


"""
    Assignment:
    1. Linear
    2. Binary
    3. Sigmoid
    4. tanh
    5. Relu
    6. Softmax

    create all above functions 
    take certain input X and plot them on matplotlib as line graph

"""

"""
    Natural Language Toolkit Installation
    pip install nltk
    
    Tensorflow Installation
    https://www.tensorflow.org/install
    
    Pytorch Installation
    https://pytorch.org/get-started/locally/
"""