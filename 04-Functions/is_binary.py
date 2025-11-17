def is_binary(number):
    number = str(number)
    for i in range(len(number)):
        if number[i] != '0' and number[i] != '1':
            return False
    return True
        
print(is_binary('10a00'))