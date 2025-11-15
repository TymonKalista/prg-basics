amount = int(input('Enter the emount in PLN: '))
AMOUNT_OF_5pln = 0
AMOUNT_OF_2pln = 0
AMOUNT_OF_1pln = 0
while amount / 5 > 1:
    AMOUNT_OF_5pln = amount // 5
    amount = amount%5
while amount / 2 > 1:
    AMOUNT_OF_2pln = amount // 2
    amount = amount%2
if amount == 1:
    AMOUNT_OF_1pln = 1
else:
    AMOUNT_OF_1pln = 0
print(f'5 PLN coins: {AMOUNT_OF_5pln}')
print(f'3 PLN coins: {AMOUNT_OF_2pln}')
print(f'1 PLN coins: {AMOUNT_OF_1pln}')


