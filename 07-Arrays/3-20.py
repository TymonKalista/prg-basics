arr = [7,9,2,4,5,6]
even = 0
for i in range(0,len(arr)):
    if arr[i]%2 == 0:
        arr[i], arr[even] = arr[even], arr[i]
        even = even +1
print(arr)