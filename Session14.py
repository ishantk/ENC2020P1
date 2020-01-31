class CA:
    # In Python, OVERLOADING is not SUPPORTED
    def __init__(self):
        print(">> CA Object Constructed")

    # If you re-define previous function again, it will be deleted
    def __init__(self, num):
        print(">> CA Object Constructed and num is:",num)


cRef = CA(10)
# So, we need to maintain standardization while creating Objects

