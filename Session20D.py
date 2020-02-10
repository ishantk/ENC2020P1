# Errors Generated at Run Time are called Run Time Error : Exceptions
# Exceptions are no good for our programs :(
# It will hamper performance of OS

print("----------------")
print(">> APP Started :)")
print("----------------")
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

idx = int(input("Enter Your Lucky Number: "))
try:
    # c = 10/0
    print(">> You won a Prize of:", numbers[idx])  # After this line in try nothing will be executed :(
    print(">> This is Awesome !!")
    print(">> Please enter your Bank Details to Send Money :)")
except Exception as e:
    print(">> Some Error:", e)
finally:
    # A Block which is executed before your process dies :)
    print(">> Thanks for Playing this Game :)")
"""
except IndexError as idxErr:
     print(">> Some Error:", idxErr)
except ZeroDivisionError as zdErr:
    print(">> Some Error:", zdErr)
"""


print("----------------")
print(">> APP Finished :)")
print("----------------")


# Whenever error at run time will occur, it will crash the program
# Program Terminates Abnormally
