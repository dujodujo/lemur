recept = "Vzemi 36 dag moke, 6 jajc (lahko tudi 7), zmešaj in peci 20 minut pri temperaturi 250C"
import re
recept = re.sub("[^\w ]", " ",recept)

def je_stevilo(cifra):
        if cifra.isdigit():
            return True
        else:
            return False

def stevilke(recept):
    recept = recept.split(" ")
    niz_stevilk = []
    for cifra in recept:
        if je_stevilo(cifra):
            niz_stevilk.append(cifra)
    return (niz_stevilk)
print(stevilke(recept))
            
