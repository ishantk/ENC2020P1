# String Formatting

name = "Fionna"
age = 22

print(">> Welcome to our App", name)
print(">> Welcome to our App %s" % (name))

print(">>", name, "Since you are", age, "years old. You can vote")
print(">> {} Since you are {} years old. You can vote".format(name, age))

message = "{} Since you are {} years old. You can vote".format(name, age)

# SQL Query
# sql = "insert into Customer values(1, 'john', 'john@example.com')"

cid = int(input("Enter Customer ID: "))
name = input("Enter Your Name: ")
email = input("Enter Your Email: ")

sql = "insert into Customer values({}, '{}', '{}')".format(cid, name, email)
print(">> SQL:", sql)

products = [3454, 2411, 1341, 4568, 8976]

for i in range(0, len(products)):
    # products[i] = products[i] - (0.4*products[i])
    oldPrice = products[i]
    products[i] -= 0.4*products[i]

    print(">> {} price reduced to {}".format(oldPrice, products[i]))
