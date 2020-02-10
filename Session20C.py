# Function with Input to Reference of Function

def hello(fun):
    print(">> Hello...")
    fun()


def bye():
    print(">> Bye...")


def show(num=10):
    print(">> showing", num)


# Passing Function as Argument
hello(fun=bye)
print("~~~~~~~~~")
hello(fun=show)



# Factory Design Pattern
# Create with help of Concept called Polymorphism (Run Time)
def loginWithFaceBook():
    print(">> Login With FaceBook")

def loginWithGoogle():
    print(">> Login With Google")

def loginWithGitHub():
    print(">> Login With GitHub")

def login(type):
    type()


print("-----------------------")
print("|1 Login With Facebook|")
print("-----------------------")
print("|2 Login With Google  |")
print("-----------------------")
print("|3 Login With GitHub  |")
print("-----------------------")
choice = int(input("Select Your Login Type"))

if choice == 1:
    login(loginWithFaceBook)
elif choice == 2:
    login(loginWithGoogle)
elif choice == 3:
    login(loginWithGitHub)
else:
    print(">> Please Select Valid Choice")