import re

# quote = r"Work Hard and Get Luckier" -> raw string to ignore special characters (eg: \n)
quote = "Work Hard and Get Luckier"

result = re.findall(".", quote)
print(result)
# print(type(result))


print("===========")

result = re.findall("\w", quote)
print(result)

print("===========")

result = re.findall("\w*", quote)
print(result)

print("===========")

result = re.findall("\w+", quote)
print(result)


# PS: https://www.vogella.com/tutorials/JavaRegularExpressions/article.html
# Validation of Inputs by User with Regular Expression
userInput = "PB10AB1234"
email = "john@example.com"
