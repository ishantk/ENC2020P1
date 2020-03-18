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

# Dummy Variables : Technique where we represent Categorical Data with Numerical data
# Dummy Variables are sometimes also known as Indicator Variables

# ONE-HOT -> Technique In ML where categorical data is represented as 1 or 0

"""

     outlook temperature humidity  windy play
0      sunny         hot     high  false   no
1      sunny         hot     high   true   no
2   overcast         hot     high  false  yes
3      rainy        mild     high  false  yes
4      rainy        cool   normal  false  yes
5      rainy        cool   normal   true   no
6   overcast        cool   normal   true  yes
7      sunny        mild     high  false   no
8      sunny        cool   normal  false  yes
9      rainy        mild   normal  false  yes
10     sunny        mild   normal   true  yes
11  overcast        mild     high   true  yes
12  overcast         hot   normal  false  yes
13     rainy        mild     high   true   no


outlook_sunny   outlook_overcast    outlook_rainy


"""

one_hot_data = pd.get_dummies(dataSet[ ['outlook', 'temperature',
                              'humidity', 'windy'] ])
print(one_hot_data)


