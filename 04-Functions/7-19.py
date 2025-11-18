def f(number):
    sum_of_digits = 0
    number = str(number)
    amount_of_1 = number.count('1')
    amount_of_2 = number.count('2')
    amount_of_3 = number.count('3')
    amount_of_4 = number.count('4')
    amount_of_5 = number.count('5')
    amount_of_6 = number.count('6')
    amount_of_7 = number.count('7')
    amount_of_8 = number.count('8')
    amount_of_9 = number.count('9')
    if amount_of_1 >1:
        sum_of_digits = sum_of_digits + amount_of_1
    else:
        sum_of_digits = sum_of_digits
    if amount_of_2 >1:
        sum_of_digits = sum_of_digits + amount_of_2*2
    else:
        sum_of_digits = sum_of_digits
    if amount_of_3 >1:
        sum_of_digits = sum_of_digits + amount_of_3*3
    else:
        sum_of_digits = sum_of_digits
    if amount_of_4 >1:
        sum_of_digits = sum_of_digits + amount_of_4*4
    else:
        sum_of_digits = sum_of_digits
    if amount_of_5 >1:
        sum_of_digits = sum_of_digits + amount_of_5*5
    else:
        sum_of_digits = sum_of_digits
    if amount_of_6 >1:
        sum_of_digits = sum_of_digits + amount_of_6*6
    else:
        sum_of_digits = sum_of_digits
    if amount_of_7 >1:
        sum_of_digits = sum_of_digits + amount_of_7*7
    else:
        sum_of_digits = sum_of_digits
    if amount_of_8 >1:
        sum_of_digits = sum_of_digits + amount_of_8*8
    else:
        sum_of_digits = sum_of_digits
    if amount_of_9 >1:
        sum_of_digits = sum_of_digits + amount_of_9*9
    else:
        sum_of_digits = sum_of_digits
    return sum_of_digits
print(f(1027))