class BankingError(Exception):
    pass

class BankAccount:

    def __init__(self):
        self.balance = 10000
        self.minBalance = 2000
        self.attempts = 0
        print(">> Account Activated and Balance is \u20b9", self.balance)

    def withdraw(self, amount):
        self.balance -= amount
        if self.balance < self.minBalance:
            self.balance += amount
            print(">> [F] Withdraw Failed")
            print(">> [F] Balance is LOW \u20b9", self.balance)
            self.attempts += 1
        else:
            print(">> [P] Withdraw Successfully Done")
            print(">> [P] New Balance is \u20b9", self.balance)

        if self.attempts == 3:
            # error = IndexError("Illegal Attempts !!")
            error = BankingError("Illegal Attempts !!")
            raise error

print(">> Banking Started")
johnsAccount = BankAccount()
"""
johnsAccount.withdraw(3000)
johnsAccount.withdraw(3000)
johnsAccount.withdraw(3000)
johnsAccount.withdraw(3000)
johnsAccount.withdraw(3000)
"""

for i in range(1, 6000):
    johnsAccount.withdraw(3000)

print(">> Banking Finished")

"""
    Nesting of try except finally :)
    try:
        try:
    
        except:
    
        finally:
    except:
        try:
    
        except:
    
        finally:
    finally:
        try:
    
        except:
    
        finally:
    
"""
