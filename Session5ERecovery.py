# for i in range(1, 11):
#     print(">> i is:", i)

# Recursion :)

def show(num):
    print(">> num is:", num)
    num += 1

    if num == 11:
        return

    show(num)



show(1)
# show(2)
# show(3)