import matplotlib.pyplot as plt
from sklearn import datasets

# Know the DataSet : Images DataSet :)

digits = datasets.load_digits()
print(digits)
print(type(digits))     #Bunch

print("------IMAGES-------")
# Images are printed as numpy array
# print(digits.images)
print(digits['images'])     #ndarray
print(len(digits['images']))

print("------TARGET-------")
# Labels for Different Digit Images
# print(digits.target)
print(digits['target'])
print(len(digits['target']))

print("====Using 1st 2 Images in DataSet====")

print(">> Printing 0th Image Data")
print(digits['images'][0])
print(digits['images'][0].shape)
print(digits['target'][0])

print(">> Printing 1st Image Data")
print(digits['images'][1])
print(digits['images'][1].shape)
print(digits['target'][1])

# Plotting Images on Matplotlib
"""
plt.subplot(2, 4, 1)
plt.imshow(digits['images'][0], cmap=plt.cm.gray_r)

plt.subplot(2, 4, 2)
plt.imshow(digits['images'][1], cmap=plt.cm.gray_r)

plt.subplot(2, 4, 3)
plt.imshow(digits['images'][2], cmap=plt.cm.gray_r)

plt.subplot(2, 4, 4)
plt.imshow(digits['images'][3], cmap=plt.cm.gray_r)

plt.subplot(2, 4, 5)
plt.imshow(digits['images'][4], cmap=plt.cm.gray_r)

plt.show()
"""

pos = 1
for i in range(0, 8):
    plt.subplot(2, 4, pos)
    # plt.imshow(digits['images'][i])
    plt.imshow(digits['images'][i], cmap=plt.cm.gray_r)
    pos += 1

plt.show()

# HW: Explore how to show image in seaborn with subplotting :)