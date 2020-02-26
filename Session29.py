import matplotlib.pyplot as plt

# ages = [21, 22, 23, 4, 5, 6, 77, 8, 21, 10, 31, 32, 66, 54, 90]
# bins = 10
# plt.hist(ages, bins)
# plt.show()

# languages = ["Python", "Java", "C++", "Dart", "JavaScript"]
# jobs = [70, 80, 88, 12, 90]
# # plt.bar(languages, jobs)
# plt.barh(languages, jobs, align="center", alpha=0.3)   # Plot Horizontally
# plt.show()

years = [2015, 2016, 2017, 2018, 2019]
years1 = [2015+0.35, 2016+0.35, 2017+0.35, 2018+0.35, 2019+0.35]
jobsInJava = [90, 80, 67, 54, 22]
jobsInPython = [80, 70, 55, 60, 19]

plt.bar(years, jobsInJava, 0.30, color='b', label='Java')
plt.bar(years1, jobsInPython, 0.30, color='g', label='Python')

plt.legend()
plt.show()
