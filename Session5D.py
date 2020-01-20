"""

    Functions
    f(x) = x*x + 1
    f(n) = 2*n*n + n + 1
    f(x, y) = x*x + y*y + 2*x*y

"""

num = 10
print(">> num is:", num)
print(">> num is:", hex(id(num)))

def f1(x):
    return x*x + 1

print(">> f1 is:", f1)

def f2(n):
    return 2*n*n + n + 1

print(">> f2 is:", f2)

# PS: if you create functions with same name again and again
#     you will get no errors
#     old function is deleted and new function is created

# Execution of function
print(">> f1(2) is:", f1(2))
print(">> f2(3) is:", f2(3))

# HW: Try implement below function
def applyPromoCode(amount, promCode):
    pass

# HW: Try Implement sorting on List with function