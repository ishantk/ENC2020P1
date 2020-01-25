number = 10
# numbers = 10, 20, 30, 40, 50
# numbers = (10, 20, 30, 40, 50)
numbers = (10, "Hello", 20, 30, 40, 50, "Bye")


print(number, type(number), hex(id(number)))
print(numbers, type(numbers), hex(id(numbers)), len(numbers))

print(numbers[1], numbers[3], numbers[len(numbers)-1])
