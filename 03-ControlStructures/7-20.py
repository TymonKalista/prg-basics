decimal = int(input('Enter decimal number: '))
binary = ""
rest = 0
while decimal > 0:
    rest = decimal%2
    rest = str(rest)
    decimal = decimal//2
    binary = rest + binary
print(binary)

