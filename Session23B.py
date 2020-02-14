# tkinter can be used to create GUIs
# BUT, tkinter needs exploration :)
# import tkinter

from tkinter import *
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("key.json")
firebase_admin.initialize_app(cred)
print(">> Firebase Configured and Initialized :)")


class Customer:
    def __init__(self, name=None, phone=None, email=None):
        self.name = name
        self.phone = phone
        self.email = email

    def showCustomer(self):
        print("{} | {} | {}".format(self.name, self.phone, self.email))


def clickHandler():
    print(">> Button Clicked")
    customer = Customer()
    customer.name = entryName.get()
    customer.phone = entryPhone.get()
    customer.email = entryEmail.get()

    customer.showCustomer()

    customerData = customer.__dict__

    db = firestore.client()
    db.collection("mycustomers").document(customer.email).set(customerData)
    print(">> CUSTOMER SAVED")


# Creating a Window :)
# Window is a frame with minimize, maximize and close buttons
window = Tk()

lblTitle = Label(window, text="Customer Management Solution")
lblTitle.pack()

lblName = Label(window, text="Enter Customer Name")
lblName.pack()

entryName = Entry(window)
entryName.pack()

lblPhone = Label(window, text="Enter Customer Phone")
lblPhone.pack()

entryPhone = Entry(window)
entryPhone.pack()

lblEmail = Label(window, text="Enter Customer Email")
lblEmail.pack()

entryEmail = Entry(window)
entryEmail.pack()

btnAddCustomer = Button(window, text="Add Customer", command=clickHandler)
btnAddCustomer.pack()

# Show the window in an infinite loop :)
window.mainloop()

