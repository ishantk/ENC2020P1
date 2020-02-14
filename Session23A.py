import requests
# import requests as rq

import json

# url = "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=?"
url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=?"
response = requests.get(url)
print(response, type(response))
print("~~~~~~~~~~~~~~~~~~~~~")
jsonData = response.text
print(jsonData)
print("~~~~~~~~~~~~~~~~~~~~~")

newsDictionary = json.loads(jsonData)
print(newsDictionary)
print(type(newsDictionary))

print("~~~~~~~~~JSON PARSING~~~~~~~~~")

print(">> TOTAL NEWS:", newsDictionary["totalResults"])

articles = newsDictionary["articles"]
print(len(articles))

for article in articles:
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(article["author"])
    print(article["title"])
    print(article["description"])
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print()


# Assignments : Explore JSON Parsing
# https://developers.olacabs.com/docs/ride-estimate
# https://openweathermap.org/api

