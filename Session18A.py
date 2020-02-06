import mysql.connector as lib

"""

PS: https://www.w3schools.com/sql/sql_foreignkey.asp
    JOINS :)

create table Customer(
	id int primary key auto_increment,
	name varchar(256),
	phone varchar(256),
	email varchar(256)
)

create table Orders(
	oid int primary key auto_increment,
	price int,
	id int,
	foreign key (id) references Customer(id)
)


"""


# CONTROLLER
# DAO | Data Access Object | Design Pattern
class DB:

    def __init__(self):
        self.con = lib.connect(user="root", password="", database="auridb", host="127.0.0.1", port="3306")

    def executeWriteOperation(self, sql):
        cursor = self.con.cursor()
        cursor.execute(sql)
        self.con.commit()
        print("SQL Executed")

    def executeReadOperation(self, sql):
        cursor = self.con.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        return rows


db = DB()

# MODEL
class Customer:

    def __init__(self, mode):
        if mode == 1:
            self.id = 0
            self.name = input("Enter Customer Name: ")
            self.phone = input("Enter Customer Phone: ")
            self.email = input("Enter Customers Email: ")
        elif mode == 2:
            self.id = int(input("Enter Customer ID: "))
            sql = "select * from Customer where id = {}".format(self.id)
            rows = db.executeReadOperation(sql)
            print(rows[0])
            self.name = input("Enter Customer Name: ")
            self.phone = input("Enter Customer Phone: ")
            self.email = input("Enter Customers Email: ")
        else:
            pass

    def showCustomerDetails(self):
        print("{} | {} | {} | {}".format(self.id, self.name, self.phone, self.email))



# APPLICATION :)
def main():
    # VIEW
    repeat = "yes"

    while repeat == "yes":

        print("==Welcome to Customer Management App==")
        print("1. Register New Customer")
        print("2. Update Existing Customer")
        print("3. Delete Existing Customer")
        print("4. View All Customers")
        print("5. View Customer by ID")
        print("6. View Customer by Phone")

        choice = int(input("Enter Your Choice: "))

        if choice == 1:
            customer = Customer(1)
            customer.showCustomerDetails()

            save = input("Would you like to Save Customer? (yes/no): ")
            if save == "yes":
                sql = "insert into Customer values(null, '{}', '{}', '{}')".format(customer.name, customer.phone, customer.email)
                db.executeWriteOperation(sql)
                print(">> CUSTOMER SAVED :)")

        elif choice == 2:

            customer = Customer(2)
            customer.showCustomerDetails()

            save = input("Would you like to Update Customer? (yes/no): ")
            if save == "yes":
                sql = "update Customer set name = '{}', phone='{}', email= '{}' where id = {}".format(customer.name, customer.phone, customer.email, customer.id)
                db.executeWriteOperation(sql)
                print(">> CUSTOMER UPDATED :)")

        elif choice == 3:

            id = int(input("Enter Customer ID to be Deleted: "))
            delete = input("Would you like to Delete Customer? (yes/no): ")

            if delete == "yes":
                sql = "delete from Customer where id = {}".format(id)
                db.executeWriteOperation(sql)
                print(">> CUSTOMER DELETED :)")

        elif choice == 4:

            # sql = "select id, name from Customer"
            sql = "select * from Customer"
            rows = db.executeReadOperation(sql)

            for row in rows:
                customer = Customer(3)
                customer.id = row[0]
                customer.name = row[1]
                customer.phone = row[2]
                customer.email = row[3]
                # print(row)
                customer.showCustomerDetails()


        elif choice == 5:
            id = int(input("Enter Customer ID to be Searched: "))
            sql = "select * from Customer where id = {}".format(id)
            rows = db.executeReadOperation(sql)

            if rows is not None:
                print(rows)
            else:
                print(">> ID Not Found")

        elif choice == 6:
            phone = input("Enter Customer Phone to be Searched: ")
            sql = "select * from Customer where phone = '{}'".format(phone)
            con = lib.connect(user="root", password="", database="auridb", host="127.0.0.1", port="3306")
            cursor = con.cursor()
            cursor.execute(sql)
            rows = db.executeReadOperation(sql)

            if rows is not None:
                print(rows)
            else:
                print(">> Customer with Phone Number {} Not Found".format(phone))

        else:
            print(">> Enter a Valid Choice")


        repeat = input("Would You Like to Re Use App (yes/no): ")


if __name__ == "__main__":
    main()