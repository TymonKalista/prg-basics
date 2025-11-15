hours = int(input("How many hours did you stay: "))
if hours > 6:
    print("The fee is 20 PLN")
elif hours > 3:
    print("The fee is 15 PLN")
else:
    print("The fee is 5 PLN")