"""
name = input("Enter Your Name:")
print(name, type(name))

print()

# age = input("Enter Your Age:")
age = int(input("Enter Your Age:"))
print(age, type(age))

# CASTING
# iAge = int(age)
# print(iAge, type(iAge))
"""

"""
num = 8
print(bin(num))     # 1 0 0 0
# Rt shift is divide number by 2 power n
result = num >> 2   # _ _ 1 0 -> 0 0 1 0 -> 2
print(">> result:", result)

num = 11            # 1 0 1 1
result = num >> 2   # _ _ 1 0 -> 0 0 1 0 -> 2
print(">> result:", result)

num = -11
result = num >> 2
print(">> result:", result)

# 1 0 1 1   11
# 0 1 0 0   1s
#       1   2s
# 0 1 0 1   -11
# >> 2
# _ _ 0 1
# 1 1 0 1

# 0 0 1 0
#       1
# 0 0 1 1 -> -3

num = -13
result = num >> 2
print(">> result:", result)

# Left shift is multiply number by 2 power n

num = 8                 # -> 0 0 0 0  1 0 0 0
result = num << 2       # -> 0 0 1 0  0 0 0 0
print(result)

print(result >> 2)
"""

# ZOMATO -> Flat 40% Off | min amount 100
# JUMBO  -> Flat 50% Off | upto 150 min amount 200

amount = float(input("Enter an Amount: "))
promoCode = input("Enter a Promo Code")

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


"""
    Simple if/else
    if/else
    
    Ladder if/else
    if/elif/else
    
    Nested if/else
    if->if/else | else->if/else
"""

