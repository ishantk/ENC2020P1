"""

    Types Of Recursion
    1. Direct Recursion
    2. Indirect Recusrion
    3. Tail Recursion

"""

def fun():

    fun()       # Direct Recursion


def fun1():

    fun2();     # InDirect Recursion

def fun2():

    fun1()


def tailRec():
    #...
    #...

    tailRec()    # Last Statement is execution of function



# HW: Implement Insertion Sort with Recursion


