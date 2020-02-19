"""
    n-Queen Problem :)
    1. Create a ChessBoard in Program
        Take Input form User (2X2, 4X4, 8X8, 16X16 ...)

    1 0 1 0 1 0 1 0
    0 1 0 1 0 1 0 1
    1 0 1 0 1 0 1 0
    0 1 0 1 0 1 0 1
    1 0 1 0 1 0 1 0
    0 1 0 1 0 1 0 1
    1 0 1 0 1 0 1 0
    0 1 0 1 0 1 0 1

    2. Take Input from User to place n-queens

    1 0 1 9 1 0 1 0
    0 1 0 1 0 1 0 1
    1 0 1 0 1 0 1 0
    0 1 0 1 0 1 0 1
    1 0 1 0 1 0 1 0
    0 1 0 1 0 1 0 1
    1 0 1 0 1 0 1 9
    0 1 0 1 0 1 0 1

    > 1. No second Queen should be in the same Column
    > 2. No second Queen should be in the same Row
    > 3. No second Queen should be in the same Diagonal

"""

import numpy as np
chessboard = np.zeros((8, 8), dtype=int)
print(chessboard)

print("=========")

# Slicing and Substitution
chessboard[1::2, 0::2] = 1
chessboard[0::2, 1::2] = 1

print(chessboard)

print("=========")

# Start from 1 and go till end | Row Filter
# Filter :)
# print(chessboard[1::2])


def rowCheck():
    pass

def columnCheck():
    pass

def diagonalCheck():
    pass
    
indexes = []

for i in range(0, len(chessboard)):
    print("Where Would You like to Place Your Queen #{} eg:1,2".format(i+1))
    i = int(input("Enter Row Position: "))
    j = int(input("Enter Column Position: "))

    # Boundary Conditions
    if (i>=0 and i<=7) and (j>=0 and j<=7):
        chessboard[i][j] = 9
    else:
        print(">> Please Enter Correct Position :)")

    indexes.append([i, j])

print("*****Final Chessboard*****")
print(chessboard)
print("*****Final Queens*****")
print(indexes)


