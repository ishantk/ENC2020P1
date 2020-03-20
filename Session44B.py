from sklearn.datasets import load_iris
from sklearn.cluster import KMeans

irisData = load_iris()
FEATURES = irisData.data

print(FEATURES)

# Create The Model
clusters = 3
model = KMeans(n_clusters=clusters)

# Train the Model
model.fit(FEATURES)

predictions = model.predict(FEATURES)
print(predictions)