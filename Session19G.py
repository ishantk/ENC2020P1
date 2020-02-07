def squareOfNumber(num=1):
    return num * num

lRef1 = lambda num: num * num
lRef2 = lambda num: num - (0.4*num)

numbers = [10, 20, 30, 40, 50]

# for number in numbers:
#     print(lRef1(number))

# result = map(squareOfNumber, numbers)
# print(result, type(result))

# result = list(map(squareOfNumber, numbers))
# result = list(map(lRef1, numbers))
# result = list(map(lambda num: num * num, numbers))
# result = list(map(lRef2, numbers))
result = list(map(lambda num: num - (0.4*num), numbers))
print(result)



# L1 = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
L1 = list(range(10, 21, 1))
print(L1)

lRef3 = lambda num: num%2 == 0
lRef4 = lambda num: num%2 != 0

result = list(map(lRef4, L1))
print(result)
result = list(filter(lRef4, L1))
print(result)

lRef5 = lambda X, Y : X + Y
L2 = [10, 20, 30, 40, 50]

from functools import reduce

# result = reduce(lRef5, L2)
# result = reduce(lambda X, Y : X + Y, L2)
# result = reduce(lambda X, Y : X + Y, [10, 20, 30, 40, 50])
print(reduce(lambda X, Y : X + Y, [10, 20, 30, 40, 50]))


