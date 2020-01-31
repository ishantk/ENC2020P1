def applyPromoCode(amount, promoCode):
    if amount >= 100:
        if promoCode == "ZOMATO":
            # amount = amount - (0.4 * amount)
            amount -= (0.4 * amount)
            print(">> ZOMATO Applied")
            print(">> Please Pay \u20b9", amount)
        elif promoCode == "JUMBO" and amount >= 200:
            discount = 0.5 * amount
            if discount <= 150:
                amount -= discount
            else:
                amount -= 150
            print(">> JUMBO Applied")
            print(">> Please Pay \u20b9", amount)
        else:
            print(">> Please use either ZOMATO or JUMBO to get Discounts")
    else:
        print(">> To avail Discounts and to Use Promo Codes")
        print(">> Add items worth of {} more".format(100 - amount))


choice = "yes"

while choice == "yes":
    amount = float(input("Enter an Amount: "))
    promoCode = input("Enter a Promo Code")
    applyPromoCode(amount, promoCode)

    choice = input("Would you like to apply another code: (yes/no): ")

# Functions Leads to modularization


"""
    f(x) = x*x + 1
    x : 1 => 2
    x : 2 => 5
    
    applyPromoCode(amount, promoCode) =>
"""
"""
def f(x):
    result = x*x + 1
    print(">> result:", result)


def f(x):
    return x*x + 1
"""

