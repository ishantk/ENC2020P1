# What is Inheritance ?
# It is a Relationship between 2 classes,
# where child class is allowed to access properties of parent class

class Parent:

    # Property of Parent Class
    vehicle = "PB10AB1234"

    # Property of Parent Class
    def __init__(self, fname, lname, wealth):
        # self.fname, self.lname and self.wealth is Property of Object
        self.fname = fname
        self.lname = lname
        self.wealth = wealth

    # Property of Parent Class
    def showDetails(self):
        print("{} | {} | {} | {}".format(self.fname, self.lname, self.wealth, Parent.vehicle))

# Inheritance
class Child(Parent):

    # Property of Child Class
    vehicle = "KA10XY3333"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    # Property of Parent Class
    def showDetails(self):
        print("{} | {} | {}".format(self.name, self.salary, Child.vehicle))

    def show(self, ref):
        print("{} | {} | {}".format(self.name, self.salary, Child.vehicle))
        Parent.showDetails(ref)

# Object of Child
cRef = Child("Fionna Flynn", 30000)
print(">> Dictionary of cRef")
print(cRef.__dict__)

print(Child.vehicle)   # OK
print(cRef.vehicle)    # OK


# cRef.showDetails()
Child.showDetails(cRef)

pRef = Parent("John", "Watson", 200000)
pRef.showDetails()

print("~~~~~~~~~~~~~~~")

cRef.show(pRef)

# Lookup Rule:
# If we have not found an attribute in Object, look up for the same in Class
# In Inheritance, lookup shall go upto Parent

