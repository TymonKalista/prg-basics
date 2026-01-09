def f(fnc, prods):
    answ = ''
    for elem in prods:
        answ = answ + fnc(elem) + ','
    return answ[0:-1]
        
prods = ["water","cheese","tomato"]
fnc1 = lambda x: "id:"+x[:2]
print(f(fnc1,prods)) 
fnc2 = lambda x: (x[0]+x[-1]).upper()
print(f(fnc2,prods)) 
