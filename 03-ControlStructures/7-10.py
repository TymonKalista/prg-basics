age = int(input("Enter dog's age in human years: "))
dogage = 0
if age == 1:
    dogage = 10.5
elif age == 2:
    dogage = 21
else:
    dogage = 21 + (age-2)*4



print(f"The dog's age in dog's years is: {dogage} ")