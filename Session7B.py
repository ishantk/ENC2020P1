students = ["John", "Jennie", "Jim", "Jack", "Joe"]
print(students, hex(id(students)))

newStudents = students + ["Fionna", "George"]
# print(students + ["Fionna", "George"])

print(newStudents, hex(id(newStudents)))

students = students + ["Fionna", "George"]
# Operation -> Concatenation in the same list
print(students, hex(id(students)))




