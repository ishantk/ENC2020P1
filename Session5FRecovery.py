# Passing Single Value Container
def square(number):
    print(">> number before is:", number, hex(id(number)))
    number = number * number
    print(">> number after is:", number, hex(id(number)))



num = 10
print(">> num is:", num, hex(id(num)))
square(num)
print(">> num now is:", num, hex(id(num)))

# Passing Multi Value Container
def squareOfNumbers(numbers):
    print(">> numbers before is:", numbers, hex(id(numbers)))

    for i in range(0, len(numbers)):
        numbers[i] = numbers[i] * numbers[i]

    print(">> numbers after is:", numbers, hex(id(numbers)))

nums = [10, 20, 30, 40, 50]
print(">> nums is:", nums, hex(id(nums)))
squareOfNumbers(nums)
print(">> nums now is:", nums, hex(id(nums)))