CORRECT_PIN = "0805"
attempts = 0

while attempts < 3:
    entered = input("Enter the PIN code: ")
    if entered == CORRECT_PIN:
        print("Correct PIN. Access granted.")
        break
    else:
        print("Incorrect...")
        attempts += 1

if attempts == 3:
    print("Sorry, your payment card has been blocked.")
    
