# Below Function is a Single Expression Computation
def areaOfCircle(radius=1.0):
    area = 3.14 * radius * radius
    return area


# Reference Copy
area = areaOfCircle
print(">> areaOfCircle is:", areaOfCircle)
print(">> area is:", area)


print(">> area of circle with radius 5 is:", areaOfCircle(5))
print(">> area of circle with radius 5 is:", area(5))

# In Mathematics Lambdas compute Sinlge Expression Statements :)
lRef1 = lambda radius = 1.0: 3.14 * radius * radius
lRef2 = lambda x, y: x**y
lRef3 = lambda x=int(input("Enter X: ")), y = int(input("Enter Y: ")): x + y
lRef4 = lambda x=int(input("Enter X: ")), y = int(input("Enter Y: ")): lRef1(x) + lRef2(x, y)

print(">> lRef1 is:", lRef1)
print(">> lRef2 is:", lRef2)
print(">> area of circle with radius 7 is:", lRef1(7))
print(">> 2 power 4 is:", lRef2(2, 4))

print(lRef3())
print(lRef4())
