n = input('Enter speed in m/s: ')
new_speed = lambda x : int(x)*3.6

result = new_speed(n)


print(f'This speed in km/h is: {result}')