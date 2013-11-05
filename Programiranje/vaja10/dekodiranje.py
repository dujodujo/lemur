s = "10a,6b,1a,13c"

def dekodiranje(niz):
    novNiz = ""
    niz = niz.split(",")
    for n in niz:
        dek = int(n[:-1])*n[-1]
        novNiz = novNiz + dek
    return novNiz
deko = dekodiranje(s)

def ceta(deko):
    for i,d in enumerate(deko):
        if d != deko[0]:
            return deko[:i] ,ceta(deko[i:])
    return deko,""

print(ceta('aaaaaaaaaabbbbbbaccccccccccccc'))
print(ceta('bbbbbbaccccccccccccc'))
print(ceta('accccccccccccc'))
print(ceta('ccccccccccccc'))

def kodiranje_cet(s):
    cete = []
    while s:
        glava, s = ceta(s)
        cete.append(str(len(glava)) + glava[0])
    return ','.join(cete)