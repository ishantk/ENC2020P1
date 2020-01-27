items = ["dal", "paneer", "roti"]
prices = [100, 200, 20]

menu = {"burger": 100}

print(items)
print(prices)
print(menu)

for i in range(0, len(items)):
    menu[items[i]] = prices[i]


print(">> Menu is:", menu)

del menu["burger"]

print(">> Menu now is:", menu)
