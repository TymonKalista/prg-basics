###
# Calculates the area of a triangle based on the lengths
# of the triangle's sides
#
import math
def triangle_area(a,b,c):
    s = (a + b + c)*0.5
    area = math.sqrt(s*(s - a)*(s- b)*(s - c))

    return area

area1 = triangle_area(3,4,5)
area2 = triangle_area(5,12,13)
area3 = triangle_area(7,24,25)

print('The area of a triangle with sides 3,4,5 is ', area1)
print('The area of a triangle with sides 5,12,13 is ', area2)
print('The area of a triangle with sides 7,24,25 is ', area3)