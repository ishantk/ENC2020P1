"""
200 > 40%Off             PC: ZOMATO
100 > 50%Off upto 150    PC: JUMBO
"""

amount = int(input("Enter an amount: "))
promoCode = input("Enter Promo Code: ")

print(">> Your Amount is:", amount)
print(">> Your PromoCode is:", promoCode)

"""
if amount > 200:
    if promoCode == "ZOMATO":
        amount = amount - (0.4*amount)
        print(">> ZOMATO Applied Successfully !! 40% OFF")
        print(">> Please Pay: \u20b9", amount)
    else:
        print(">> Try using ZOMATO to get 40% OFF")
elif amount > 100:
    if promoCode == "JUMBO":
        discount = 0.5 * amount
        if discount > 150:
            amount = amount - 150
        else:
            amount = amount - discount

        print(">> JUMBO Applied Successfully !! 50% OFF upto 150")
        print(">> Please Pay: \u20b9", amount)
    else:
        print(">> Try using JUMBO to get 50% OFF")

else:
    print(">> Please Pay: \u20b9", amount)
"""

# HW: Rectify the Use Case Above. Hint shared below:
#     You need to suggest correct promo code as well
if amount > 100:
    if promoCode == "ZOMATO" and amount > 200:
        pass
    elif promoCode == "JUMBO":
        pass


