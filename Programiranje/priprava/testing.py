#s = [1, 2, 7, 14, 33, 140, 5]
#s = []
#s = [0, 7, 14]
#def v7raus(s):
#    return [v for v in s if v % 7 != 0]
#print(v7raus(s))

import math
#o =[(1, 5, 2), (1, 5, 5)]
#o = [(0, 0, 1), (2, 2, 1), (4, 4, 1), (4, 6, 2)]
#o = [(0, 0, 1), (2, 2, 1), (4, 4, 1), (6, 6, 1)]

#def sekajoci(o):
#    for i, (x1, y1, r1) in enumerate(o):
#        for (x2, y2, r2) in o[:i]:
#            if (x2-x1)**2 + (y2-y1)**2 < (r1 + r2)**2:
#                return True
#    return False
#print(sekajoci(o))

#bankovci = {100: 5, 50: 6, 10: 7, 5: 3}

#class Blagajna():
#    def __init__(self, bank):
#        self.bank = bank
#
#    def vsota(self):
#        v = 0
#        for bankovci in self.bank:
#            v += self.bank[bankovci]*bankovci
#        return v

#    def izplacaj(self, izplacilo):
#        for bankovci in izplacilo:
#            if self.bank[bankovci] < izplacilo[bankovci]:
#                raise ValueError
#        for bankovci in izplacilo:
#            self.bank[bankovci] -= izplacilo[bankovci]

#b = Blagajna({100: 5, 50: 6, 10: 7, 5: 3})
#print(b.vsota())
#"885
#b.izplacaj({100: 2, 10: 3})
#print(b.vsota())
#655
#b.izplacaj({100: 7})
#ValueError: nimam toliko bankovcev po 100
#print(b.vsota())
#655


#import re
#t = ["Napiši funkcijo povedi, ki kot argument ", "sprejme nekaj. Kot rezultat ",
#"vrne nekaj drugega, ", "namreč seznam. ", "Kaj naj ta vsebuje? Eh, ",
#"kaj neki, nize! Same ", "nize. ", "Da, tako bodi."]

#def v_stavke(t):
#    t = "".join(t)
#    return re.findall("[^.!?]*[.!?]",t)
#print(v_stavke(t))

#xs = [1, 2, 7, 14, 33, 140, 5]
#ys = [1, 2, 7, 4]
#zs = []

def sodi_lihi(xs):
    sode = [x for x in xs if x %2 == 0]
    lihe = [x for x in xs if x %2 != 0]
    if len(sode) >= len(lihe):
        return sode
    return lihe
print(sodi_lihi(zs))


import string
def naslednji_avtobus(razpored):
    min_prihod = 100
    min_avtobus = 100
    for avtobus in razpored:
        avtobus, prihod = int(avtobus), min(razpored[avtobus])
        if prihod < min_prihod or prihod == min_prihod and avtobus < min_avtobus:
            min_prihod = prihod
            min_avtobus = avtobus
    return min_avtobus, min_prihod

#razpored = {"1": [5, 7], "3": [3, 11], "6": [7]}
#razpored = {"1": [5, 7], "6b": [11, 3], "11": [3, 7]}

#print(naslednji_avtobus(razpored))

