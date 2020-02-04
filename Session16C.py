file = open("Session15C.py", "r")
"""
line1 = file.readline()
print(line1)

line2 = file.readline()
print(line2)

line3 = file.readline()
print(line3)
"""

lines = file.readlines()
print(type(lines))

functions = 0
for line in lines:
    if "def" in line:
        print(line)
        functions += 1

print(">> Total Functions:", functions)

# SOURCE CODE ANALYSIS
# Find Number of Objects in Session16.py by reading the Files
# Those Objects belongs to which class that should also be found
# Finally, create a dictionary where key is class and value is number of objects
