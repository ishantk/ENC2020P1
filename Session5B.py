# Iterations or Loops

num = int(input(">> Enter a Number: "))
i = 1

while i <= 10:
    print(num, "", i, "'s are", (num*i))
    # i += 1     # i = i + 1
    i += 2

print(">>>>><<<<<")

# for i in range(1, 11):
for i in range(1, 11, 2):
    print(num, "", i, "'s are", (num * i))

print(">>>>><<<<<")

for i in range(10, 0, -1):
    print(num, "", i, "'s are", (num * i))

