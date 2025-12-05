countries = [
{"name":"Poland", "population":38000000},
{"name":"USA", "population":200000000},
{"name":"France", "population":80000000},
{"name":"Monako", "population":5000},
{"name":"Vatican", "population":1}
]


print("COUNTRY  POPULATION")

# Loop through each dictionary in the list and print country and population
for country in countries:
    print(f"{country['name']:} {country['population']}")