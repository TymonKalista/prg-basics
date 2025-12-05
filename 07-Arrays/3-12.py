arr  = [2, 3, 2, 5, 8, 1, 9, 8]

print('Unique elements: ', end=' ')
for i in range(0,len(arr)):
    x = arr[i] 
    if arr.count(x) == 1:
        print(arr[i],end=" ")