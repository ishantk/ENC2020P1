# TUPLE : IMMUTABLE
num1 = (10, 20, 30, 40, 50, 30)
print("num1:", num1, type(num1))

# LIST  : MUTABLE
num2 = [10, 20, 30, 40, 50, 30]
print("num2:", num2, type(num2))

# SET   : UNIQUE and MUTABLE with add and delete not for update
# To achieve uniqueness set hashes the data and we don't have indexes here
# due to hashing here in Set output is unordered
num3 = {10, 20, 30, 40, 50, 30}
print("num3:", num3, type(num3))

# STRING : IMMUTABLE
name = "John Watson"
print("name:", name, type(name))

print(num1[1])
print(num2[2])
print(name[2])
# print(num3[3]) # error

# num1[1] = 11 # err
num2[1] = 11   #OK
# num3[1] = 11   # err
# name[1] = "k"  # err
print(name)

# DICTIONARY : KEY and VALUE Pair | MUTABLE
# On the Web Terminology it is JSON : Java Script Object Notation

customer = {
                "name": "John",
                "age": 30,
                "email": "john@example.com",
                "rating":4.5,
                "loyalityPoints":5133
            }

customer["name"] = "John Watson"
customer["phone"] = "+91 99999 88888"
print(customer, type(customer))

# HW 1: Create Memory Representation of Dictionary [ Google It :) ]
# HW 2: Find single value and multi value containers use case in apps which you use
# HW 3: Refer the link below: Copy the data and create dictionary
# From the dictionary lear how multi value containers stores other containers
# Make the dictionary in python and show ride estimate
# https://developers.olacabs.com/docs/ride-estimate
