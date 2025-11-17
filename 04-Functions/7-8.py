def amount_to_pay(price):
    coins1 = price // 5
    price %= 5
    
    coins2 = price // 2
    price %= 2

    coins3 = price  # 0 lub 1

    return coins1 + coins2 + coins3

print(amount_to_pay(3))

