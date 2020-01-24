# https://visualgo.net/bn/sorting

def insertionSort(data):

    for i in range(1, len(data)):
        key = data[i]
        j = i-1
        # print(">> i[{}] key[{}] j[{}]".format(i, key, j))

        while j >= 0 and data[j] > key:
            data[j+1] = data[j]
            j -= 1

        data[j+1] = key

    # return

ages = [12, 34, 11, 67, 88, 77, 37, 43, 51, 13]

# Original Data     : 12, 34, 11, 67, 88, 77, 37, 43, 51, 13
# i[1], j[0], k[34] : 12, 34, 11, 67, 88, 77, 37, 43, 51, 13
# i[2], j[1], k[11] : 12, 34, 34, 67, 88, 77, 37, 43, 51, 13
#       j[0]        : 11, 12, 34, 67, 88, 77, 37, 43, 51, 13
# i[3], j[2], k[67] : 12, 34, 34, 67, 88, 77, 37, 43, 51, 13


insertionSort(ages)

for age in ages:
    print(age, end=" ")

