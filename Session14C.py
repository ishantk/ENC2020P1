# Why Inheritance
# 1. Code ReUsability
# 2. Only write additional details in Children
# 3. Saves TIME [DEVELOPMENT] :)

# Inheritance leads to Generalization | IS-A Relationship

"""
class Shoe:
    def __init__(self, pid, name, price, brand, shoeSize):
        self.pid = pid
        self.name = name
        self.price = price
        self.brand = brand
        self.shoeSize = shoeSize

    def showShoeDetails(self):
        print("======{} | {}======".format(self.pid, self.name))
        print("{} | {} | {}".format(self.price, self.brand, self.shoeSize))
        print("===========================")


class MobilePhone:
    def __init__(self, pid, name, price, brand, ram, os):
        self.pid = pid
        self.name = name
        self.price = price
        self.brand = brand
        self.ram = ram
        self.os = os

    def showMobilePhoneDetails(self):
        print("======{} | {}======".format(self.pid, self.name))
        print("{} | {} | {}".format(self.price, self.brand))
        print("{} | {}".format(self.ram, self.os))
        print("===========================")


class LEDTV:
    def __init__(self, pid, name, price, brand, screenSize, technology):
        self.pid = pid
        self.name = name
        self.price = price
        self.brand = brand
        self.screenSize = screenSize
        self.technology = technology

    def showLEDTVDetails(self):
        print("======{} | {}======".format(self.pid, self.name))
        print("{} | {} | {}".format(self.price, self.brand))
        print("{} | {}".format(self.screenSize, self.technology))
        print("===========================")

"""

class Product:
    def __init__(self, pid, name, price, brand):
        self.pid = pid
        self.name = name
        self.price = price
        self.brand = brand

    def showProductDetails(self):
        print("########{} | {}########".format(self.pid, self.name))
        print("{} | {}".format(self.price, self.brand))
        print("###########################")

# Shoe IS-A Product
class Shoe(Product):
    def __init__(self, pid, name, price, brand, shoeSize):
        Product.__init__(self, pid, name, price, brand)
        self.shoeSize = shoeSize

    def showShoeDetails(self):
        Product.showProductDetails(self)
        print("{}".format(self.shoeSize))
        print("===========================")


# MobilePhone IS-A Product
class MobilePhone(Product):
    def __init__(self, pid, name, price, brand, ram, os):
        Product.__init__(self, pid, name, price, brand)
        self.ram = ram
        self.os = os

    def showMobilePhoneDetails(self):
        Product.showProductDetails(self)
        print("{} | {}".format(self.ram, self.os))
        print("===========================")


# LEDTV IS-A Product
class LEDTV(Product):
    def __init__(self, pid, name, price, brand, screenSize, technology):
        Product.__init__(self, pid, name, price, brand)
        self.screenSize = screenSize
        self.technology = technology

    def showLEDTVDetails(self):
        Product.showProductDetails(self)
        print("{} | {}".format(self.screenSize, self.technology))
        print("===========================")


sRef = Shoe(101, "AlphaBounce", 8000, "Adidas", 8)
mRef = MobilePhone(201, "iPhoneX", 70000, "Apple", 4, "iOS")
lRef = LEDTV(301, "Samsung Curved", 50000, "Samsung", 50, "OLED")

sRef.showShoeDetails()
mRef.showMobilePhoneDetails()
lRef.showLEDTVDetails()
