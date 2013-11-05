#kako narediti konstanto za utf-8?

import random
import math
#stevila = random.random() * 100000000
tecaj = []
def generiraj():
    for i in range (100):
        stevila = random.randrange(20000,21000)
        stevila = str(math.trunc(stevila))
        tecaj.append(stevila)
    return tecaj
tecaj = generiraj()

file = "Yen-tecaj.txt"
def napisi_dat(file,tecaj):
    f = open(file, "wt",encoding = "utf-8")
    for st in tecaj:
        f.write("{}\n".format(st))
#f.write("xxxx")
    f.close()
    return file
file = napisi_dat(file,tecaj)

tecaj = []
def min_maks(file):
    for st in open(file, "rt", encoding= "utf-8"):
        st = st.strip()
        tecaj.append(int(st))
    rezultat = (min(tecaj),max(tecaj))
    return rezultat
rezultat = min_maks(file)
mini, maksi = rezultat
print(mini)
print(maksi)

#math.trunc(x)	x truncated to Integral
#round(x[, n])	x rounded to n digits

