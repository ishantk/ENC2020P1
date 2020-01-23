"""
    MODEL -> SVC and MVC
    VIEW  -> input()
    CONTROLLER | Logic
        Computation
            Operators
        Conditional Flow
            if/else / Ladder if/else / Nested if/else
        Iterations
            while, for and enhanced for

"""

print(">> \u0905")

num1 = 10
num2 = 3
# num3 = num1 / num2
num3 = num1 // num2

print(num3)

num = 8                     # 0 0 0 0  1 0 0 0
result = num >> 2           # _ _ 0 0  0 0 1 0 ->  0 0 0 0  0 0 1 0
print(">> result:", result)

result = num << 2           # 0 0 0 0  1 0 0 0
print(">> result:", result) # 0 0 1 0  0 0 _ _ -> # 0 0 1 0  0 0 0 0


num = 11                    # 1 0 1 1 >> 2   _ _ 1 0 -> 0 0 1 0
result = num >> 2
print(">> result:", result)

num = -11
result = num >> 3
print(">> result:", result)

# 1 0 1 1
# 0 1 0 0
#       1
# 0 1 0 1 >> 2  _ _ 0 1 -> 1 1 0 1

# 1 1 0 1
# 0 0 1 0
#       1
# 0 0 1 1 -> -3

print("*********")

data = 12
key = 2
result = data >> key
print(result)

anotherResult = result << key
print(anotherResult)


