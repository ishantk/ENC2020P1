num = 10

def square():

    global num  #declare variables as global if you wish to use them inside :)

    num = 11
    num = num * num

    print(">> 1. num is:", num)

square()

print(">> 2. num is:", num)

