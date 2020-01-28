# 1. Think of an Object
#    Customer is Object
#    name, phone, email, gender, address are Attributes

# 2. Create its Class
class Customer:

    # __init__ : constructor, which gets executed when we create object
    # self is a reference variable, which holds the hashcode of current object
    # name of self can by any name of your choice
    # BUT self is always the first input to __init__
    def __init__(self):
        print("init executed")
        print(">> self is:", self)
        self.name = "John"


# 3. From Class Create Real Object
cRef1 = Customer()  # Object Construction Statement
print(">> cRef1 is:", cRef1)
cRef1.phone = "+91 99999 88888"

print(cRef1.__dict__)

cRef2 = Customer()
cRef2.phone = "+91 98765 65432"

print(cRef2.__dict__)

# Reference Copy Operation
cRef3 = cRef1