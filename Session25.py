import numpy as np

# numpy array creation :0)

numbers = [10, 20, 30, 40, 50]
print(numbers, type(numbers))

print()

# optimised -> better on memory and time while usage :)
# numpy array is optimised as compared to the list :)
# array = np.array(numbers)
array = np.array([10, 20, 30, 40, 50])
print(array, type(array))

#                OK      OK    OK       OK
# Explore with string, tuple, set and dictionary

array1 = np.array((10, 20, 30, 40, 50))
print(array1, type(array1))
print()

array2 = np.array({10, 20, 30, 40, 50})
print(array2, type(array2))
print()

# Array with 1 single element of type string
array3 = np.array("Hello")
print(array3, type(array3))
print()

# array4 = np.array({"name":"John", "age":30})
array4 = np.array([{"name":"John", "age":30}, {"name":"Fionna", "age":22}])
print(array4, type(array4))
print()

# Array with 1 single element of type int
array5 = np.array(30)
print(array5, type(array5))
print()

# Updating Data in numpy
array1[2] = 222
print(array1)

# Iterate in numpy array

# for i in range(0, len(array1)):
#     print(array1[i])


print()

for num in array1:
    print(num)

print()

# Append Data in Existing ndarray to get a new ndarray
array = np.append(array1, [11, 22, 33, 44, 55])
print(array1)
print(array)

# Refer : https://numpy.org/