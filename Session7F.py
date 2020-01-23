menu = {
    "paneer": 200,
    "dal": 100,
    "roti": 10,
    "champ": 150,
    "salad": 10,
    "noodles": 120
}


# print("paneer tikka" in menu)

cart = []
print(cart, type(cart), len(cart))

choice = "yes"

# print(">> Menu For You:")
# print(menu.keys())

while choice == "yes":
    foodItem = input("Enter a Food Item:")

    if foodItem in menu:
        cart.append(foodItem)
        choice = input("Would you like to add another Food Item (yes/no):")
    else:
        print(">> Please choose another food item")


print("Your Cart:", cart)
totalPrice = 0
# for item in cart:
#     print(item, menu[item])
#     totalPrice = totalPrice + menu[item]

for i in range(0, len(cart)):
    item = cart[i]
    print(item, menu[item])
    totalPrice = totalPrice + menu[item]

print(">> Total Price:", totalPrice)
promoCode = input("Enter Promo Code: ")
# Below this you guys code

# extend functions supports MUTABILITY i.e. changes the same List
# rather than creating a new one :)
"""
cart.extend(["salad", "noodles"])

print("Surprises in Cart:", cart)

cart.insert(1, "champ")

print(">> More Surprise in Cart", cart)

cart.pop(2)
print(">> Final Cart", cart)
"""

