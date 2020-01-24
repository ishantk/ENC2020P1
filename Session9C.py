"""
    insertionSort(data)

    Functions or Procedure or Routine or Method
    1. Name
    2. Inputs (May or May Not) / Parameters / Arguments
    3. return (in the end) if you have not given it it is by default return
       act as acknowledgement
    4. Definition
        What function should do !!

        Execution happens in a sequence i.e. line by line

    Loops:
        Loops will execute a sequence from 0 to n-1 or any choice of range of yours
        do the same thing again and again

    Function:
        Group of statements / logic which has to be executed
        we can give several different inputs to get the logic work
        and generate results accordingly

        My Program is MODULARIZED
"""

"""
paneer = 200
parantha = 20
bill1 = paneer + parantha
print(">> bill1 is:", bill1)

dal = 100
bill2 = dal + parantha
print(">> bill2 is:", bill2)

dosa = 80
idli = 30
bill3 = dosa + idli
print(">> bill3 is:", bill3)
"""

paneer = 200
parantha = 20
dal = 100
dosa = 80
idli = 30

# def add(n1, n2):

def add(n1=0, n2=0):
# def add(n1, n2=0):
# def add(n1=0, n2):  # error
    sum = n1 + n2
    return sum

# def add(n1=0, n2, n3=0): err
# def add(n1, n2=0, n3=0): ok


print(">> bill1 is:", add(paneer, parantha))
print(">> bill2 is:", add(dal, parantha))
print(">> bill3 is:", add(dosa, idli))
print(">> bill4 is:", add(dosa, parantha))
print(">> bill5 is:", add(dosa, dal))
print(">> bill6 is:", add(10))

print(">> bill7 is:", add(n1=dosa, n2=dal))
print(">> bill8 is:", add(n2=dosa, n1=dal))

print(">> bill9 is:", add(n2=10))




