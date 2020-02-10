import os

cwd = os.getcwd()
print(cwd)
print(os.name)
print(os.uname())
print(os.getlogin())
print(os.getppid())

pathToDirectory = "/Users/ishantkumar/Downloads"
pathToFile = "/Users/ishantkumar/Downloads/MyApp.java"

print(">> Is Downloads Existing:", os.path.isdir(pathToDirectory))
print(">> Is MyApp.java Existing:", os.path.isfile(pathToFile))

path = "/Users/ishantkumar/Downloads/MyPyProjects"
print(">> Is MyPyProjects Existing:", os.path.isdir(path))

# if os.path.isdir(path) == False:
#     os.mkdir(path)
#     print(">> Directory Created")

# Use Carefully
# os.rmdir(path)


files = os.walk("/Users/ishantkumar/Downloads")
# print(files)
# print(type(files))

allFiles = list(files)

for file in allFiles:
    print(file)

# Assignment:  Write File Explorer App :)
# DOCUMENTS [dCount] | IMAGES [iCount] | AUDIOS [aCount] | VIDEOS [vCount]