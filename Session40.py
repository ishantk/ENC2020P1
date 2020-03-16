import pandas as pd
import numpy as np

dataSet = pd.DataFrame()

# Attribute: outlook
dataSet['outlook'] = ['sunny', 'sunny', 'overcast', 'rainy', 'rainy', 'rainy',
                      'overcast', 'sunny', 'sunny', 'rainy', 'sunny',
                      'overcast', 'overcast', 'rainy']

# Attribute: temperature
dataSet['temperature'] = ['hot', 'hot', 'hot', 'mild', 'cool',
                      'cool', 'cool', 'mild', 'cool', 'mild',
                      'mild', 'mild', 'hot', 'mild']

# Attribute: humidity
dataSet['humidity'] = ['high', 'high', 'high', 'high', 'normal', 'normal',
                      'normal', 'high', 'normal', 'normal', 'normal',
                      'high', 'normal', 'high']

# Attribute: windy
dataSet['windy'] = ['false', 'true', 'false', 'false', 'false', 'true',
                      'true', 'false', 'false', 'false', 'true',
                      'true', 'false', 'true']
# Attribute: play
dataSet['play'] = ['no', 'no', 'yes', 'yes', 'yes', 'no',
                      'yes', 'no', 'yes', 'yes', 'yes',
                      'yes', 'yes', 'no']

print(dataSet)


def computeEntropyDataSet():

    # E(S) = -P(Yes) * log_base2(P(Yes)) - P(No) * log_base2(P(No))
    # E(S) = -9/14 * log_base2(9/14) - 5/14 * log_base2(5/14)


    # print(len(dataSet['play']))
    # print(len(dataSet[dataSet['play'] == 'yes']))
    # print(len(dataSet[dataSet['play'] == 'no']))

    """
    total = len(dataSet['play'])
    numOfYes = len(dataSet[dataSet['play'] == 'yes'])
    numOfNo = len(dataSet[dataSet['play'] == 'no'])

    probabilityYes = numOfYes / total
    probabilityNo = numOfNo / total

    print(probabilityYes)
    print(probabilityNo)

    entropy = -(probabilityYes*np.log2(probabilityYes)) - (probabilityNo*np.log2(probabilityNo))
    print(entropy)
    return entropy
    """

    return  -( (len(dataSet[dataSet['play'] == 'yes']) / len(dataSet['play']) ) * np.log2( (len(dataSet[dataSet['play'] == 'yes']) / len(dataSet['play']) ) ))  - ( (len(dataSet[dataSet['play'] == 'no']) / len(dataSet['play']) ) * np.log2( (len(dataSet[dataSet['play'] == 'no']) / len(dataSet['play']) ) ))


def informationGainInOutlook():
    pass

print("Entropy Of Data Set:", computeEntropyDataSet())