import pandas as pd

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

# dataSet1 = pd.DataFrame()
# dataSet1['Weather']=['Overcast','Rainy','Sunny','Grand total']
# dataSet1['No']=[len(dataSet[dataSet['Overcast']=='no']),len(dataSet[dataSet['Rainy']=='no']),len(dataSet[dataSet['Sunny']=='no']),len(dataSet[dataSet['Overcast']=='no'])+len(dataSet[dataSet['Rainy']=='no'])+len(dataSet[dataSet['Sunny']=='no'])]
# dataSet1['No']=[len(dataSet[dataSet['Overcast']=='yes']),len(dataSet[dataSet['Rainy']=='yes']),len(dataSet[dataSet['Sunny']=='yes']),len(dataSet[dataSet['Overcast']=='yes'])+len(dataSet[dataSet['Rainy']=='yes'])+len(dataSet[dataSet['Sunny']=='yes'])

# rainyDataSet = dataSet[dataSet['outlook'] == 'rainy']
# print(rainyDataSet)
#
# print("Length Of Rainy DataSet:", len(rainyDataSet))
# print("yes_rainy", len(rainyDataSet[rainyDataSet['play'] == 'yes']))
# print("no_rainy", len(rainyDataSet[rainyDataSet['play'] == 'no']))

# print("~~~~Grouping~~~~")
# count = dataSet.groupby(['outlook', 'play']).size()
# print(count, type(count))
# print("~~~~~~~~")

print("======================================")
print("Frequency Table")

overcastDataSet = dataSet[dataSet['outlook'] == 'overcast']
print(overcastDataSet)

print("Length Of Overcast DataSet:", len(overcastDataSet))
print("yes_overcast", len(overcastDataSet[overcastDataSet['play'] == 'yes']))
print("no_overcast", len(overcastDataSet[overcastDataSet['play'] == 'no']))

rainyDataSet = dataSet[dataSet['outlook'] == 'rainy']
print(rainyDataSet)

print("Length Of Rainy DataSet:", len(rainyDataSet))
print("yes_rainy", len(rainyDataSet[rainyDataSet['play'] == 'yes']))
print("no_rainy", len(rainyDataSet[rainyDataSet['play'] == 'no']))


sunnyDataSet = dataSet[dataSet['outlook'] == 'sunny']
print(sunnyDataSet)

print("Length Of Sunny DataSet:", len(sunnyDataSet))
print("yes_sunny", len(sunnyDataSet[sunnyDataSet['play'] == 'yes']))
print("no_sunny", len(sunnyDataSet[sunnyDataSet['play'] == 'no']))

print("======================================")


print("======================================")
print("Likelihood Table")


