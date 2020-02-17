class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def showPoint(self):
        print("{} | {}".format(self.x, self.y))

    def __str__(self):
        # return "{} | {} | {}".format(self.x, self.y, object.__str__(self))
        return "{} | {} | {}".format(self.x, self.y, hex(id(self)))


p1 = Point(10, 20)

data = str(p1)
print(data)

Point.showPoint(p1)