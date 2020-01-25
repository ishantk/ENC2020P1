# MODEL
# Storage Containers
# Single Value | Multi Value [Homo, Hetro]
# Dynamic Storage Containers [Data Structures]

# Single Value
age = 10    # Storage Container Creation Statement
print(">> age is:", age, id(age))
print(">> age is:", age, hex(id(age)))
print(">> age is:", age, oct(id(age)))
print(">> age is:", age, bin(id(age)))

# age is a reference variable, having hashcode of data i.e. 10

johnsAge = 10
print(">> johnsAge is:", johnsAge, hex(id(johnsAge)))

# Update Statement
age = 20
print(">> age now is:", age, hex(id(age)))

# Reference Copy
fionnasAge = johnsAge
print(">> fionnasAge is:", fionnasAge, hex(id(fionnasAge)))

# Delete Statement
# del johnsAge
# print(">> johnsAge is:", johnsAge, hex(id(johnsAge))) # error

del fionnasAge

