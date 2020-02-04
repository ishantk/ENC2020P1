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


# FIFO
class Queue:

    size = 0
    items = 0
    price = 0

    def __init__(self):
        print(">> Stack Created")
        print(self)
        self.head = None
        self.current = None

    def add(self, product):
        print(product)
        Queue.size += 1
        Queue.items += product.quantity
        Queue.price += (product.quantity * product.price)

        if self.head == None:
            self.head = product
            self.current = product
        else:
            product.prevProduct = self.current
            self.current.nextProduct = product

            self.current = product
            product.nextProduct = self.head
            self.head.prevProduct = self.current     # Fixing 1st Product Object's Previous to be the current for iterating in backward directions


    def iterate(self):

        temp = self.head

        while temp.nextProduct != self.head:
            temp.showProductDetails()
            temp = temp.nextProduct

        temp.showProductDetails()


    # Remove Head of Queue
    def poll(self):
        self.head = self.head.nextProduct
        self.head.prevProduct = self.current
        self.current.nextProduct = self.head

    def peek(self):
        self.head.showProductDetails()




shoppingCart = Queue()


shoppingCart.add(Product(101, "1. iPhoneX", 70000, 1))
shoppingCart.add(Product(301, "2. AlphaBounce", 8000, 2))
shoppingCart.add(Product(701, "3. Samsung LED", 40000, 1))
shoppingCart.add(Product(401, "4. Samsung M10", 1000, 3))

shoppingCart.iterate()

print("#####################")

shoppingCart.poll()
shoppingCart.poll()

shoppingCart.iterate()


print("HEAD OF QUEUE")
shoppingCart.peek()


"""
    IMPLEMENT SELECTION SORT IN LINKEDLIST

    class LinkedList:
        pass
        
    class Stack(LinkedList):
        pass    

    class Queue(LinkedList):
        pass

"""
