import random
dice_roll_1 = random.randint(1,6)
special = dice_roll_1 == 1 or dice_roll_1 == 6

print(f'Dice rolled: {dice_roll_1}')
print(f'Special number(1 or 6): {special}')