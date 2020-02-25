import pandas as pd

nums1 = [10, 20, 30, 40, 50]
nums2 = [11, 22, 33, 44, 55]

emp1 = {"name": "John", "age": 22, "salary": 30000}
emp2 = {"name": "Fionna", "age": 24, "salary": 45000}
emp3 = {"name": "Dave", "age": 26, "salary": 54000}
emp4 = {"name": "Kia", "age": 28, "salary": 59000, "email": "kia@example.com"}

frame1 = pd.DataFrame([nums1, nums2])
frame2 = pd.DataFrame([emp1, emp2, emp3, emp4])

print(frame1)
print("-----")
print(frame2)

print("--Access Data in DataFrame--")

# Fetch data Column Wise :)
print(frame1[0])
print(frame2["name"])

print(frame1[1][1])
print(frame2["salary"][2])

print("--Apply Slicing on Data in DataFrame--")
print(frame1[0:1])
# print(frame1[0:])

print(frame2[0:2])

print("--Delete Data in DataFrame--")

# del frame1[0]
# print(frame1)

# Deleting a Row or Column
# drop -> either axis=0 (ROW) or axis=1(Column)
# This operation is IMMUTABLE i.e. will generate a new DataDrame :)
print("--drop--")
frame3 = frame1.drop(0, axis=0)
print(frame1) # No Change    :(
print(frame3) # With Changes :)

# Deleting a Value in DataFrame


print("--Update Data in DataFrame--")

# frame1[1][1] = 111
frame1[1] = 111
print(frame1)