store = {
'Laptop': 15,
'Desktop PC': 10,
'Monitor': 25,
'Keyboard': 50,
'Mouse': 60,
'External Hard Drive': 30,
'Printer': 12,
'Router': 20,
'USB Flash Drive': 100,
'Graphics Card': 8
}
for product, quantity in store.items():
    print(f'There is {quantity} {product} in store')
total = 0
for quantity in store.values():
    total = total + quantity
print(total)

