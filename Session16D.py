file = open("Session15C.py", "r")

print(file.tell())  #0

# Move Cursor Location
file.seek(10)
data = file.read(15)
print(data)

# Tell Cursor Location
print(file.tell())  #25


