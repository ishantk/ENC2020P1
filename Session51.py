# Activation Functions:

import matplotlib.pyplot as plt
import numpy as np

def sigmoid(inputs):
    outputs = []

    for x in inputs:
        result = 1 / (1 + np.exp(-x))
        outputs.append(result)
    return outputs

def softmax(inputs):
    outputs = np.exp(inputs) / sum(np.exp(inputs))
    return outputs

def hyperbolicTan(inputs):
    outputs = np.tanh(inputs)
    return outputs

def main():
    inputs = list(range(0, 21))
    outputs = sigmoid(inputs)
    print(inputs)
    print(outputs)

    plt.plot(inputs, outputs)
    plt.xlabel("Inputs")
    plt.ylabel("Outputs")
    plt.show()


if __name__ == '__main__':
    main()

