totalFloors = 10
myFloor = 5
liftPosition = 1

for floor in range(liftPosition, totalFloors+1):
    print(">> Floor #", floor)

    if floor == myFloor:
        print(">> Your Floor Arrived")
        break

# products = (1541, 2451, 1353, 4673, 5245, 2356, 6777, 8234, 9231, 1331)
products = [1541, 2451, 1353, 4673, 5245, 2356, 6777, 8234, 9231, 1331]

for i in range(0, len(products)):
    if products[i] > 5000:
        products[i] = products[i] - 0.4*products[i]

print(">> AFTER EORS SALE NEW PRICES:")

for i in range(0, len(products)):
    print(">> ", products[i])

# SORT : Insertion Sort :) | Maths -> Time Complexity :)

