def sestavljena_stevila(n):
    for i in range(2,n):
        if n % i == 0:
            return True
    return False

ss = sestavljena_stevila(12)
print(ss)

def prastevila(n):
    pras = []
    for i in range(2,n):
        if prastevilo(i):
            pras.append(i)
    return pras

def deljivost(n,i):
    counter = 0
    while n % i == 0:
        n = n / i
        counter +=1
    return counter

def razcep(n):
    t = []
    for p in prastevila(n):
        d = deljivost(n, p)
        if d != 0:
            t.append((p, d))
    return t