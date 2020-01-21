# Passing the Reference i.e. HashCodes :)
def square(numbers):

    print(">> [SQUARE] numbers is:", numbers, hex(id(numbers)))

    # We are squaring each and every single element of List
    for i in range(0, len(numbers)):
        numbers[i] = numbers[i] * numbers[i]

    print(">> [SQUARE] numbers now is:", numbers, hex(id(numbers)))



# List in Python
numbers = [10, 20, 30, 40, 50]

print(">> numbers[0] is:", numbers[0], hex(id(numbers[0])))

print(">> [MAIN] numbers is:", numbers, hex(id(numbers)))
square(numbers)
print(">> [MAIN] numbers now is:", numbers, hex(id(numbers)))

print(">> numbers[0] is:", numbers[0], hex(id(numbers[0])))





