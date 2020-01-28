# OOPS QUIZ :)

class Counter:

    def __init__(self):
        self.count = 1

    def increment(self):
        self.count += 1

    def decrement(self):
        self.count -= 1

    def showCount(self):
        print(">> Count is: {}".format(self.count))


c1 = Counter()  # c1/c3 count = 1
c2 = Counter()  # c2    count = 1
c3 = c1

c1.increment()  # c1/c3 count = 2
c1.increment()  # c1/c3 count = 3
c2.increment()  # c2    count = 2
c3.increment()  # c1/c3 count = 4

c1.decrement()  # c1/c3 count = 3
c3.increment()  # c1/c3 count = 4       -> 4
c2.increment()  # c2    count = 3       -> 3

# How many Object : 2 OK
c1.showCount()  # >> Count is: 4
c2.showCount()  # >> Count is: 3
c3.showCount()  # >> Count is: 4

print(hex(id(c1)), c1.__dict__)
print(hex(id(c2)), c2.__dict__)
print(hex(id(c3)), c3.__dict__)
