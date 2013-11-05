besede = ["RABarbara", "izpit", "zmagA","itizuzpl"]

def najRaz(besede):
    maxSt = 0
    rez = ""
    for beseda in besede:
        naj_raznolike_besede = set()
        for b in beseda:
            naj_raznolike_besede.add(b.lower())
        velikost= len(naj_raznolike_besede)
        if velikost > maxSt:
            rez = beseda
    return rez

rezultat = najRaz(besede)
print(rezultat)


#def najRaz(besede):
#    maxSt = 0
#    rez = ""
#    for beseda in besede:
#        zbiralnik = []
#        for b in beseda:
#            if b not in zbiralnik:
#                zbiralnik.append(b.lower())
#                print(zbiralnik)
#        if len(zbiralnik) > maxSt:
#            maxSt = len(zbiralnik)
#            rez = beseda
#    return rez
#rezultat = najRaz(besede)
#print(rezultat)

