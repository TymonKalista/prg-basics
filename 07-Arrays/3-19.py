arr = [3,5,7,70,19,38]
x = int(input('Enter your number: '))
counter = 0
for i in range(0,len(arr)):
    if arr[i] > x:
        counter = counter + 1
print(counter)
