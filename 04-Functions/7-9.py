def counting_digits(number, even):
    if even == True:
        number=str(number)
        y = number.count('2')
        z = number.count('4')
        u = number.count('6')
        w = number.count('8')
        return y*2 + z*4 + u*6 + w*8
    if even == False:
        number=str(number)
        y = number.count('1')
        z = number.count('3')
        u = number.count('5')
        w = number.count('7')
        x = number.count('9')
        return y*1 + z*3 + u*5 + w*7 + x*9
print(counting_digits(20576,False))