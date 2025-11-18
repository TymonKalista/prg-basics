def f(number1, number2, number3):
    if number1 > number2 and number1 > number3 and number2>number3:
        return number1 - number3
    if number1 > number2 and number1 > number3 and number3>number2:
        return number1 - number2
    if number2 > number1 and number2 > number3 and number1>number3:
        return number2 - number3
    if number2 > number1 and number2 > number3 and number3>number1:
        return number2 - number1
    if number3 > number1 and number3 > number2 and number1>number2:
        return number3 - number2
    if number2 > number1 and number2 > number3 and number2>number1:
        return number3 - number1
    
print(f(7,4,9))
print(f(2,12,8))