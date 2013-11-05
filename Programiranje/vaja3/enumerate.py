xs = [5, 1, 4, 2, 3]
xss = []

#for x in enumerate(xs):
#    xss.append(x)
#print(xss)

i = 0
for i in range(len(xs)):
    l = (i,xs[i])
    xss.append(l)
print(xss)
