dic = {"Krakow":7,"Warszawa":-2,"Sopot":4,"Koszalin":-1,"Opole":3}
positive_cities = list(filter(lambda item: item[1] > 0, dic.items()))

print("Cities with positive temperatures:", end=" ")
for city, temp in positive_cities:
    print(city, end=" ")