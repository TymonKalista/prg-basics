import math
r = int(input('Type radius: '))
circurmfernce = round(r*2*math.pi, 2)
area = round(math.pi*r*r, 2)
print(f'Circumference = {circurmfernce}')
print(f'Area = {area}')