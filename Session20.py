# Function
def hello():
    print(">> This is hello")
    return "Hello"
    # return "Bye" # This wont work

result = hello()
print(">> result is:", result)


# Generator IS-A Function
def helloAgain():
    print(">> This is helloAgain")
    yield "Hi"
    yield "Hello"
    yield "He Ya"
    yield "Bye"


ha = helloAgain
print(helloAgain)
print(ha)

# result = ha()
# print(">> result is:", result)

# Executing a function with yield statement(s) makes a function as Generator
result = helloAgain()
print(">> result is:", result)
print(next(result))
print(next(result))
print(next(result))
print(next(result))
# print(next(result)) # error

