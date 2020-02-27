import requests
from bs4 import BeautifulSoup


url = "https://www.espncricinfo.com/table/series/8048/season/2019/ipl"
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
        iplTeams2019Data[j].append(float(tag.text.strip()))
    except Exception as e:
        iplTeams2019Data[j].append(tag.text.strip())

    i += 1

    if i % 9 == 0:
        j += 1
        print("~~~~~~~~")


print(iplTeams2019Names)
print(iplTeams2019Data)
