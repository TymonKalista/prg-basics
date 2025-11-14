###
# Calculates the sum of the digits in a number
#


def sum_digits(any_number):
    number = abs(any_number)
    digit_sum = 0
    for char in str(number):
        digit_sum = digit_sum + int(char)
    return digit_sum

any_number = int(input('Enter integer number: '))

print(f'The sum of the digits in the number {any_number} is {sum_digits(any_number)}')