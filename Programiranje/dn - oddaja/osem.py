stolpci = "abcdefgh"
vrstice = "12345678"
polje1 ="a4"
polje2 ="b4"
polje="a4"
razpored = ["f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8"]
stolpec="e"

#0
def stolpec_prost(stolpec, razpored):
    s = True
    for r in razpored:
        if stolpec in r:
            s = False
            break
    return s
print(stolpec_prost(stolpec, razpored))
#1
def prosti_stolpci(razpored):
    ps = []
    for s in stolpci:
        if stolpec_prost(s, razpored):
            ps.append(s)
    return ps
print(prosti_stolpci(razpored))
#2
def prost_stolpec(razpored):
    for s in prosti_stolpci(razpored):
        return s
print(prost_stolpec(razpored))
#3
def napada(polje1, polje2):
    s1 = stolpci.index(polje1[0])
    s2 = stolpci.index(polje2[0])
    v1 = vrstice.index(polje1[1])
    v2 = vrstice.index(polje2[1])

    if polje1[1] == polje2[1] or polje1[0] == polje2[0]:
        return True
    elif abs((s1-s2)/(v1-v2)) == 1:
        return True
    else:
        return False
print(napada(polje1, polje2))
#4
def napadajo(polje, razpored):
    ps = []
    for r in razpored:
        if napada(polje,r):
            ps.append(r)
    return ps
print(napadajo(polje,razpored))
#5
def napadeno(polje, razpored):
    if napadajo(polje, razpored):
        return True
    else:
        return False
print(napadeno(polje,razpored))
#6
def prosto_v_stolpcu(stolpec,razpored):
    ls=[]
    if not stolpec_prost(stolpec, razpored):
        return ls
    for a in range(1,9):
        aa = stolpec + str(a)
        if not napadeno(aa,razpored):
            ls.append(aa)
    return ls
print(prosto_v_stolpcu(stolpec,razpored))
#7
def prosto_polje(razpored):
    pst = prost_stolpec(razpored)
    a = prosto_v_stolpcu(pst,razpored)
    if a:
        return a[0]
print(prosto_polje(razpored))
