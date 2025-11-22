tuple = (10,20,30,40,50)

    
print('Tuple: ', end=" ")
print(", ".join((str(x) for x in tuple)))
print('reverse order: ', end=" ")
for i in range(1,len(tuple)):
    print(tuple[-i], end=" ")
print(tuple[0])