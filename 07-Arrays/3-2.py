arr = [ 34,7,19,4,22,8]
i = 0
counter = 0
while i<len(arr):
    if arr[i]%2 ==0:
        counter = counter + 1
        i = i+1
    else:
        i = i+1



print(counter)

