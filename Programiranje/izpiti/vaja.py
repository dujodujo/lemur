
imena = ['marko', 'Miha', 'maja', 'Monika']
print("***9.1***")
def capitalize(imena):
    nova = []
    for im in imena:
        nova.append(im.capitalize())
    return nova
capi = capitalize(imena)
print(imena)
print(capi)

print("***9.1***")

def icapitalize(imena):
    for i in range(len(imena)):
        imena[i] = imena[i].capitalize()
print(icapitalize(imena))
print(imena)

def count(n):
    n = str(n)
    vsota = 0
    for cifra in n:
        vsota +=int(cifra)
    if vsota > 9:
        return count(vsota)
    return vsota
cc = count(2147483647)
print(cc)

print("maska")


