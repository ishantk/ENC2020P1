amount = int(input("Enter an Amount: "))
promoCode = input("Enter Promo Code: ")


"""
if amount > 100:
    if promoCode == "ZOMATO":
        amount -= 0.4 * amount
        print(">> Promo Code Applied Successfully")
        print(">> Please Pay \u20b9",amount)
    else:
        print(">> Invalid Promo Code")
        print(">> Use ZOMATO to avail 40% Off")
else:
    print(">> Please Pay \u20b9", amount)
    print(">> To avail 40% Off add product worth \u20b9", (100-amount))
"""

# Ladder if/else
if amount > 100 and amount < 500:
    if promoCode == "ZOMATO":
        amount -= 0.4 * amount
        print(">> Promo Code Applied Successfully")
        print(">> Please Pay \u20b9",amount)
    else:
        print(">> Invalid Promo Code")
        print(">> Use ZOMATO to avail 40% Off")
elif amount > 500:
    if promoCode == "JUMBO":
        amount -= 0.5 * amount
        print(">> Promo Code Applied Successfully")
        print(">> Please Pay \u20b9",amount)
    else:
        print(">> Invalid Promo Code")
        print(">> Use JUMBO to avail 50% Off")
else:
    print(">> Please Pay \u20b9", amount)
    print(">> To avail 40% Off add product worth \u20b9", (100-amount))
    print(">> To avail 50% Off add product worth \u20b9", (500 - amount))