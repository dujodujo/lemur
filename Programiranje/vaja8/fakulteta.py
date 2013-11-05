def fakulteta(n):
    if n < 2:
        return 1
    else:
        return n*fakulteta(n-1)
#print(fakulteta(1))
#print(fakulteta(2))
#print(fakulteta(3))
#print(fakulteta(4))
#print(fakulteta(5))


rez = fakulteta(12)/(fakulteta(3)*fakulteta(9))
print(rez)