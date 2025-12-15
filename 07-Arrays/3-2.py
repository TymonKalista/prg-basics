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

arr1 = [15, 8, 31, 47, 2, 19]

print("existed array:", *arr1)

print("reverse array:", end=" ")
for i in range(len(arr1)-1, -1, -1):
    print(arr1[i], end=" ")

