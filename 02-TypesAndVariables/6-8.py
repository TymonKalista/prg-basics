first = input('Enter first letter: ')
last = input('Enter last letter: ')
first_letter_code = ord(first)
last_letter_code = ord(last)
if first_letter_code != last_letter_code: 
    number_of_letters = last_letter_code - first_letter_code -1
else:
    number_of_letters = 0
print(f'Between {first} and {last} is {number_of_letters} letters')