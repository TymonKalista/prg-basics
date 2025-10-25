import random

computer = random.randint(1,6)

you = int(input('I guess nr: '))

winning = computer == you
print(f'You won: {winning}')