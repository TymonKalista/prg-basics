import matplotlib.pyplot as plt

medals = [
    {"country": "Denmark", "gold": 2, "silver": 4, "bronze": 6},
    {"country": "Finland", "gold": 5, "silver": 0, "bronze": 4},
    {"country": "USA", "gold": 12, "silver": 5, "bronze": 11},
    {"country": "Peru", "gold": 0, "silver": 1, "bronze": 7}
]

# Names of countries
countries = list(map(lambda x: x["country"], medals))

# Total medals for each country
total_medals = list(
    map(lambda x: x["gold"] + x["silver"] + x["bronze"], medals)
)

# Create bar chart
plt.bar(countries, total_medals)

# Chart details
plt.title("Total Number of Medals Won by Each Country")
plt.xlabel("Country")
plt.ylabel("Number of Medals")

plt.show()
