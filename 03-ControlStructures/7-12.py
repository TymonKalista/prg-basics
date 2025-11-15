amount = int(input("Number of products you purchased: "))
price = int(input("Price of the product: "))
final_price = 0
if amount == 1 or amount == 2:
    final_price = price*amount
    print(f'Amount to pay: {final_price:g}')
else:
    final_price = price*2 + 0.75*price*(amount-2)
    print(f'Amount to pay: {final_price:g}')