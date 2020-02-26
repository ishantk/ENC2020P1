import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/india/top-rated-indian-movies/"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
# print(soup.prettify())

tags = soup.find_all("td", class_="titleColumn")

movies = []
years = []

for tag in tags:
    # print(tag.text)
    movieTitle = tag.text.strip()
    movies.append(movieTitle)
    # print("----------")

for movie in movies:
    print(movie)
    print("~~~~~~~~~~~")


# Plot Histogram :)