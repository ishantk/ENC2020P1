class Product:

    def __init__(self, pid, name, price, quantity):
        self.pid = pid
        self.name = name
        self.price = price
        self.quantity = quantity
        self.nextProduct = None
        self.prevProduct = None

    def showProductDetails(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("{}\t{}\t{}".format(self.pid, self.name, self.price))
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


class LinkedList:

    size = 0
    items = 0
    price = 0

    def __init__(self):
        print(">> Linked List Created")
        print(self)
        self.head = None
        self.current = None

    def append(self, product):
        print(product)
        LinkedList.size += 1
        LinkedList.items += product.quantity
        LinkedList.price += (product.quantity * product.price)

        if self.head == None:
            self.head = product
            self.current = product
        else:
            product.prevProduct = self.current
            self.current.nextProduct = product

            self.current = product
            product.nextProduct = self.head
            self.head.prevProduct = self.current     # Fixing 1st Product Object's Previous to be the current for iterating in backward directions


    def iterateForward(self):

        temp = self.head

        while temp.nextProduct != self.head:
            temp.showProductDetails()
            temp = temp.nextProduct

        temp.showProductDetails()


    def iterateBackward(self):

        temp = self.current

        while temp.prevProduct != self.current:
            temp.showProductDetails()
            temp = temp.prevProduct
            print(">> temp is:", temp)

        temp.showProductDetails()


    def getTotalPrice(self):

        totalPrice = 0
        totalItems = 0
        totalProducts = 0

        temp = self.head

        while temp.nextProduct != self.head:
            totalPrice = totalPrice + (temp.price * temp.quantity)
            totalItems = totalItems + temp.quantity
            totalProducts += 1
            temp = temp.nextProduct

        totalPrice = totalPrice + (temp.price * temp.quantity)
        totalItems = totalItems + temp.quantity
        totalProducts += 1

        return (totalPrice, totalItems, totalProducts)





shoppingCart = LinkedList()

# product1 = Product(101, "iPhoneX", 70000)
# product2 = Product(301, "AlphaBounce", 8000)
# product3 = Product(701, "Samsung LED", 40000)
# shoppingCart.append(product1)
# shoppingCart.append(product2)
# shoppingCart.append(product3)

shoppingCart.append(Product(101, "1. iPhoneX", 70000, 1))
shoppingCart.append(Product(301, "2. AlphaBounce", 8000, 2))
shoppingCart.append(Product(701, "3. Samsung LED", 40000, 1))
shoppingCart.append(Product(401, "4. Samsung M10", 1000, 3))

# shoppingCart.iterateForward()
shoppingCart.iterateBackward()

# result = shoppingCart.getTotalPrice()
# print(">> TOTAL PRICE:\u20b9", result[0])
# print(">> TOTAL ITEMS:", result[1])
# print(">> TOTAL PRODUCTS:", result[2])
print(">> SIZE OF LINKED LIST:", LinkedList.size)
print(">> ITEMS IN LINKED LIST:", LinkedList.items)
print(">> PRICE IN LINKED LIST:", LinkedList.price)

