S1 = {1, 2, 3, 'A', 'B', 'C'}
S2 = {1, 'A', 'B'}

print(1 in S1)
print('X' not in S2)

print(S2.issubset(S1))
print(S1.issuperset(S2))

S3 = S1.union(S2)
S4 = S1.intersection(S2)
S5 = S1.difference(S2)

# Explore This with Real Time Use Case
# S6 = S1.symmetric_difference(S2)
