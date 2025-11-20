def f(x,y):
    sum_of_everything = 0
    for i in range(x,y+1):
        if i%2 == 0 and i%3==0 and i%4 !=0:
            sum_of_everything = sum_of_everything + i
        else:
            sum_of_everything = sum_of_everything
    return sum_of_everything
print(f(1,20))