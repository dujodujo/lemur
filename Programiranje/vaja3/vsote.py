xs = [9, 1, 2, 3, 8, 9, 0, 4, 3, 7]

vsota = 0
naj = sum(xs[:5])
for i in range(len(xs)-2):
    vsota = sum(xs[i:i+5])
    if naj < vsota:
        naj = vsota
print(naj)
    