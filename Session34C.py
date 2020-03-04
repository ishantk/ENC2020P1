import pandas as pd


# Manual Creation of IPL Data Set
Teams = [
    "Rajasthan Royals",
    "Delhi Capitals",
    "Chennai Super Kings",
    "Delhi Capitals",
    "Mumbai Indians",
    "Kolkata Knight Riders",
    "Chennai Super Kings",
    "Deccan Chargers",
    "Kings XI Punjab",
    "Mumbai Indians",
]


Ranks = [2, 3, 4, 1, 3, 4, 1, 2, 5, 4]
Years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]

iplData = {
    "Team": Teams,
    "Rank": Ranks,
    "Year": Years
}

table = pd.DataFrame(iplData)
print(table)

print()

print("===Group By Teams===")
groupTeam = table.groupby("Team")
# print(group)
print(groupTeam.groups)

print()

print("===Group By Rank===")
groupRank = table.groupby("Rank")
print(groupRank.groups)

print()

print("===Group By Team and Rank===")
groupTeamRank = table.groupby(["Team", "Rank"])
print(groupTeamRank.groups)

print()
print("===Iterate in  Group===")
for teamName, grp in groupTeam:
    print(grp)
    # print(teamName)

print()
print("Fetch a single Group from Groups")
print(groupTeam.get_group("Delhi Capitals"))

