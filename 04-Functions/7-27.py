def f(product_code):
    x = product_code[0:3]
    x = int(x)
    y = product_code[-1]
    y = int(y)
    if x%7 == y:
        return True
    elif x%7 != y:
        return False

print(f("1082"))
