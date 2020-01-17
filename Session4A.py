"""

    CONTROLLER
        1. Computation
            Operators -> Perform some mathematical operations
        2. Conditional Flow
            if/else, ladder if/else, nested if/else
        3. Iterations
            while, for, enhanced for | (for-each)

"""

# Operators
# Arithmetic +, -, *, **, /, //, %

dish1 = 100
dish2 = 150

billAmount = dish1 + dish2
taxes = 0.05 * billAmount

billAmount = billAmount + taxes

# rupee = "₹"

print(">> Please Pay: \u20b9", billAmount)

num = 2
result = num ** 3
print(">> result:", result)

num1 = 10
num2 = 3
# num3 = num1 / num2
num3 = num1 // num2
print(">> num3 is:", num3)

num4 = 10 % 3
print(">> num4 is:", num4)

# HW1: number 123 -> 1+2+3 -> 6 -> even
#             1*10pow2 + 2*10pow1 + 3*10pow0
# HW2: number 123 -> One Twenty Three

number = int(input("Enter a 3 digit number:"))
print(">> Your Entered Number is:", number)
n1 = number // 100  # 1
n2 = number % 100   # 23
n3 = n2 // 10
n4 = n2 % 10
print(n1)
print(n2)
print(n3)
print(n4)

sum = n1 + n3 + n4
print(">> Sum is:",sum)

