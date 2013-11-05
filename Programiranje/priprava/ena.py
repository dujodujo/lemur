#Veckratniki 7 raus

def raus(x):
    return [r for r in x if r % 7 != 0]

xs = [[1, 2, 7, 14, 33, 140, 5], [0, 7, 14], []]
for x in xs:
    a = raus(x)
#    print(a)

#sekajoci se krogi

krogi = [[(0, 0, 1), (2, 2, 1), (4, 4, 1), (6, 6, 1)],
        [(0, 0, 1), (2, 2, 1), (4, 4, 1), (4, 6, 2)],
        [(1, 5, 2), (1, 5, 5)]]

def sekajo(krogi):
    for i, (x1, y1, r1) in enumerate(krogi):
        for (x2, y2, r2) in krogi[:i]:
            if ((x2 - x1)**2 + (y2 - y1)**2) < (r1 + r2)**2:
                return True
    return False

for k in krogi:
    kr = sekajo(k)
#    print(kr)

t = ["Napiši funkcijo povedi, ki kot argument ", "sprejme nekaj. Kot rezultat ",
"vrne nekaj drugega, ", "namreč seznam. ", "Kaj naj ta vsebuje? Eh, ",
"kaj neki, nize! Same ", "nize. ", "Da, tako bodi."]

import re
#print(re.findall("[^!.?]*[!.?]", "".join(t)))

#oklepaji

oklepaji = ["((()))", "((())", "(()))", "(())((()()(())))()", "))(("]

def pOklepaji(oklepaji):
    levo = 0
    desno = 0
    for o in oklepaji:
        if o == "(":
            levo +=1
            if desno > levo:
                return False
        elif o == ")":
            desno +=1
    if desno != levo:
        return False
    return True

for o in oklepaji:
    pO = pOklepaji(o)
#    print(pO)

#zaporedni samoglasniki

stavek = "a preudarno, govoriti o njihovem neobstoju bi bilo preuranjeno"
stavek = "jaoao"
stavek = stavek.replace(",","")
besede = stavek.split(" ")

def zaporedni(besede):
    samoglasniki = ['a', 'e', 'i', 'o', 'u']
    stej = 0
    zap = []
    for beseda in besede:
        if len(beseda) > 2:
            for crka in beseda:
                if crka in samoglasniki:
                    stej += 1
                    if stej > 1:
                        zap.append(beseda)
                        break
                else:
                    stej = 0
    return zap

#print(zaporedni(besede))

#brez ntih
#[1, 2, 4, 5, 7, 8, 10]

cc = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def non(cc,n):
    stej = 0
    for i in range(1, len(cc)):
        if i % n == 0:
            stej +=1
            del cc[i - stej]
non(cc,3)
#print(cc)

#sumljive besede

import collections
stavek = "Beseda je sumljiva, če ne poseduje črke, katero posedujejo vse druge besede te povedi."
stavek = stavek.replace(",", "")
stavek = stavek.replace(".","")
stavek = stavek.split(" ")

pojavitev = collections.defaultdict(int)
def sumljive(besede):
    pojavitev = collections.defaultdict(int)
    for beseda in besede:
        for crka in set(beseda):
            pojavitev[crka] += 1
    for crka, pojav in pojavitev.items():
        if pojav == len(besede)-1:
            break
    for beseda in besede:
        if not crka in beseda:
            return beseda

#print(sumljive(stavek))

import collections
nakupi = "C:\\Users\dujo\\PycharmProjects\\Programiranje\\priprava\\nakupi.txt"
artikli = "C:\\Users\dujo\\PycharmProjects\\Programiranje\\priprava\\artikli.txt"

n = collections.defaultdict(list)
a = collections.defaultdict(list)

for line in open(nakupi,"r"):
    line = line.strip()
    koda, cena = line.split("  ")
    n[koda] = float(cena)

for line in open(artikli,"r"):
    line = line.strip()
    koda, kolicina = line.split("  ")
    a[koda] = float(kolicina)

vsota = 0

for koda, cena in n.items():
    if koda in a.keys():
        vsota += n[koda] * a[koda]
#        print(vsota)

#najvec n
import collections

dd = collections.defaultdict(list)
s = [1, 2, 3, 1, 1, 2, 1, 2, 3, 3, 2, 4, 5, 3, 1]
k = 3

def najvec_n(s, k):
    ss = []
    for x in s:
        if x not in dd:
            dd[x] = 1
        else:
            dd[x] += 1

        if dd[x] <= k:
            ss.append(x)
    return ss

bleh = najvec_n(s,k)
blah = [1, 2, 3, 1, 1, 2, 2, 3, 3, 4, 5]

import re

def imena():
    beseda = re.compile("[A-Za-z]\w*")

    keywords = ["and", "del", "from", "not", "while", "as", "elif", "global", "or", "with", "assert", "else", "if",
                "pass", "yield", "break",  "except", "import", "print", "class", "exec", "in", "raise", "continue",
                "finally", "is", "return", "def", "for", "lambda", "try"]

    spremenljivke = set()
    for line in open("C:\\Users\dujo\\PycharmProjects\\Programiranje\\priprava\\testing.py"):
        line = line.strip().split("#")[0]
        spremenljivke.update(beseda.findall(line))
    return sorted(spremenljivke.difference(keywords))
#print(imena())

stavek = "Poet tvoj nov Slovencem venec vije"
vine = "vine"

#xs = []
#maksi = 0

#stavek = stavek.split(" ")
#for beseda in stavek:
#    bes = ""
#    stej = 0
#    for b, v in zip(beseda, vine):
#        if b in vine:
#            bes += b
#        if b == v:
#            stej += 1
#    if maksi < stej:
#        maksi = stej
#        xs.append((beseda, bes, maksi))

#print(xs)

emso = ['2206954500424', '0502933501561', '2002996506452', '0802923508251']

def jeZenska(emso):
    if len(emso) == 13:
        return int(emso[-4:-1]) > 500

#for e in emso:
#    print(jeZenska(e))

emsoti = ['0903912505707', '0110913506472', '2009956506012',
          '1102946502619', '1902922506199', '2602930503913',
          '0204940508783', '1602960505003', '0207959502025',
          '0207962509545']

emsoti = ['1012947507186', '0506929507291', '3107910505475',
          '1109984500497', '0510960506179', '0307978501042',
          '1607944505399', '1706954501918', '1305934508423',
          '1406967504211']

emsoti = ['0503973503512', '3004964501773', '1005933505567',
          '2905936507573', '0712966507144']

emsoti = ['0702948501362', '1505987508785']

#emsoti = ['2807955501835', '1604923501254', '0601925504908']

#emsoti = ['2807955501835']

#emsoti = []

def srecnezi(emsoti):
    if not len(emsoti) or len(emsoti) == 1:
        return 0
    else:
        steviloSrecnih = 0
        
        if jeZenska(emsoti[0]):
            if not jeZenska(emsoti[-1]) and not jeZenska(emsoti[1]):
                steviloSrecnih +=1
        else:
            if jeZenska(emsoti[-1]) and jeZenska(emsoti[1]):
                steviloSrecnih +=1

        for i in emsoti[1:-2]:
            if jeZenska(emsoti[i]):
                if not jeZenska(emsoti[i-1]) and not jeZenska(emsoti[i+1]):
                    steviloSrecnih +=1
            else:
                if jeZenska(emsoti[i-1]) and jeZenska(emsoti[i+1]):
                    steviloSrecnih +=1

        if jeZenska(emsoti[-1]):
            if not jeZenska(emsoti[-2]) and not jeZenska(emsoti[0]):
                steviloSrecnih +=1
        else:
            if jeZenska(emsoti[-2]) and jeZenska(emsoti[0]):
                steviloSrecnih +=1
        return steviloSrecnih

#print(srecnezi(emsoti))

razporedi = ['0505913509174', '2202973506004', '0304943506069',
             '2702943501809', '2407980508463', '0209965503761',
             '2109913502875', '1802924506701', '0207970500808',
             '1501917509568']

razporedi = ['2702943501809', '0505913509174', '0209965503761',
             '2202973506004', '2109913502875', '0304943506069',
             '0207970500808', '2407980508463', '1802924506701',
             '1501917509568']

razporedi = ['2806984508656', '0602925509884', '1102979507594',
             '1104915509537', '1502929506188', '1104923504226']

razporedi = ['1104923504226', '2806984508656', '0602925509884',
             '1102979507594', '1104915509537', '1502929506188']
#
#razpordei = ['2806984508656', '0602925509884', '1102979507594',
#             '1104915509537']

razporedi = ['2806984508656']

razporedi = []

def optimalniRazporedi(razporedi):
    moski = []
    zenske = []

    for oseba in razporedi:
        if jeZenska(oseba):
            zenske.append(oseba)
        else:
            moski.append(oseba)

    parov = min(len(zenske),len(moski))
    razpored = []

    for i in range(parov):
        razpored.append(moski[i])
        razpored.append(zenske[i])

    razpored += moski[len(zenske): ] + zenske[len(moski): ]
    return razpored

#print(optimalniRazporedi(razporedi))

r1 = ["Ana", "Berta", "Cilka", "Dani", "Ema"]
r2 = ["Cilka", "Dani", "Ema", "Ana", "Berta"]
#r2 = ["Berta", "Ana", "Cilka", "Dani", "Ema"]
#r2 = ["Ana", "Berta", "Cilka"]
#r1 = []
#r2 = []

def razporedi(r1, r2):
    for i in range(len(r1)):
        if r2 == r1[i:] + r1[:i]:
            return True
    return not r1 and not r2

#print(razporedi(r1, r2))

gostje = ['0505913509174', '2202973506004', '0304943506069',
             '2702943501809', '2407980508463', '0209965503761',
             '2109913502875', '1802924506701', '0207970500808',
             '1501917509568']

def razporedba(gostje):
    moski = [m for m in gostje if not jeZenska(m)]
    zenska = [z for z in gostje if jeZenska(z)]

    razpored = []
    while moski or zenska:
        for x in moski, zenska:
            if x:
                razpored.append(x.pop())
    return razpored
#print(razporedba(gostje))

#bes1 = "ROKA"
#bes2 = "REKE"

#bes1 = "ROKA"
#bes2 = "ROKAV"

#bes1 = "CELINKE"
#bes2 = "POLOVINKE"

def ujeme(bes1, bes2):
    uj = ""
    for b1, b2 in zip(bes1, bes2):
        if b1 == b2:
            uj += b1
        else:
            uj += "."
    return uj

#print(ujeme(bes1, bes2))

xs = [500, 100, 100, 100, 900]
xs = [500, 100, 100, 100, 900, 100]
xs = [50, 86, 250, 13, 205, 85]
xs = [50, 86, 150, 13, 205, 85]
xs = [5, 5]
xs = [5]
xs = []


def razdeliKnjige(xs):
    polovica = sum(xs)/2
    peter = 0
    stej = 0

    for x in xs:
        if peter + x/2 > polovica:
            break
        peter += x
        stej +=1
    return stej, len(xs) - stej

#print(razdeliKnjige(xs))


#ploscina = [(0, 0), (1, 0), (2, .5), (1, 1), (1, 2), (.5, 1), (0, 2)]

def ploscine(p):
    pl = 0
    for i in range(1, len(p)):
        pl += p[i-1][0]*p[i][1] - p[i-1][1]*p[i][0]
    pl += p[0][0]*p[-1][1] - p[0][1]*p[-1][0]
    return pl*0.5

#print(ploscine(ploscina))

visineStopnic = ([10, 20, 25, 45, 50, 71, 98, 110], [30, 40, 50], [10, 20, 30, 40, 45])

def stopnice(visine):
    zacetek = 0
    for i in range(len(visine)):
        if visine[i] - zacetek > 20:
            return visine[i]
        zacetek = visine[i]
    return visine[-1]

for v in visineStopnic:
    stopnice(v)

#esv ej eboran idut elat kevats
stavek = "vse je narobe tudi tale stavek"

#print(" ".join([s[::-1] for s in stavek.split()]))

emso = "3105985500204"

#class Oseba:
#    def __init__(self, ime, spol, emso):
#        self.ime = ime
#        self.spol = spol
#        self.emso = emso
#
#
#    def preveri_emso(self):
#        dnevi = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#        dan, mesec = int(self.emso[:2]), int(self.emso[2:4])
#        if not (1 <= mesec <= 12 and 1 <= dan <= 31):
#            return False
#        if dan > dnevi[mesec - 1]:
#            return False
#        if self.spol != ('Z' if self.emso[9] >= '5' else 'M'):
#            return False
#        ctl = sum(int(e) * i for e, i in zip(self.emso, [7, 6, 5, 4, 3, 2, 7, 6, 5, 4, 3, 2]))
#        return (ctl + int(self.emso[-1])) % 11 == 0

import math

def vrvi():
    hlodi = [(23.989,  8.526), (31.338, 11.759), (35.16, 17.933),
             (47.507, 11.759), (54.269, 24.694), (63.088, 5.880),
             (69.556, 13.523), (72.496, 29.692), (78.082, 8.966),
             (84.255, 16.169), (91.017,  8.048), (94.838, 11.759),
             (102.776, 4.263), (109.244, 20.285), (117.181, 8.966),
             (118.945, 3.381), (121.591, 8.966), (133.35, 6.762)]

    while len(hlodi) > 2:
        novi = [hlodi[0]]
        for i in range(1, len(hlodi)-1):
            x0, y0 = novi[-1]

            x1, y1 = hlodi[i]
            x2, y2 = hlodi[i+1]

            if (y1 - y0) / (x1 - x0) >= (y2 - y1) / (x2 - x1):
                novi.append((x1, y1))
        novi.append(hlodi[-1])
        if novi == hlodi:
            break
        hlodi = novi
    return hlodi
print(vrvi())
