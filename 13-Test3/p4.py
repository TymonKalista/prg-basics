def f(fnc, res):
    min = 100
    max = 0
    
    for i in res:
        if fnc(i):
            if i > max:
                max = i
            if i<min:
                min = i
    return (max - min)






res = [95,90,20,50,70]
fnc1 = lambda x: x>50
print(f(fnc1,res)) 
fnc2 = lambda x: x>30 and x<90
print(f(fnc2,res))

