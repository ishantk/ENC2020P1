# object is a built in class in Python
# By Default, every class is Child of object class


# class Point(object):
class Point:

    def __init__(self, x, y):
        self._x = x
        self.__y = y

    def __showPoint(self):
        print("{} | {}".format(self._x, self._Point__y))

    # Overiding
    def __str__(self):
        return "{} | {}".format(self._x, self._Point__y)

p1 = Point(10, 20)
p2 = Point(30, 40)

# print(p1)
# print(p2)
# print("-------------")
# print(p1.__str__())
# print(p2.__str__())

# print(p1._x)
# print(p1.__y)

# p1.__showPoint()

print(p1.__dict__)
print(Point.__dict__)

print(p1._x)
print(p1._Point__y)
p1._Point__showPoint()

# PS: _  -> protected
#     __ -> private
# But both of them can be accessed. They are just Logical Concepts
