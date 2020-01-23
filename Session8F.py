S1 = {1, 2, 3, 4, 5, 2}
S2 = {3, 4, 5, 6}

print(S1, type(S1))
print(S2, type(S2))

S3 = S1 | S2    # Union
S4 = S1 & S2    # Intersection
S5 = S1 - S2    # Difference

print("Union:", S3)
print("Intersection:", S4)
print("Difference:", S5)





