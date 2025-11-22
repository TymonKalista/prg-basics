arr = ['Genowefa', 'Onufry', 'Celestyna', 'Alojzy', 'Pankracy']
print('Names: ', end="")
print(", ".join(arr))
longest = arr[0]
for name in arr:
    if len(name) > len(longest):
        longest = name

print("Longest name:", longest)



