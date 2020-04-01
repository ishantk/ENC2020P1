import requests
from bs4 import BeautifulSoup
import nltk
from nltk.corpus import stopwords


url = "https://about.google/?utm_source=google-IN&utm_medium=referral&utm_campaign=hp-footer&fg=1"
response = requests.get(url)
print(response.text)

soup = BeautifulSoup(response.text, "html.parser")
# Some Parsing in case needed
text = soup.text

# Tokenization
tokens = [token for token in text.split()]
print(tokens)


# Text PreProcessing
tokensWithoutStopWords = tokens[:]

# Removing StopWords from Tokens
for token in tokens:
    if token in stopwords.words("english"):
        tokensWithoutStopWords.remove(token)

# Applying NLTK
frequency = nltk.FreqDist(tokensWithoutStopWords)
frequency.plot(20)
