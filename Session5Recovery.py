# Single Value Containers
city1Population = 10212
city2Population = 20212
city3Population = 31112
city4Population = 64312
city5Population = 24578
city6Population = 54578

stat1Population = city1Population + city2Population + city3Population + city4Population + city5Population + city6Population
print(">> stat1Population:", stat1Population)

# Challenge:
# When we have lot of data, Single Value Containers is not a good choice

# Solution:
# We should use Multi Value Container

# Data is Indexed :  0       1     2       3     4      5
statePopulation = [10212, 20212, 31112, 64312, 24578, 54578]

# 0 inclusive, 5 exclusive -> 0 to 4
total = 0
for i in range(0, len(statePopulation)):
    total += statePopulation[i]

print(">> total with for :", total)

i = 0
total = 0
while i < len(statePopulation):
    total += statePopulation[i]
    i += 1

print(">> total with while :", total)


# Enhanced i.e. For-Each Loop | We don't manage indexes :)

total = 0
for population in statePopulation:
    total += population

print(">> total with for-each :", total)