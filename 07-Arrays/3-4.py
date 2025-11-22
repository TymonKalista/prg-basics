arr = [-15, 8, -31, 47, -2, 19]



maximum = arr[0]
minimum = arr[0]


for num in arr:
    if num > maximum:
        maximum = num
    if num < minimum:
        minimum = num

print("Maximum:", maximum)
print("Minimum:", minimum)