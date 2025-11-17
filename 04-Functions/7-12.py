def asterisks(n):
    if n == 1:
        return('*')
    if n > 1:
        return('*/'*(n-1))+('*')
print(asterisks(4))