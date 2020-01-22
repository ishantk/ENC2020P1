data = [1, 2, 3, 4, 5]
print(len(data))
print(max(data))
print(min(data))

# HW: You code your own functions


def myLen(data):
    length = 0
    return length

def myMax(data):
    max = 0
    return max

def myMin(data):
    min = 0
    return min


# List Comprehension
print([x**2 for x in data])

productPrices = [1123, 1342, 3341, 4421, 5456]
# List Comprehension and Expressions : Error
# Explore Do we have any other way to do the same job
print([0.4*x for x in productPrices])

numbers = list(range(1, 101))
print(numbers)


names1 = ("John", "Jennie", "Jim", "John", "Jack")
names2 = list(names1)
names3 = set(names1)
# names4 = dict(names1) | Error

print(names1, type(names1))
print(names2, type(names2))
print(names3, type(names3))




