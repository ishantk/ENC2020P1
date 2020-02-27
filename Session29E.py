import requests
from bs4 import BeautifulSoup

import matplotlib.pyplot as plt

url = "https://www.imdb.com/india/top-rated-indian-movies/"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
# print(soup.prettify())

tags = soup.find_all("td", class_="titleColumn")
ratingTags = soup.find_all("td", class_="ratingColumn imdbRating")

movies = []
years = []
ratings = []

for tag in tags:
    # print(tag.text)
    movieTitle = tag.text.strip()
    movieYear = int(movieTitle[-5:-1])
    movies.append(movieTitle)
    years.append(movieYear)


for tag in ratingTags:
    rating = float(tag.text.strip())
    ratings.append(rating)


print(movies)
print(len(movies))

print(years)
print(len(years))

print(ratings)
print(len(ratings))

plt.barh(years, ratings)
plt.show()