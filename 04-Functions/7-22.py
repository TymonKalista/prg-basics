def f(name):
    name = str(name)
    new_name = name[0]
    i = 0
    while i < len(name):
        if name[i] == ' ':
            new_name = new_name + name[i+1]
            i = i +1
        else:
            i = i +1    
    return new_name


print(f("Python"))
