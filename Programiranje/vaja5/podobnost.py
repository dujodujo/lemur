s1 = "sobota"
s2 = "robot"

def primerjaj(s1,s2):
    stevec = 0
    for s, r in zip(s1,s2):
        if s == r:
            stevec +=1
    return stevec
print(primerjaj(s1,s2))