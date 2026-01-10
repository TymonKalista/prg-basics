arr =[(17,15,16,17,15),
 (16,18,19,17,19),
 (19,15,15,19,18),
 (18,17,19,15,16)]
x = list(map(max, arr))
y = list(map(min, arr))
z = list(map(sum, arr))
q = []
for i in range (0, len(z)):
    z[i] = z[i] - x[i] - y[i]
    q.append(z[i])
print(q)
