#import collections
#
#seznam = []
#ime = "berta"
#
#slovar = collections.defaultdict(set)
#for i in range(65,91):
#    a = chr(i)
#    (beseda, vrednost) = chr(i).lower(), ord(a)
#    slovar[beseda] = vrednost - 64
#
#
#vsota = 0
#for crka in ime:
#    if crka in slovar:
#        vsota += slovar[crka]
#while len(str(vsota)) < 9:
#    n_vsota = 0
#    for s in str(vsota):
#        n_vsota += int(s)
#    vsota = str(n_vsota)
#print(vsota)

ime = "benjamin"


def numerologija(ime):
    vs = 0
    for c in ime.upper():
        vs += ord(c) - 64
    while vs > 9:
        n_vsota = 0
        for s in str(vs):
            n_vsota += int(s)
        vs = n_vsota
    return vs

def numerologija1(ime):
    vs = 0
    for c in ime.upper():
        vs += ord(c) - 64
    while vs > 9:
        nova = 0
        for c in str(vs):
            nova += int(c)
        vs = nova
    return vs

num1 = numerologija1(ime)
num = numerologija(ime)
print(num, num1)