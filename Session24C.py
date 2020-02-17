# Regular Expressions
import re

quote = "Search the Candle rather than cursing the darkness"
# result = re.match("Search", quote)# 0-6
# result = re.match("Candle", quote)  # None
# print(result, type(result))

# result = re.search("the", quote)

result = re.findall("the", quote)
print(result)

print("------------")

# data = re.split("the", quote)
# print(data)

# substitute
data = re.sub("the", "a", quote)
print(data)