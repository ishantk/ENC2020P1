# View i.e. how to take data from user and show it to user

name = input("Enter Your Name: ")
print(">> name:", name, type(name))

age = int(input("Enter Your Age: "))
print(">> age:", age, type(age))

# age = age + 1 | error

age = age + 1

print(">> After 1 year age will be:",age)

# Anything which we take from user as input is always -> string
# Whatever we need to display to the user is alss string
num = 10
num1 = float(num)
print(num1, type(num1))

