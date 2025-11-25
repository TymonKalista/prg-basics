import matplotlib.pyplot as plt
import math

x = []
y = []


for n in range(0, 361):
    x.append(n)


for n in x:
    y.append(math.sin(math.radians(n)))

plt.plot(x, y)
plt.title("Graph of f(x) = sin(x)")
plt.xlabel("x (degrees)")
plt.ylabel("sin(x)")
plt.grid(True)
plt.show()
