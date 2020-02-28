import requests
from bs4 import BeautifulSoup

year = 2019
url = "https://www.espncricinfo.com/table/series/8048/season/{}/ipl".format(year)
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

teamNameTags = soup.find_all("span", class_="team-names")
teamDataTags = soup.find_all("td", class_="")

iplTeams2019Names = []
iplTeams2019Data = []

for tag in teamNameTags:
    print(tag.text.strip())
    iplTeams2019Names.append(tag.text.strip())
    iplTeams2019Data.append([])


i = 0
j = 0
for tag in teamDataTags:

    print(tag.text.strip())
    try:
        iplTeams2019Data[j].append(int(tag.text.strip()))
    except Exception as e:
        iplTeams2019Data[j].append(tag.text.strip())

    i += 1

    if i % 9 == 0:
        j += 1
        print("~~~~~~~~")


print(iplTeams2019Names)
print(iplTeams2019Data)

class Team:
    def __init__(self, teamName, matches, won, lost, tied, abandoned, points, netRunRate, forScore, againstScore):
        self.teamName = teamName
        self.matches = matches
        self.won = won
        self.lost = lost
        self.tied = tied
        self.abandoned = abandoned
        self.points = points
        self.netRunRate = netRunRate
        self.forScore = forScore
        self.againstScore = againstScore

    def __str__(self):
        return "{},{},{},{},{},{},{},{},{},{},{}\n".format(year,self.teamName, self.matches, self.won, self.lost, self.tied, self.abandoned, self.points, self.netRunRate, self.forScore, self.againstScore)

teams = []
for i in range(0, len(iplTeams2019Names)):
    team = Team(iplTeams2019Names[i], iplTeams2019Data[i][0], iplTeams2019Data[i][1], iplTeams2019Data[i][2], iplTeams2019Data[i][3], iplTeams2019Data[i][4], iplTeams2019Data[i][5], iplTeams2019Data[i][6], iplTeams2019Data[i][7], iplTeams2019Data[i][8])
    teams.append(team)


file = open("IPL-TEAMS-2019.csv", "a")

for team in teams:
    print(team)
    data = str(team)
    file.write(data)


print("--CSV FILE GENERATED--")