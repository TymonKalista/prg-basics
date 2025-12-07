price_list = {
   'T-shirt': 19.99,
   'Jeans': 49.99,
   'Jacket': 89.99,
   'Sneakers': 59.99,
   'Hat': 15.99
}
print('Before discount')
for item, price in price_list.items():
    print(f'{item} costs {price}')
total1 = 0
for price in price_list.values():
    total1 = total1 + price
    total1 = round(total1, 2)
print(f'Everything costs {total1}')

print('After discount')
for item, price in price_list.items():
    price = price*0.9
    price = round(price, 2)
    print(f'{item} costs {price}')
total2 = 0
for price in price_list.values():
    price = price*0.9
    price = round(price, 2)
    total2 = total2 + price
total2 = round(total2, 2)
print(total2)

    