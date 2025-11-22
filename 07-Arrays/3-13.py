def occurs(number, array):
    for i in range(0,len(array)):
        if number == array[i]:
            return True
    return False
arr = [15, 38, 7, 23, 14]
number = int(input('Enter number: '))
if occurs(number,arr) == True:
    print(f'Number {number} appears in the arrey')
else:
    print(f'Number {number} doesnt appears in the arrey')

