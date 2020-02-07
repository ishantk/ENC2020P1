def fun():
    print("This is fun in Session19")


class CA:
    def __init__(self):
        print("CA Object Constructed in Session19")


def main():
    print("This is Session19")
    print("Session19 __name__ is:", __name__)
    fun()
    cRef = CA()

if __name__ == "__main__":
   main()