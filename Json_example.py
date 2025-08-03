#Name :- Mayuri Pawar
#Branch :- Computer
#Import Json File

import json

with open('data.json') as file:
    data = json.load(file)

print("Full JSON data:")
print(data)

print("Name:", data["name"])
print("Age:", data["age"])
print("Branch:", data["branch"])
print("Task:", data["task"])
