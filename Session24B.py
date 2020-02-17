class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def showPoint(self):
        print("{} | {}".format(self.x, self.y))

    def __str__(self):
        return "{} | {} | {}".format(self.x, self.y, hex(id(self)))

    def add(self, point):
        temp = Point()
        temp.x = self.x + point.x
        temp.y = self.y + point.y
        return temp

    # Magical Method leads to Operator Overloading in Python
    def __add__(self, point):
        temp = Point()
        temp.x = self.x + point.x
        temp.y = self.y + point.y
        return temp

    # The way we have add function, we have rest of the functions as well

    # Deep Copy VS Shallow Copy -> Explore
    # def __copy__(self):


p1 = Point(10, 20)
p2 = Point(30, 40)

p3 = p1.add(p2)
p4 = p1 + p2  # p4 = p1.__add__(p2)

p3.showPoint()
p4.showPoint()