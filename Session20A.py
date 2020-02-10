def dataGenerator():

    file = open("points.csv", "r")
    lines = file.readlines()

    for line in lines:
        yield line


result = dataGenerator()
# Here result will refer to generator object

print(result)
print(next(result))
print(next(result))