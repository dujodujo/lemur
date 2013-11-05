
niz = "vse je narobe tudi tale stavek"

#niz = niz.split(" ")
#nov = []
#for n in niz:
#    nov.append(n[::-1])
#nov = " ".join(nov)
#print(nov)

n = " ".join([n[::-1] for n in niz.split(" ")])
print(n)