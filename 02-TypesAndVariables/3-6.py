import math
h1= float(input("Jaki jest twój wzrost: "))
print("Odległość do horyzontu na plaży w metrach wynosi: ", 3570*math.sqrt(h1))
h2= 20
print("Odległość do horyzontu z hotelu w metrach wynosi: ", 3570*math.sqrt(h2+h1))
