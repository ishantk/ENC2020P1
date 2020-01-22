"""
    Sequences in Python
    Sequence : Data with quite similar type

    Sequences listed below is also known as
    Built In Data Structures here in Python

    Why Data should be Structured?
    1. Sort
    2. Search
    3. Filter
    PS: Must be done in least possible time !!

    1. Tuple
    2. List
    3. String
    3. Set
    4. Dictionary

    Operations on Sequences:
    1. Concatenation
    2. Repetition
    3. Membership Testing
    4. Slicing
    5. Indexing

"""

students = ("John", "Jennie", "Jim", "Jack", "Joe")
print(students)
print(type(students))

# 1. Concatenation | IMMUTABLE
newStudents = students + ("Fionna", "George")

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

