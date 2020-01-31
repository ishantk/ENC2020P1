# Linear Search :)

numbers = [1, 2, 5, 9, 6, 11, 45]
number = 2

# print(number in numbers)

print(numbers)
for i in range(0, len(numbers)):

    print(">> Checking number {} with numbers[{}] i.e. {}".format(number, i, numbers[i]))

    if numbers[i] == number:
        print(">> Number {} Found".format(number))
        break


