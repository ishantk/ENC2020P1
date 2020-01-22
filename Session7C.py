"""

    1. Check all operations on Set |
    2. Check Concatenation Immutable property on Set | NO
    3. Try Concatenating List and Tuple into Set | NO
    4. Repetition + Indexing + Slicing | No
    4. See if for loop with range works set
    5. See if for-each loop works with set

"""

students = {"John", "Jennie", "Jim", "John", "Jack", "Joe"}
print(students)
print(type(students))

# PS: In set data will be unordered due to Hashing
#     Data will be UNIQUE



# 3. Membership Testing
print("John" in students)
print("Dave" not in students)

# Enhanced Version of For Loop -> For-Each Loop
for student in students:
    print(student)




