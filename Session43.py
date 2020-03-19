from sklearn import svm

"""
    Machine Learning

    Vehicles
    0 -> Bike
    1 -> Car

    Attributes : weight and engine

    weight      engine      vehicle

    Bikes:
    200kgs      100cc       0
    250kgs      200cc       0
    300kgs      300cc       0
    350kgs      350cc       0

    Cars:
    800kgs      800cc       1
    1000kgs     1100cc      1
    1200kgs     1300cc      1
    1500kgs     1550cc      1

"""


# Representing Training Data

bike = 0
car = 1

bike1 = [200, 100]

X = [
        bike1, [250, 200], [300, 300], [350, 350],
        [800, 800], [1000, 1100], [1200, 1300], [1500, 1550]
    ]
Y = [bike, bike, bike, bike, car, car, car, car]

# Create the Model
model = svm.SVC()

# Train the Model
model.fit(X, Y)

vehicle = [1200, 1100]

preidctedVehicle = model.predict([vehicle])
print(preidctedVehicle)

# Always prefer model with higher accuracy
# keep on testing your models for accuracy by changing them for your dataset
