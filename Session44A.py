from sklearn.cluster import KMeans

"""
    Machine Learning
    Attributes : weight and engine

    weight      engine      vehicle

    Bikes:
    200kgs      100cc       
    250kgs      200cc       
    300kgs      300cc       
    350kgs      350cc       

    Cars:
    800kgs      800cc       
    1000kgs     1100cc      
    1200kgs     1300cc      
    1500kgs     1550cc      

"""


# Representing Training Data

bike1 = [200, 100]
car1 = [800, 800]
data = [
        bike1, [250, 200], [300, 300], [350, 350],
        car1, [1000, 1100], [1200, 1300], [1500, 1550]
    ]

tagetNames = ["Car", "Bike"]

# Create the Model
clusters = 2
model = KMeans(n_clusters=clusters)

# Train the Model but no labels specified
model.fit(data)

# predictions = model.predict(data)
# print(predictions)

sampleInput = [1190, 1170]
predictedClass = model.predict([sampleInput])
print(tagetNames[predictedClass[0]])

