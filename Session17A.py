"""

    DataBase
	Permanent Data Store :)
	Prefer DataBase over Files :)
	> 1. Security
	> 2. Centralization
	> 3. Operations | Time Optimized
		 Insert
		 Update
		 Delete
		 Fetch/Query/Retrieve
	> 4. Structured Data Storage
	     We have Tables
	     In Tables we have rows
	     and in rows we have data as columns :)

	> 5. DataBase Represents a Data Structure

	examples:
	MySQL and Oracle 	| SQL
	Tree Data Structure

	FirebaseFirestore	| No SQL
	Tree Data Structure

	Neo4J				| No SQL
	Graph Data Structure

	ORM (Object Relational Mapping)
	SQL
	1. Create Table

    create table Customer(
        id int primary key auto_increment,
        name varchar(256),
        phone varchar(20),
        email varchar(256)
    )

    2. Insert Data Into Table
    insert into Customer values(null, 'John', '+91 99999 88888', 'john@example.com')


    STEPS to Perform DB Interaction
    1. Download the library and install it in your Python Project
       > Settings of your project
       > execute pip install command on terminal
    2. Write SQL Statement to be executed and substitute the data
    3. import mysql.connector in your program
    4. Create Connection to DataBase with library
    5. Obtain Cursor from Connection to execute SQL Statement
    6. Execute SQL Statement and Commit It :)

"""

import mysql.connector as lib
# import mysql.connector

class Customer:

    def __init__(self):
        self.id = 0
        self.name = input("Enter Customer Name: ")
        self.phone = input("Enter Customer Phone: ")
        self.email = input("Enter Customers Email: ")


    def showCustomerDetails(self):
        print("{} | {} | {}".format(self.name, self.phone, self.email))


print("==Welcome to Customer Management Software==")
print("1. Register New Customer")

choice = int(input("Enter Your Choice: "))
usage = "yes"
while usage == "yes":
    if choice == 1:
        customer = Customer()
        customer.showCustomerDetails()

        save = input("Would you like to Save Customer? (yes/no): ")
        if save == "yes":

            sql = "insert into Customer values(null, '{}', '{}', '{}')".format(customer.name, customer.phone, customer.email)
            #con = mysql.connector.connect(user="root", password="", database="auridb", host="127.0.0.1", port="3306")
            con = lib.connect(user="root", password="", database="auridb", host="127.0.0.1", port="3306")
            print(">> Connection Created :)")
            cursor = con.cursor()
            cursor.execute(sql)
            con.commit()

            print(">> CUSTOMER SAVED :)")

            usage = input("Would You Like Use Software Further? (yess/no): ")