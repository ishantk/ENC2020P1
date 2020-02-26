import requests
from bs4 import BeautifulSoup

url = "https://twitter.com/dna"
response = requests.get(url)

# We have Extracted HTML Response from the URL
# print(response.text)

# HTML PARSING
# We need to Extract only meaningful data from HTML Response
# Beautiful Soup shall be used to do HTML Parsing

soup = BeautifulSoup(response.text, "html.parser")
# print(soup)
print(soup.prettify())

print("----TITLE-----")
print(soup.title.text)

# print("----CHILDREN-----")
# children = soup.children
# for child in children:
#     print(child)
#     print("^^^^^^^^^^^")

# print("----P Tags-----")
# pTags = soup.find_all("p")
# for tag in pTags:
#     print(tag)
#     print("^^^^^^^^^^^")

print("----Div Tags-----")

# divTags = soup.find_all("div")
divTags = soup.find_all("div", class_="js-tweet-text-container")
for tag in divTags:
    # print(tag)
    print(tag.text)
    print("^^^^^^^^^^^")

