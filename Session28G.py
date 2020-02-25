import matplotlib.pyplot as plt

"""
A = [1, 2, 3, 4, 5]
B = [10, 20, 30, 40, 50]
plt.bar(A, B)
plt.show()
"""

"""
scores = {"sachin": 200, "rohit": 264, "yuvraj": 139, "virat": 183, "dhoni": 183}
plt.bar(0, scores["sachin"])
plt.bar(1, scores["rohit"])
plt.bar(2, scores["yuvraj"])
plt.bar(3, scores["virat"])
plt.bar(4, scores["dhoni"])

plt.show()
"""

scores = {"sachin": 200, "rohit": 264, "yuvraj": 139, "virat": 183, "dhoni": 183}

for i, key in enumerate(scores):
    # print(i, key, scores[key])
    # plt.bar(i, scores[key])
    plt.bar(key, scores[key])

plt.xlabel("Batsman")
plt.ylabel("Score")

plt.title("Top 5 Indian Cricketers")

plt.show()
