import os
import collections
import pprint

cwd =".\\dn8_tree"

print("")
print("")

def preisci0(dir):
    dir_xs = []
    for xName in os.listdir(dir):
        dirList = os.path.join(dir,xName)
        if os.path.isdir(dirList):
            dir_xs.extend(preisci0(dirList))
        elif os.path.isfile(dirList):
            dir_xs.append(dirList)
    return dir_xs

def preisci(dir):
    slovar = collections.defaultdict(set)
    xxs = preisci0(dir)
    for l in xxs:
        ime_dat, ime_dir= os.path.split(l)
        slovar[ime_dir].add(ime_dat)
    return slovar

slovar = preisci(cwd)
print("preisci:")
pprint.pprint(slovar)

print("")
print("")

def isci(datoteke,arg):
    imenik1 = collections.defaultdict(set)

    for ime_dat, ime_dir in datoteke.items():
        if arg in ime_dat:
            imenik1[ime_dat] = ime_dir
    return imenik1

rIsci = isci(slovar,"main.c")
print("isci",)
pprint.pprint(rIsci)

print("")
print("")

def trojke(datoteke):
    imenik2 = collections.defaultdict(set)
    for k in datoteke:
        for i in range(len(k)-2):
            if k[i:i+3] in k:
                imenik2[k[i:i+3]].add(k)
    return imenik2

rTrojke = trojke(slovar)
print("trojke")
pprint.pprint(rTrojke)

def isci_hitro(datoteke,trojke,vzorec):
    xss = []
    imenik3 = collections.defaultdict(set)
    for k,v in trojke.items():
        if k in vzorec:
            xss.append(v)
    if not xss:
        return set()
    presek = set.intersection(*xss)
    for p in presek:
        if vzorec in p:
            imenik3[p] = datoteke[p]
    return imenik3
    
rIsci_hitro = isci_hitro(slovar,rTrojke,"main.c")
print(rIsci_hitro)

