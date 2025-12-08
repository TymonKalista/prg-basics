import json

with open('dogs.json','r') as file:
    data = json.load(file)

for dog in data:
    if dog['age'] < 5:
        for key, value in dog.items():
            print(key,':',value)