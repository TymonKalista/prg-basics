def f(d):
    total = 0
    for numbers in d.values():
        total = total + numbers
    avg = total/len(d)
    i = 0
    for numbers in d.values():
        if numbers >= avg:
            i = i +1
    return i


print(f({"LO231":150,"BA787":20,"NZ15":30}))
