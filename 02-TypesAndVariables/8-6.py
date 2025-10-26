distance = int(input('Enter distance in km: '))
fuel_price = float(input('Enter fuel price per liter: '))
fuel_consumption = float(input('Enter fuel consumpiton in liters per 100 km: '))

total_cost = ((distance*fuel_consumption)/100)*fuel_price
print(f'Total cost is: {total_cost}')
