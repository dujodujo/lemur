b = (1, 2, 3)
a = (4, 5, 6)

prod = 0
for x,y in zip(a,b):
    prod += x*y
print(prod)

print(' + '.join('%d * %d' % (x, y) for x, y in zip(a, b)))