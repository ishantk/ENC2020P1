import matplotlib.pyplot as plt

languages = ["Python", "Java", "C++", "Dart", "JavaScript"]
jobs = [80, 70, 55, 60, 19]

plt.pie(jobs, labels=languages)
plt.legend()
plt.show()