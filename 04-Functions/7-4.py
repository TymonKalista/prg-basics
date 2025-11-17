import letter_calculaor

txt = (input('Enter your text: '))
letter = (input('Enter your letter: '))
amount = letter_calculaor.letter_counter(txt,letter)
print(f'The number of letter {letter} is: {amount}')