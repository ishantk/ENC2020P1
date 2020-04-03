"""

    XOR
    A   B   Y
    0   0   0
    0   1   1
    1   0   1
    1   1   0

    >> AND OR NOT, Rest all operations must be derived from above

    A XOR B:
    (A OR B) AND (NOT (A AND B))

    A:0, B:0
    (0 OR 0) AND (NOT (0 AND 0))
    0       AND  (NOT 0)
    0 AND 1
    0

    A:0, B:1
    (0 OR 1) AND (NOT (0 AND 1))
    1       AND  (NOT 0)
    1 AND 1
    1

    A:1, B:0
    (1 OR 0) AND (NOT (1 AND 0))
    1       AND  (NOT 0)
    1 AND 1
    1

    A:1, B:1
    (1 OR 1) AND (NOT (1 AND 1))
    1       AND  (NOT 1)
    1 AND 0
    0

"""

import numpy as np

# OR Operation
class PerceptronOR:

    def __init__(self):
        self.weights = np.array([1.1, 1.1])
        self.theta = 1

        print(">> Perceptron1 Created for OR Operations")

    # Sum of Inputs*Weights
    def summation(self):
        self.sum = np.dot(self.inputs, self.weights)

    # Binary Step Activation Function
    def activation(self):
        if self.sum >= self.theta:
            return 1
        else:
            return 0

    def processPerceptron(self, inputs):
        self.inputs = inputs
        self.summation()
        return self.activation()

# AND Operation
class PerceptronAND:

    def __init__(self):
        self.weights = np.array([0.5, 0.5])
        self.theta = 1

        print(">> Perceptron2 Created for AND Operations")

    # Sum of Inputs*Weights
    def summation(self):
        self.sum = np.dot(self.inputs, self.weights)

    # Binary Step Activation Function
    def activation(self):
        if self.sum >= self.theta:
            return 1
        else:
            return 0

    def processPerceptron(self, inputs):
        self.inputs = inputs
        self.summation()
        return self.activation()

# NOT Operation
class PerceptronNOT:

    def __init__(self):

        self.weight = -1
        self.theta = -0.5
        print(">> Perceptron3 Created for NOT Operations")

    # Sum of Inputs*Weights
    def summation(self):
        self.sum = self.input * self.weight

    # Binary Step Activation Function
    def activation(self):
        if self.sum >= self.theta:
            return 1
        else:
            return 0

    def processPerceptron(self, input):
        self.input = input
        self.summation()
        return self.activation()

def main():
    #                  A  B
    input1 = np.array([0, 0])
    input2 = np.array([0, 1])
    input3 = np.array([1, 0])
    input4 = np.array([1, 1])

    #  A XOR B:
    #  (A OR B) AND (NOT (A AND B))

    orPerceptron = PerceptronOR()
    andPerceptron = PerceptronAND()
    notPerceptron = PerceptronNOT()

    # A OR B
    or1 = orPerceptron.processPerceptron(input1)    # 0
    or2 = orPerceptron.processPerceptron(input2)    # 1
    or3 = orPerceptron.processPerceptron(input3)    # 1
    or4 = orPerceptron.processPerceptron(input4)    # 1

    # A AND B
    and1 = andPerceptron.processPerceptron(input1)  # 0
    and2 = andPerceptron.processPerceptron(input2)  # 0
    and3 = andPerceptron.processPerceptron(input3)  # 0
    and4 = andPerceptron.processPerceptron(input4)  # 1

    # NOT (A AND B)
    not1 = notPerceptron.processPerceptron(and1)    # 1
    not2 = notPerceptron.processPerceptron(and2)    # 1
    not3 = notPerceptron.processPerceptron(and3)    # 1
    not4 = notPerceptron.processPerceptron(and4)    # 0

    # ( A OR B ) AND ( NOT (A AND B) )
    finalInput1 = np.array([or1, not1])
    final1 = andPerceptron.processPerceptron(finalInput1)
    final2 = andPerceptron.processPerceptron(np.array([or2, not2]))
    final3 = andPerceptron.processPerceptron(np.array([or3, not3]))
    final4 = andPerceptron.processPerceptron(np.array([or4, not4]))

    # XOR OPERATION
    print("( {} OR {} ) AND ( NOT ({} AND {}) ) : {}".format(input1[0], input1[1], input1[0], input1[1], final1))
    print("( {} OR {} ) AND ( NOT ({} AND {}) ) : {}".format(input2[0], input2[1], input2[0], input2[1], final2))
    print("( {} OR {} ) AND ( NOT ({} AND {}) ) : {}".format(input3[0], input3[1], input3[0], input3[1], final3))
    print("( {} OR {} ) AND ( NOT ({} AND {}) ) : {}".format(input4[0], input4[1], input4[0], input4[1], final4))




if __name__ == '__main__':
    main()

# Assignment : Implement OOPS to the best in this program
#              Implement other logical operations eg: NAND :)