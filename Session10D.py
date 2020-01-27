"""
def maxNumber(data):

    max = data[0]

    for num in data:
        if num > max:
            max = num

    return max


# numbers = [10, 20, 330, 40, 50]
# print(">> Max number in {} is {}".format(numbers, maxNumber(numbers)))

"""

def maxNumber(data, length):

    if length == 1:
        return data[0]
    else:
        num = maxNumber(data, length-1)


    if num > data[length-1]:
        return num
    else:
        return data[length - 1]



numbers = [10, 20, 30]

print(">> max is:", maxNumber(numbers, 3))
