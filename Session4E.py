"""
amount = float(input("Enter Total Amount: "))
minAmount = 500

# Regular if/else
if amount > minAmount:
    amount = amount - (0.5*amount)
    print(">> You got 50% OFF. Please Pay: \u20b9", amount)
else:
    print(">> Sorry No Discounts !!")
    print(">> Please add items worth of \u20b9", (minAmount-amount), "to get 50% OFF")
"""

"""
200 > 40%Off Zomato
100 > 50%Off upto 150 JUMBO

"""

amount = float(input("Enter Total Amount: "))
promoCode = input("Enter Promo Code: ")

# Ladder if/else
if amount > 200 and promoCode == "Zomato":
    amount = amount - (0.4 * amount)
    print(">> Promo Code Zomato Applied Successfully. 40% OFF. Please Pay: \u20b9", amount)

elif amount > 100 and promoCode == "JUMBO":

    discount = 0.5*amount
    # Nested if/else
    if discount > 150:
        amount -= 150
    else:
        amount -= discount

    print(">> Promo Code JUMBO Applied Successfully. 50% OFF. Please Pay: \u20b9", amount)

else:
    print(">> No Promo Code Found and no Discount Available")
    print(">> Please Pay: \u20b9", amount)

# HW: Suggect Correct Promo Code to be applied