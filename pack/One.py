def fun():
    print(">> This is fun in One")


def show():
    print(">> __name__ is:",__name__)


class CA:
    def __init__(self):
        print(">> CA Object Constructed in One")

def main():
    a = 10
    b = a ** 2
    print(">> This is suppose to be executed :)", b)

if __name__ == "__main__":
    main()


