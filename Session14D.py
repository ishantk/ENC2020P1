# Types of Inheritance
"""
    1. Single Level
    A
    |
    B

    class A:
        pass

    class B(A):
        pass


    2. Multi Level
    A
    |
    B
    |
    C

    class A:
        pass

    class B(A):
        pass

    class C(B):
        pass

    3. Hierarchy
         A
         |
      B    C

    class A:
        pass

    class B(A)
        pass

    class C(A)
        pass

    4. Multiple
    A   B
      |
      C

    class A:
        pass

    class B
        pass

    class C(A, B)
        pass

    5. Hybrid
        Any combination of above :)

"""

class A:

    # Property of A class
    a = 10

    def __int__(self, b):
        print(">> Object Constructed with init of A")
        self.b = b

    def show(self):
        print(">> a is:", A.a)
        print(">> b is:", self.b)


class B:

    x = 10

    def __init__(self, y):
        print(">> Object Constructed with init of B")
        self.y = y

    def show(self):
        print(">> x is:", B.x)
        print(">> y is:", self.y)


class C(A, B):
    pass


cRef = C(10)
print(cRef.__dict__)

cRef.show()



# State of Confusion | Ambiguity | Discombobulated
# Q1: which parent init should be used to construct object of C ?
# Q2: which parent show should be executed ?
# Q3: Is Multiple Inheritance Safe to use ?

