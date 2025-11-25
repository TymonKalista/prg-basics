a =[
    [7, 3, 7 ,9, 0],
    [2, 9, 0, 1, 5],
    [3, 8, 6, 4, 7],
    [8,7,1,1,5]
]
couner = 0
for row in a:
    couner = couner + row[-1]
print(couner)
