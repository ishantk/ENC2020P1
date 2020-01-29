"""
    Class : Attributes and Methods/Functions
            whatever you write in class belongs to class
            Class is also a Multi Value Container
            Whatever is in the class, is common for all its objects

    Object : Attributes will be created with self

"""

class Counter:

    # Property of Class
    sCount = 1

    def __init__(self):
        self.count = 1

    def increment(self):
        self.count += 1
        # self.sCount += 1    # self.sCount = self.sCount + 1
        Counter.sCount += 1

    def decrement(self):
        self.count -= 1
        Counter.sCount -= 1

    def showCount(self):
        print(">> count is: {} and sCount is: {}".format(self.count, Counter.sCount))
        # print(">> sCount is:", self.count)
        # print(">> sCount is:", Counter.sCount)


c1 = Counter()
c2 = Counter()
c3 = c1     # reference copy

c1.increment()  # c1/c3 count = 2 sCount = 2

c1.increment()  # c1/c3 count = 3 sCount = 3
c2.increment()  # c2    count = 2 sCount = 4
c3.increment()  # c1/c3 count = 4 sCount = 5

c1.decrement()  # c1/c3 count = 3 sCount = 4
c3.increment()  # c1/c3 count = 4       -> 4    sCount = 5
c2.increment()  # c2    count = 3       -> 3    sCount = 6

# How many Object : 2 OK
c1.showCount()  # >> Count is: 4 and sCount is: 6
c2.showCount()  # >> Count is: 3 and sCount is: 6
c3.showCount()  # >> Count is: 4 and sCount is: 6


"""
c1 = Counter()
c1.increment()
Counter.increment(c1)

print(">> Dictionary of c1 ref to Object")
print(c1.__dict__)

print(">> c1.count is:", c1.count)
print(">> c1.sCount is:", c1.sCount)

print(">> Dictionary of Counter Class ")
print(Counter.__dict__)
"""



