# Fibonacci

#iteracija
k = int(input("Vnesi k: "))
a = 0
b = 1
l = []
if a == 0:
    l.append(a)
for i in range(0,k):
    a, b = b, a+b
    l.append(a)
print(l)
