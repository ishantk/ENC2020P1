name = "John"
phone = "+91 99999 88888"
address = "Redwood Shores"
data = "{},{},{}\n".format(name, phone, address)
print(data)

# file = open("data.csv", "w")
file = open("data.csv", "a")
file.write(data)
file.close()

print(">> Data Saved in File")

