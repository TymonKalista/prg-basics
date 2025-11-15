age = int(input("How old are you: "))
if age >= 65:
    print("Senior")
elif age >= 20:
    print("Adult")
elif age >= 13:
    print("Teen")
else:
    print("Child")