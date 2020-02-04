# Passing By value :)
"""
def square(num):
    print(">> num BEFORE is:", num)
    num = num * num
    print(">> num AFTER is:", num)


num = 10
square(num)
print(">> num is:", num)
"""

# Pass By Reference
def square(numbers):
    print("2.", numbers, hex(id(numbers)))
    for i in range(0, len(numbers)):
        numbers[i] = numbers[i] * numbers[i]


nums = [10, 20, 30, 40, 50]
print("1.", nums, hex(id(nums)))

print(">> nums BEFORE is:")
square(nums)

print(">> nums AFTER is:")
print(nums)