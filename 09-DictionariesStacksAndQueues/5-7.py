hotels_in_Krakow = [
   {"name":"Sky","price":320.00},
   {"name":"Metropol","price":480.00},
   {"name":"New Port","price":420.00},
   {"name":"Aparthotel","price":390.00}
]
hotels_in_Sopot = [
   {"name":"Focus","price":510.00},
   {"name":"Aqua","price":345.00},
   {"name":"La Boutique","price":390.00},
   {"name":"Marina","price":410.00}
]
avg1 = 0
for hotel in hotels_in_Krakow:
    avg1 = avg1 + int(hotel['price'])

avg1 = avg1/len(hotels_in_Krakow)
print(avg1)

avg2 = 0
for hotel in hotels_in_Sopot:
    avg2 = avg2 + int(hotel['price'])

avg2 = avg2/len(hotels_in_Krakow)
print(avg2)

if avg1>avg2:
    cheaper_in = 'Sopot'
if avg2> avg1:
    cheaper_in = 'Krakow'













print("Hotels in Krakow:")
for hotel in hotels_in_Krakow:
    print(f"{hotel['name']}")
print(f'Average hotel price in Krakow: {avg2}')
print("Hotels in Sopot:")
for hotel in hotels_in_Sopot:
    print(f"{hotel['name']}")
print(f'Average hotel price in Sopot: {avg2}')
print(f'Cheaper hotels in: {cheaper_in}')