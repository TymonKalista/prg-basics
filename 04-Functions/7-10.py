def neg_even_numbers(x,y):
    counter = 0
    for i in range(x,y):
        if i%2 == 0 and i < 0:
            counter = counter + 1
        else:
            counter = counter
    return counter
print(neg_even_numbers(-18,-1))