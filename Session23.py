# Java Script Object Notation | https://newsapi.org/
# JSON is a dictionary having lists/dictionary nested in it

import json

employee = {
    "eid": 101,
    "name": "John",
    "salary": 3000,
    "projects": ["CMS", "GMS"],
    "manager": {"mid": 201, "name": "Fionna"}
}

print(employee)
print(type(employee))

# Convert Dictionary into JSON
jsonData = json.dumps(employee)
# jsonData = str(employee) # ERR While De-Serialization
print(jsonData)
print(type(jsonData))

# Convert JSON into Dictionary
employeeDictionary = json.loads(jsonData)
print(employeeDictionary)
print(type(employeeDictionary))


