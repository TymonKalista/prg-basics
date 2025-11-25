def f(expression):
    total = int(expression[0])   # start with the first digit
    i = 1

    while i < len(expression):
        op = expression[i]            # '+' or '-'
        num = int(expression[i + 1])  # next digit

        if op == '+':
            total += num
        else:
            total -= num

        i += 2  # move to the next operator

    return total
