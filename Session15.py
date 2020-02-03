# Extending Code
# Decorate Object :) with a Helper

"""
class Customer:

    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def showCustomer(self):
        print("CUSTOMER: {} | {} | {}".format(self.name, self.phone, self.email))

    def showPrimeCustomer(self):
        print("PRIME CUSTOMER : {} | {} | {} | {}".format(self.name, self.phone, self.email, self.type))


cRef1 = Customer("John", "+91 99999 88888", "john@example.com")
cRef2 = Customer("Fionna", "+91 78901 88888", "fionna@example.com")

cRef2.type = 1


print(cRef1.__dict__)
print(cRef2.__dict__)

cRef1.showCustomer()
cRef2.showCustomer()

cRef1.showPrimeCustomer()
cRef2.showPrimeCustomer()
"""


# Inheritance : Extending :)
"""
class Customer:

    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def showCustomer(self):
        print("CUSTOMER: {} | {} | {}".format(self.name, self.phone, self.email))


# Inheritance : Extending :)
class PrimeCustomer(Customer):

    def upgrageToPrime(self):
        self.prime = True
        self.videos = True
        self.music = True

    def showPrimeCustomer(self):
        self.showCustomer()

        customerDetails = self.__dict__
        keys = customerDetails.keys()

        if "prime" in keys:
            print("PRIME FEATURES: VIDEOS: {} | MUSIC: {}".format(self.videos, self.music))



cRef1 = Customer("John", "+91 99999 88888", "john@example.com")
cRef2 = Customer("Fionna", "+91 78901 88888", "fionna@example.com")
print(cRef1.__dict__)

PrimeCustomer.upgrageToPrime(cRef1)
print(cRef1.__dict__)

PrimeCustomer.showPrimeCustomer(cRef1)
print()

PrimeCustomer.upgrageToPrime(cRef2)
PrimeCustomer.showPrimeCustomer(cRef2)

"""

class Customer:

    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def showCustomer(self):
        print("CUSTOMER: {} | {} | {}".format(self.name, self.phone, self.email))


# Inheritance : Extending :)
class PrimeCustomer(Customer):

    def  __init__(self, customer):
        customer.prime = True
        customer.videos = True
        customer.music = True

    def showPrimeCustomer(self, customer):
        customer.showCustomer()

        customerDetails = customer.__dict__
        keys = customerDetails.keys()

        if "prime" in keys:
            print("PRIME FEATURES: VIDEOS: {} | MUSIC: {}".format(customer.videos, customer.music))


cRef1 = Customer("John", "+91 99999 88888", "john@example.com")
primecRef1 = PrimeCustomer(cRef1)

print(cRef1.__dict__)
print(primecRef1.__dict__)

primecRef1.showPrimeCustomer(cRef1)

# Write Program for McDonalds Meal Upgrade :)