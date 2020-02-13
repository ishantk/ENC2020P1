# Fee for Different Sizes of Property
feeStructure = {

    "100": 100,
    "200": 150,
    "300": 200,
    "400": 250,
    "500": 300
}

class Property:

    def __init__(self, houseNum=None, block=None, street=None, area=None, size=None):
        self.houseNum = houseNum
        self.block = block
        self.street = street
        self.area = area
        self.size = size

    def inputPropertyDetails(self):
        self.houseNum = input("Enter House Num: ")
        self.block = input("Enter House Block: ")
        self.street = input("Enter House Street: ")
        self.area = input("Enter House Area: ")
        self.size = int(input("Enter House Size: "))

    def showProperty(self):
        print("{} | {} | {} | {} | {}".format(self.houseNum, self.block, self.street, self.area, self.size))

    def toCSV(self):
        return "{},{},{},{},{}".format(self.houseNum, self.block, self.street, self.area, self.size)

class Customer:

    def __init__(self, name=None, phone=None, email=None, property=None):
        self.name = name
        self.phone = phone
        self.email = email
        self.property = property

    def inputCustomerDetails(self):
        self.name = input("Enter Customer Name: ")
        self.phone = input("Enter Customer Phone: ")
        self.email = input("Enter Customer Email: ")

    # Has-A Relationship
    def linkPropertyToCustomer(self, property):
        self.property = property

    def showCustomer(self):
        print("{} | {} | {}".format(self.name, self.phone, self.email))
        self.property.showProperty()

    def toCSV(self):
        return "{},{},{},{}\n".format(self.name, self.phone, self.email, self.property.toCSV())


class Fee:

    def __init__(self, phone=None, month=None, year=None, amount=None):
        self.phone = phone
        self.month = month
        self.year = year
        self.amount = amount

    def inputFeeDetails(self):
        self.phone = input("Enter Customer Phone: ")
        self.month = int(input("Enter Month: "))
        self.year = int(input("Enter Year: "))

        # Amount must be fetched automatically
        file = open("gc-customers.csv", "r")
        lines = file.readlines()

        # Implement Linear Search on List
        for line in lines:
            data = line.split(",")
            if data[1] == self.phone:
                size = data[len(data)-1].strip()
                self.amount = feeStructure[size]
                break

        lastMonth = self.getLastFeePaidMonth()
        difference = self.month - lastMonth

        if difference == 1:
            print(">> Fee to be Paid on {} month {} year : \u20b9{}".format(self.month, self.year, self.amount))
        else:
            print(">> Fee Not Paid for {} months".format(difference))


    # Fetching Fee Paid in the Last Month
    def getLastFeePaidMonth(self):
        file = open("gc-fees.csv", "r")
        lines = file.readlines()
        lastFeeLine = None

        # Time Complexity - O(n)
        for line in lines:
            data = line.split(",")
            if data[0] == self.phone:
                lastFeeLine = line

        data = lastFeeLine.split(",")
        month = int(data[1])
        return month

    def showFee(self):
        print("{} | {} | {} | {}".format(self.phone, self.month, self.year, self.amount))

    def toCSV(self):
        return "{},{},{},{}\n".format(self.phone, self.month, self.year, self.amount)



def main():

    print("===Garbage Collector App===")

    print("1. Add Customer")
    print("2. Charge Garbage Fee")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:

        property = Property()
        property.inputPropertyDetails()

        customer = Customer()
        customer.inputCustomerDetails()

        customer.linkPropertyToCustomer(property)

        customer.showCustomer()
        data = customer.toCSV()
        print(data)

        save = input("Would you like to save {} (yes/no)".format(customer.name))
        if save == "yes":
            file = open("gc-customers.csv", "a")
            file.write(data)
            file.close()
            print(">> Customer Saved in File")


    elif choice == 2:

        fee = Fee()
        fee.inputFeeDetails()
        fee.showFee()

        data = fee.toCSV()

        save = input("Would you like to save Fee {} for {} (yes/no)".format(fee.amount, fee.phone))
        if save == "yes":
            file = open("gc-fees.csv", "a")
            file.write(data)
            file.close()
            print(">> Fee Saved in File")

    else:
        print(">> Select Valid Choice")



if __name__ == "__main__":
    main()