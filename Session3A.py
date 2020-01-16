# Container Creation
num1 = 10
print("num1:", num1, id(num1))

# Container Creation with Reference Copy Operation
num2 = num1
print("num2:", num2, id(num2))

# Update Operation
num1 = 100
print("num1 after updated:", num1, id(num1))

# Container Creation
# Tuple: IMMUTABLE | We cannot change it later
# numbers1 = (10, 20, 30, 40, 50)

# List: MUTABLE | We can change it later
numbers1 = [10, 20, 30, 40, 50]

# Reference Copy Operation
numbers2 = numbers1

print("numbers1:", numbers1, type(numbers1), id(numbers1))
print("numbers2:", numbers2, type(numbers2), id(numbers2))

print("numbers1[2] is:", numbers1[2])
print("numbers2[2] is:", numbers2[2])

# Update Operation | For tuple(err) | For list[work]
numbers1[2] = 33

print("numbers1[2] now is:", numbers1[2])  # 33
print("numbers2[2] now is:", numbers2[2])  # 33




