# Built In APIs i.e. Functions

# Strings are IMMUTABLE
# Manipulation operations will create a new String in memory
# Old String will not be modified

name = "Fionna Flynn"
print(">> name is:", name)
newName = name.upper()
print(">> name now is:", name)
print(">> newName is:", newName)

authorName = "john watson"
print(authorName, hex(id(authorName)))
# We are creating a new string and referring it in our old ref var
# newAuthorName = authorName.capitalize()
# print(">> newAuthorName is:", newAuthorName)
# print(">> authorName is:", authorName)
authorName = authorName.capitalize()
print(authorName, hex(id(authorName)))

names = "John, Jennie, Jim, John, Jack, Joe"
print(names[0])
print(names[len(names)-1])
# idx = names.index("o")
idx = names.index("Jennie")
print(idx)

newNames = names.replace('J', 'K')
print(names)
print(newNames)

# num = names.count("J", 0, len(names))
num = names.count("John", 0, len(names))
print(">> num is:", num)

# HW:
quotes = """Work Hard, Get Luckier
Search the Candle, rather than cursing the darkness
"""

def count(data, word, start, end):
    c = 0
    j = 0
    for i in range(start, end):
        print(data[i] == word[j])

    return c

print(">> the occurs: ", count(quotes, "the", 0, len(quotes)))