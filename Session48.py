import math

# point1: [65.2] point2: [60]
# point1: [65.2, 2.3] point2: [60, 3.3]
# point1: [65.2, 2.3, 45.2] point2: [60, 3.3, 33.6]
def euclideanDistance(point1, point2):
    sumOfSquaredDistance = 0

    for i in range(len(point1)):
        sumOfSquaredDistance += math.pow(point1[i] - point2[i], 2)

    return math.sqrt(sumOfSquaredDistance)

def main():

    # Height in Inches and Weight in Pounds
    dataSet = [
                [65.2, 120.22],
                [71.5, 35.77],
                [69.8, 153.23],
                [67.2, 148.55],
                [68.5, 133.11],
                [69.11, 148.5],
                [70.55, 160.0],
                [67.33, 112.9],
                [66.49, 127.11]
              ]

    # We need to predict the value of weight given the value of height
    givenHeight = [60]

    # With k nearest neighbours we will solve this regression problem !!

    k = 3

    # List in which we will place distances of the data points from the givenHeight
    neighborDistances = []

    for idx, dataPoint in enumerate(dataSet):
        print(idx, dataPoint)

        # Compute Distance of Each Data POint from givenHeight
        distance = euclideanDistance(dataPoint[:-1], givenHeight)
        print("distance between {} and {} is: {}".format(dataPoint[:-1], givenHeight, distance))

        # Appending distance and index as a tuple in the list
        neighborDistances.append((distance, idx))

    # Sort the List in Ascending order based on Distances
    neighborDistances = sorted(neighborDistances)
    print(neighborDistances)

    # Pick up the first k data point distances from sorted neighborDistances
    kNearestNeighbors = neighborDistances[:k]
    print("K Nearest Neighbors: ")
    print(kNearestNeighbors)

    # Since we are solving regression problem, we need to compute mean of the labels
    # Fetch the lables first i.e. weight
    outputLabels = []
    for neighbor in kNearestNeighbors:
        # print(neighbor) -> (5.200000000000003, 0)
        idx = neighbor[1]
        outputLabels.append(dataSet[idx][1])


    predictedWeight = sum(outputLabels) / len(outputLabels)
    print(">> Predicted Weight for givenHeight", givenHeight[0], "is:", predictedWeight)

    # PS: For Classification, take the mode of nearest neighbors to predict class


if __name__ == '__main__':
    main()