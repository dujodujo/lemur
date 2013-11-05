def fib1(n):
    if n < 2:
        return 1
    else:
        return fib1(n-1) +  fib1(n-2)
print(fib1(11))
#
#def fib(n):
#    a = 1
#    b = 1
#    for i in range(n):
#        a, b = b, a + b
#    return a
#print(fib(11))

#(1,3,6)
#(3,6,10)
#(6,10,19)
#(10,19,35)
#(19,35,64)
#
#def fib(n,*s):
#    for i in range(n):
#        s = s[1:] + (sum(s),)
#    return s[0]
#print(fib(10,1,2,3))