import math

class Point:

    totalPoints = 0

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def showPoint(self):
        print("{} | {}".format(self.x, self.y))

    # def calculateDistance(self, point1, point2):
    #     distance = math.sqrt((point2.y - point1.y)**2 + (point2.x - point1.x)**2)
    #     return distance

    # def calculateDistance(self, point):
    #     distance = math.sqrt((point.y - self.y) ** 2 + (point.x - self.x) ** 2)
    #     return distance

    # Static Method -> Which will not take self as 1st input :)
    @staticmethod
    def calculateDistance(point1, point2):
        distance = math.sqrt((point2.y - point1.y)**2 + (point2.x - point1.x)**2)
        return distance

    @staticmethod
    def createPoint():
        file = open("points.csv", "r")
        line = file.readline()
        data = line.split(",")
        point = Point(int(data[0]), int(data[1]))
        return point

    @staticmethod
    def createPoints():

        points = []

        file = open("points.csv", "r")
        lines = file.readlines()

        for line in lines:
            data = line.split(",")
            point = Point(int(data[0]), int(data[1]))
            points.append(point)

        return points


    @classmethod
    def createPointsAgain(cls):
        # print(cls)
        # print(cls.__dict__)
        # point = Point(10, 20)
        # point = cls(10, 20)
        # return point

        points = []

        file = open("points.csv", "r")
        lines = file.readlines()

        for line in lines:
            data = line.split(",")
            point = cls(int(data[0]), int(data[1]))
            points.append(point)

        return points


# pRef1 = Point(4, 5)
# pRef2 = Point(6, 9)

# pRef1.calculateDistance(pRef1, pRef2)
# result = pRef1.calculateDistance(pRef2)

# result = Point.calculateDistance(pRef1, pRef2)
# print(">> Distance is:", result)

# points = Point.createPoints()
# print(points)
# points[0].showPoint()
# points[1].showPoint()

points = Point.createPointsAgain()

for point in points:
    # point.showPoint()
    print(point.__dict__)