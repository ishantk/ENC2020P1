# https://www.python.org/dev/peps/pep-0008/
# Passing References | As Value
def square(num): # num is a Reference Variable which holds HashCode of 10
    print(">> [SQUARE] num is:", num, hex(id(num)))
    num = num * num
    print(">> [SQUARE] num now is:", num, hex(id(num)))


num = 10  # num is a Reference Variable which holds HashCode of 10
print(">> [MAIN] num is:", num, hex(id(num)))
square(num)
print(">> [MAIN] num now is:", num, hex(id(num)))

