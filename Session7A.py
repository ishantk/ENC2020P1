"""

    1. Check all operations on List | YES
    2. Check Concatenation Immutable property on list | YES
    3. Try Concatenating List and Tuple | NO

"""

students = ["John", "Jennie", "Jim", "Jack", "Joe"]
print(students)
print(type(students))

# 1. Concatenation | IMMUTABLE
newStudents = students + ["Fionna", "George"]

print(newStudents)
print(students)

print()

# 2. Repetition
print(students*3)

print()

# 3. Membership Testing
print("John" in students)
print("Dave" not in students)

# 4. Indexing
print(students[0])
print(students[len(students)-1])

# 5. Slicing
print(students[0:2])    # 0 is inclusive and 2 in exclusive
print(students[1:4])
filteredStudents = students[1:4]
print(filteredStudents)

print()

# Basic For Loop
# for i in range(0, len(students)):
#     print(students[i])

# Enhanced Version of For Loop -> For-Each Loop
for student in students:
    print(student)




