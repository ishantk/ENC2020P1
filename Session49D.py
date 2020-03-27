from sklearn.feature_extraction import DictVectorizer

weather = [
    {'city': 'Delhi', 'temperature': 33.0},
    {'city': 'Mumbai', 'temperature': 12.0},
    {'city': 'Pune', 'temperature': 18.0},
]

print(weather)

vec = DictVectorizer()
array = vec.fit_transform(weather).toarray()
print(array)

featureNames = vec.get_feature_names()
print(featureNames)