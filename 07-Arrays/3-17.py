tuple = (50,20,40,50,30,50)
print('Tuple: ', end=" ")
print(", ".join((str(x) for x in tuple)))
x = 50
print('Value: ', x)
y = tuple.count(x)
print('Number of occurences: ', y)