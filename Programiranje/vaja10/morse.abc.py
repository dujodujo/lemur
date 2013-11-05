import collections

slovar  = collections.defaultdict()
for line in open("morse.txt","rt"):
    line = line.replace(",","")
    line = line.replace("'","")
    line = line.replace(":","").strip()
    line = line.split()
    crka , koda = line[0], line[1]
    slovar[crka] = koda

slovar[' '] = ''

def txt2morse(arg):
    niz = ""
    for a in arg:
        izpis = slovar[a]
        niz = niz + izpis + " "
    return niz[:-1]

arg = 'HELLO WORLD'
ttm = txt2morse(arg)
print("textToMorse",ttm)

#def txt2morseB(arg):
#    return ' '.join(slovar[c] for c in arg)

def obrni_slovar(slovar):
    slovar2 = collections.defaultdict()
    for kljuc, vrednost in slovar.items():
        slovar2[vrednost] = kljuc
    return slovar2
slovar2 = obrni_slovar(slovar)
print("obs slovar",slovar2)

def morse2txt(ttm):
    str = ""
    ttm = ttm.split(' ')
    for t in ttm:
        str += slovar2[t]
    return str
mtt = morse2txt(ttm)
print(mtt)

def morse2textB(ttm):
    return "".join(slovar2[t] for t in ttm.split(' '))
morse = morse2textB(ttm)
print(morse)