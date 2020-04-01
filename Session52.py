"""
Natural Language Processing
"""

# 1. Text Pre-processing : Noise Removal
stopWords = ["is", "am", "are", "the", "...", "to", "a", "and", "we"]

def removeNoiseFromText(text):
    words = text.split()
    # print(words)
    noiseFreeWords = [word for word in words if word not in stopWords]
    print(noiseFreeWords)
    noiseFreeText = " ".join(noiseFreeWords)
    return noiseFreeText


text = "I am really happy and we are going to a vacation"
noiseFreeText = removeNoiseFromText(text)
print(noiseFreeText)

print("==================")

import re

def removeNoiseFromTextWithRegEx(text, regExpPattern):
    matches = re.finditer(regExpPattern, text)
    # print(matches) # Object -> callable_iterator

    for match in matches:
        # print(match)
        print(match.group())
        text = re.sub(match.group().strip(), '', text)

    return text

text = "Stay at Home #covid19. Stay Safe"
regExpPattern = "#[\w]*"
noiseFreeText = removeNoiseFromTextWithRegEx(text, regExpPattern)
print(noiseFreeText)

import nltk
# nltk.download()               # Just for one time downloading with GUI
# nltk.download("stopwords")    # Just for one time downloading with command


# https://www.nltk.org/book/
# 2. Text Pre-processing : Lexicon Normalization
# Stemming
from nltk.stem.porter import PorterStemmer
stem = PorterStemmer()
word = "races"
print(stem.stem(word))

# Lemmatization
from nltk.stem.wordnet import WordNetLemmatizer
lem = WordNetLemmatizer()
word = "playing"
print(lem.lemmatize(word, "v"))


# 2. Text Pre-processing : Object Standardization
dictionary = {
                        "brb": "be right back",
                        "cb": "call back",
                        "awsm": "awesome",
                        "lol": "laugh out loud"
                    }

def objectStandardization(text):
    words = text.split()
    substitutedWords = []

    for word in words:
        if word in dictionary:
            word = dictionary[word]

        substitutedWords.append(word)

    text = " ".join(substitutedWords)
    return text

text = "awsm you are. cb me soon"
print(objectStandardization(text))

# Part Of Speech (POS Tags)
from nltk import word_tokenize, pos_tag
sentence = "Stay Safe. Be At Home. Learn Well and Code Regularly."
tokens = word_tokenize(sentence)
print(tokens)
print(pos_tag(tokens))


"""
import requests
from bs4 import BeautifulSoup

url = "https://about.google/?utm_source=google-IN&utm_medium=referral&utm_campaign=hp-footer&fg=1"
response = requests.get(url)
print(response.text)
"""