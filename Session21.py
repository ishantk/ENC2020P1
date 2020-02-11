"""
1. Install Firebase Admin Library
   pip install firebase-admin

   If facing errors, try upgrading your pip
   python -m pip install -U --force-reinstall pip

2. Go to firebase.google.com
   Create a New Project (edit project id of your choice)
   Use Locations as India

3. Create DataBase in your Account
    Create Firestore in Test Mode
    Location -> Asia-South1 [But it can be any of your choice]

    Explore DataBase with collections and documents structure :)

4. Go To Settings
    Project Settings > Service Accounts
    Select Python
    Generate Private Key (It shall download a json file)

5. Copy this downloaded json file in your Pycharm Project and rename it to anyname.json

6. Copy the Snippet and paste it in your program


"""
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("key.json")
firebase_admin.initialize_app(cred)
print(">> Firebase Configured and Initialized :)")

# MODEL
class Customer:

    def __init__(self):
        self.name = input("Enter Customer Name: ")
        self.phone = input("Enter Customer Phone: ")
        self.email = input("Enter Customers Email: ")

    def showCustomerDetails(self):
        print("{} | {} | {}".format(self.name, self.phone, self.email))



# APPLICATION :)
def main():
    customer = Customer()
    customer.showCustomerDetails()

    customerData = customer.__dict__
    print(customerData, type(customerData))

    # db is reference to Firestore Database
    db = firestore.client()
    db.collection("customers").document(customer.email).set(customerData)
    print(">> CUSTOMER SAVED")

if __name__ == "__main__":
    main()