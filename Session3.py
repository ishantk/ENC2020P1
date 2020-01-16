# Container Creation Statement

# Single Value Container
number = 10

# Multi Value Container
# numbers = 10, 20, 30, 40, 50
numbers = (10, 20, 30, 40, 50)

# Read/Print Statement
print("number:", number, type(number), id(number))
print("numbers:", numbers, type(numbers), id(numbers))

print("numbers[0]:", numbers[0], type(numbers[0]), id(numbers[0]))
print("numbers[1]:", numbers[1], type(numbers[1]), id(numbers[1]))
print("numbers[2]:", numbers[2], type(numbers[2]), id(numbers[2]))
print("numbers[3]:", numbers[3], type(numbers[3]), id(numbers[3]))
print("numbers[4]:", numbers[4], type(numbers[4]), id(numbers[4]))

# PS: number and numbers are Reference Variables
#     they contain HashCode
#     But when we print them i.e. read them we don't see HashCodes
#     Rather we see data. This is MAGIC.

age = 30
print("age:", age, type(age), id(age))

del age

# print("age after we have deleted age:", age)
print("numbers[2] after we have deleted age:", numbers[2])

