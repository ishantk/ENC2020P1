class Order:
    id = 1
    def __init__(self, name, address, price):
        self.oid = Order.id
        self.name = name
        self.address = address
        self.price = price

        Order.id += 1

    def showOrderDetails(self):
        print("{}, {}, {}, {}".format(self.oid, self.name, self.address, self.price))

    def toCSV(self):
        return "{},{},{},{}\n".format(self.oid, self.name, self.address, self.price)

    def saveOrder(self):
        file = open("orders.csv", "a")
        orderData = self.toCSV()
        file.write(orderData)
        file.close()
        print(">> Order[{}] Saved :)".format(self.oid))

    # @staticmethod is a DECORATOR : no self needed in this method
    @staticmethod
    def readOrders():
        file = open("orders.csv", "r")
        lines = file.readlines() # List of Lines
        # print(lines)
        # print(type(lines))
        for line in lines:
            data = line.split(",")
            # print(data)
            # print(line)
            order = Order(data[1], data[2], int(data[3]))
            order.oid = int(data[0])
            order.showOrderDetails()

        file.close()



# order1 = Order("John", "Redwood Shores", 300)
# order2 = Order("Mike", "Country Homes", 350)
# order3 = Order("Leo", "Redwood Shores", 200)
# order4 = Order("Harry", "Country Homes", 1300)
# order5 = Order("George", "Redwood Shores", 450)
#
# order1.showOrderDetails()
# order2.showOrderDetails()
# order3.showOrderDetails()
# order4.showOrderDetails()
# order5.showOrderDetails()
#
# order1.saveOrder()
# order2.saveOrder()
# order3.saveOrder()
# order4.saveOrder()
# order5.saveOrder()

Order.readOrders()

# Explore : Selection-Sort Algorithm and Implement it to Sort the Order read from File into Ascending Order based on Price :)



