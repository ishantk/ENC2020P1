# numbers = [1, 2, 4, 4]
numbers = [1, 2, 4, 9]

sum = 8
# Linear Search operation to find 2 numbers whose sum is 8

isNumberFound = False

for i in range(0, len(numbers)):
    # i : 0 | j: 1 to 3
    # i : 1 | j: 2 to 3
    # i : 2 | j: 3 to 3
    # i : 0 | j: 1 to 3 | this should not work
    for j in range(i+1, len(numbers)):

        x = numbers[i] + numbers[j]

        if x == sum:
            isNumberFound = True
            break

    if isNumberFound:
        break

if isNumberFound:
    print(">> Numbers Found: {} {}".format(numbers[i], numbers[j]))
else:
    print(">> Numbers Not Found")

# Solve the same Problem with 1 Loop :)




