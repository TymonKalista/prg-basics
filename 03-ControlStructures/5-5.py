###
# Sums numbers entered by user
#
total_sum = 0

x=0

while True:
    number = int(input("Enter a number (0 to stop): "))
    
    if number == 0:
        break  # Exit the loop when 0 is entered
    total_sum += number
    x =  x + 1
arithmeticmean = total_sum/x


print(f"The total sum of the numbers is: {total_sum}")
print(f"The arithmeic mean of the numbers is: {arithmeticmean}")

