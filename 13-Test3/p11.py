def f(car, order):

    car = str(car)
    car = car.replace('}, {', ',')  
    car = car.replace('[', ' ')  
    car = car.replace(']', ' ')  
    car = eval(car)
    if order == '1': 
        car = dict(sorted(car.items()))
    elif order == '2': 
        car = dict(sorted(car.items(), reverse=True, key=lambda item: item[1]))
    car = str(car)
    car = car.replace(',', '}, {')
    car = '[' + car + ']'
    
    return car

cars = [{"KR333": 138}, {"WL555": 497}, {"DB444": 341}, {"MC222": 412}]
print(f(cars, '1'))  
print(f(cars, '2'))  
