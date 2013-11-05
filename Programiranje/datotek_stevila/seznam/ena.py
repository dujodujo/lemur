import math
import re
import random
import collections
import os
import string
import pprint

sedemkratniki = [[0, 7, 14, 17, 23, 27], [1, 2, 7, 14, 17,  33, 140, 5]]
def vraus(sedem):
    return [s for s in sedem if not s % 7 == 0]

def vvraus(sedem):
    return [s for s in sedem if not s % 7 == 0 and not "7" in str(s)]

rezultat7 = []
rezultat77 = []
for sedem in sedemkratniki:
    rezultat7.append(vraus(sedem))
    rezultat77.append(vvraus(sedem))
print(rezultat7)
print(rezultat77)

pari_krog = [[(0, 0, 1), (2, 2, 1), (4, 4, 1), (6, 6, 1)],
             [(0, 0, 1), (2, 2, 1), (4, 4, 1), (4, 6, 2)],
             [(1, 5, 2), (1, 5, 5)]]

def sekajo1(pari):
    for i in range(len(pari)-1):
        for j in range(i+1, len(pari)):
            x1, y1 ,r1 = pari[i]
            x2, y2, r2 = pari[j]
            if math.sqrt((x2 - x1)**2 + (y2 - y1)**2) < r1 + r2:
                return True
    return False

def sekajo11(pari):
    for i, (x1, y1, r1) in enumerate(pari):
        for (x2, y2, r2) in pari[:i]:
            if math.sqrt((x2 - x1)**2 + (y2 - y1)**2) < r1 + r2:
                return True
    return False

for pari in pari_krog:
    print(sekajo1(pari))
    print(sekajo11(pari))

class Blagajna(object):
    def __init__(self, xs):
        self.bankovci = xs

    def vsota(self):
        vsota = 0
        for bankovec in self.bankovci:
            vsota += self.bankovci[bankovec]*bankovec
        return vsota

    def izplacaj(self, xss):
        for bankovec, komadi in xss.items():
            self.bankovci[bankovec] -= komadi

xs = {100: 5, 50: 6, 10: 7, 5: 3}
b = Blagajna(xs)
print(b.vsota())
b.izplacaj({100:2, 50:2, 10: 2})
print(b.vsota())
b.izplacaj({100:3, 50:3, 10: 2})
print(b.vsota())
b.izplacaj({100:7})
print(b.vsota())

poved = ["Napisi funkcijo povedi, ki kot argument ",
         "sprejme nekaj. Kot rezultat ",
         "vrne nekaj drugega, ",
         "namres seznam. ",
         "Kaj naj ta vsebuje? Eh, kaj neki, nize! Same nize. ",
         "Da, tako bodi."]

def v_stavke11(poved):
    return [x+ "." for x in "".join(poved).split(".")][:-1]
tt = v_stavke11(poved)
print(tt)

def stavke(poved):
    return re.findall("[^.!?]*[.!?]", "".join(poved))
print(stavke(poved))

class ListMod(list):
    def __getitem__(self, item):
        return super(ListMod, self).__getitem__(item % len(self))

    def __setitem__(self, item, value):
        return super(ListMod, self).__setitem__(item % len(self), value)

b = ListMod()
for e in "Benjamin":
    b.append(e)
print(b[3])

prepovedane = {"zadnjica", "tepec", "pujs", "kreten"}
povedi = ["Pepe je ena navadna zadnjica in pujs in se kaj hujsega",
          "Pepe je ena velika Zadnjica in PUJS in se kaj hujsega",
          "Pepe je okreten"]

def cenzura(poved, prepovedane):
    return " ".join([p for p in poved.split(" ") if p.lower() not in prepovedane])

for poved in povedi:
    print(cenzura(poved, prepovedane))

niz = "8732"
print(niz[::-1])


def gcd(a, b):
    print(b,a)
    if not b:
       return a
    else:
       return gcd(b, a % b)
a = 12345
b = 54321
print(gcd(a,b))

stevilo = "12345"
stevilo = int(stevilo)
n = 1
stevila = [1]
dvojisko = []
while n < stevilo:
    n *= 2
    if n < stevilo:
        stevila.append(n)
trenutno = 0
for s in stevila[::-1]:
    if trenutno + s  <= stevilo:
        trenutno = trenutno + s
        print(trenutno)
        dvojisko.append("1")
    else:
        dvojisko.append("0")
print("".join(dvojisko))

oklepaji = ["()", "(())", "(()()())()", "((", "())(", "(()()))"]

def oklepaji1(ook):
    levi = 0
    desni = 0
    for o in ook:
        if o == "(":
            levi +=1
        else:
            desni +=1
            if desni > levi:
                return False
    if levi == desni:
        return True
    return False

for ook in oklepaji:
    print(oklepaji1(ook))

osebe = ["Ana", "Berta", "Cilka", "Dani", "Ema", "Nada"]
trenutna = 0
while len(osebe) > 1:
    trenutna = (trenutna + 11) % len(osebe)
    ven = osebe.pop(trenutna)
    print ("Izlocena:", ven)
print ("Ostane", osebe[0])

stevilo = int("14")
print(str(bin(stevilo))[2:])

stevilo = 563
dvojiska_stevila = []
while stevilo:
    stevilo, ostanek = round(int(stevilo / 2), 0), int(stevilo % 2)
    dvojiska_stevila.append(str(ostanek))
print("".join(dvojiska_stevila)[::-1])

dvojisko = "1000110011"
dvojisko = dvojisko[::-1]

desetisko_stevilo = []
for i,d in enumerate(dvojisko):
    desetisko_stevilo.append(int(d) * (2**i))
print(sum(desetisko_stevilo))

niz = "Joj ta Python spet se pocutim kot mentalno zaostala oseba"
grde_besede = [('idiot', ['mentalno zaostala oseba', 'omejen clovek'])]
grde_besede = dict(grde_besede)
print(grde_besede)

print(' '.join(grde_besede.get(beseda, [beseda][0]) for beseda in niz.split()))
niz = "to je test joina"
print(" ".join(beseda for beseda in niz.split(" ")))

l = [5, 4, -7, 2, 9, -3, -4, -11, 7]
min_max = l[0]
for a in l:
    if a < min_max:
        min_max = a
print(min_max)

a = [1, 2, 3, 6, 7]
b = [4, 5, 6]
xs = [x + y for x,y in zip(a,b)] + a[len(b):] + b[len(a):]
print(xs)

xs = [1, 4, 3, 5, 2]
count = 0
for i, a in enumerate(xs):
    for j, b in (enumerate(range(1,len(xs)))):
        if i < j and a > b:
            print((i,j),(a,b))
            count +=1

count = 0
for i in range(len(xs)-1):
    for j in range(1,len(xs)):
        if i < j and xs[i] > xs[j]:
            print((i,j),(xs[i],xs[j]))
            count +=1

najnaj = [1,2,3,4,5,[6,7,[111,9],10],11,[[[13]]]]
def najvecji(najnaj):
    elementi = []
    for naj in najnaj:
        if isinstance(naj, list):
            elementi.extend(najvecji(naj))
        else:
            elementi.append(naj)
    return elementi
xs = [1, [], [2, 3, [4]], 5]

xs = [1,2,3,4,5,[6,7,[8,9],10],11,[[[13]]]]
def sum(xs):
    vsota = 0
    for x in xs:
        if isinstance( x, list):
            vsota += sum(x)
        else:
            vsota +=x
    return vsota
xx = sum(xs)
print(xx)

najnaj = [1,2,3,4,5,[6,7,[14,9],10],11,[[[15]]]]
def najvecji(najnaj):
    elemnti = []
    for naj in najnaj:
        if isinstance(naj, list):
            elemnti.append(najvecji(naj))
        else:
            elemnti.append(naj)
    return max(elemnti)
print(najvecji(najnaj))

minmin = [1,2,3,4,5,[6,7,[14,9],10],11,[[[15]]]]
def najvecji(minmin):
    elemnti = []
    for naj in minmin:
        if isinstance(naj, list):
            elemnti.append(najvecji(naj))
        else:
            elemnti.append(naj)
    return min(elemnti)
print(najvecji(minmin))

def preisci(direktorij):
    datoteke = []
    stevilke = []
    preisci0(direktorij, datoteke)
    for d in datoteke:
        stevilke.append(int(d[-2:]))
    return max(stevilke)

def preisci0(direktorij, datoteke):
    for name in os.listdir(direktorij):
        full_name = os.path.join(direktorij, name)
        if os.path.isdir(full_name):
            preisci0(full_name, datoteke)
        else:
            datoteke.append(name)

datoteka = os.getcwd() + "\\family.txt"
def family_tree(datoteka):
    druzina = collections.defaultdict(list)
    for line in open(datoteka, "rt"):
        (stars, otrok) = line.split()
        druzina[stars].append(otrok)
    return druzina
drevo = family_tree(datoteka)
print(drevo)

otrok = "rob"
stars = "sid"
otrok = "suzan"
stars = "sid"

def jeStars(stars, otrok):
    if otrok in drevo[stars]:
        return True
    return False
print(jeStars(stars,otrok))

def potomec(stars, otrok, drevo):
    names = []
    for otroci in drevo[stars]:
        names.append(otroci)
        names.extend(potomec(otroci,otrok,drevo))
    return names

def jePotomec(stars,otrok,drevo):
    imena = potomec(stars,otrok,drevo)
    if otrok in imena:
        return True
    return False
print(jePotomec(stars, otrok, drevo))

xs = [5, 4, 6, 7, 1]
def convert(xs):
    if not xs:
        return ()
    else:
        return xs[0], convert(xs[1:])
print(convert(xs))

xs = (5, (4, (6, (7, (1, ())))))
def length(xs):
    if not xs:
        return 0
    else:
        return 1 + length(xs[1])
print(length(xs))

niz = "Tako je rekel (brez obotavljanja): Ce ne gremo, bomo ostali tu... Drzi?!"
print(re.sub(r'\W', ' ', niz))
niz = "besedE, kI sE KoncajO Z mAlO"
print(re.findall(r'\b[a-z]+[A-Z]\b',niz))
niz = "+386 1 123 4567"
for match in re.finditer(r'(\+386 [1-7]?) ([ -]?\d){7}',niz):
    print(match.group(0))
niz = "Zofke Kvedrove ulica 25, Ljubljana, Slovenija"
niz = "Tito Avenue 123,\nAccra,\nGhana"
for match in re.finditer(r'([a-zA-Z]+ )+\d{1,3},\n[a-zA-Z]+,\n[a-zA-Z]+', niz):
    print(match.group(0))
niz = ["Love Can Seriously Damage Your Health", "Prsut Prsut",
       "Vicky Cristina Barcelona", "Meseno pozelenje",
       "Sin noticias de Dios", "Not Love" , "Just Frenzy"]
for n in niz:
    print(" ".join(re.findall(r'[a-zA-Z]+',n)))

skritopis = "Napisi funkcijo skritopis(s), ki (kar predobro) skrije besedilo tako, da vsako besedo zamenja z njeno prvo crko."
print(re.sub(r'\w+',lambda mo: mo.group(0)[0], skritopis))

p1 = "Tule    je samo en prevec."
p2 = "Tule ni nobenega prevec."
p3 = "Ta    je res    pretiran."
print(len(re.findall(r'\s\s+',p3)) / len((re.findall(r'\s+',p3))))

tiz = ["Napisi funkcijo povedi, ki kot argument ", "sprejme nekaj. Kot rezultat ",
"vrne nekaj drugega, ", "namrec seznam. ", "Kaj naj ta vsebuje? Eh, ",
"kaj neki, nize! Same ", "nize. ", "Da, tako bodi."]
print(re.findall(r'[^.!?]*[.!?]',"".join(tiz)))

poved = "Poet tvoj nov Slovencem venec vije"
sub = "vine"

def prileg(poved, sub):
    indeks = [0]
    for i in range(1,len(poved)-1):
        if not str(poved[i]).isalpha():
            indeks.append(i+1)
    poved = poved.split(" ")
    zadetki = []
    for beseda in poved:
        zadetek = 0
        for a, b in zip(beseda, sub):
            if a == b:
                zadetek +=1
        zadetki.append((zadetek, beseda))
    rezultat = []
    for indeks, (zadetek, beseda) in zip(indeks, zadetki):
        rezultat.append((zadetek, indeks, beseda))
    maxi = rezultat[0]
    for i in range(1,len(rezultat)):
        if rezultat[i-1][0] < rezultat[i][0]:
            maxi = rezultat[i]
    return maxi
print(prileg(poved, sub))

s = "Poet tvoj"
def naj_prileg(s,sub):
    najpos = najuj = -1
    for pos in range(len(s)-len(sub)+1):
        uj = 0
        for c1, c2 in zip(s[pos:], sub):
            print(c1, c2)
            if c1 == c2:
                uj += 1
        if uj > najuj:
            najpos, najuj = pos, uj
    return najpos, najuj, s[najpos:najpos+len(sub)]
naj_prileg(s,sub)

n = 2
niz = "ACATATGAD"
def indeksiraj(niz, n):
    slovar = {}
    for i in range(len(niz)-1):
        znak = niz[i:i+n]
        if znak in slovar:
            slovar[znak].append(i)
        else:
            slovar[znak] = [i]
    return slovar
print(indeksiraj(niz,n))

razpored = ["Ana", "Berta", "Cilka", "Dani", "Ema"]
prerazpored = ["Berta", "Cilka", "Dani", "Ema", "Ana"]
prerazpored = ["Cilka", "Dani", "Ema", "Berta", "Ana"]
prerazpored = ["Berta", "Ana", "Cilka", "Dani", "Ema"]
prerazpored = ["Ana", "Berta", "Cilka"]
prerazpored = ["Greta", "Helga"]
razpored = []
prerazpored =[]

def enaka_razporeda(razpored, prerazpored):
    for i in range(len(razpored)):
        if prerazpored == razpored[i:] + razpored[:i]:
            print(prerazpored)
            return True
    return not razpored and not prerazpored
print(enaka_razporeda(razpored,prerazpored))

xss = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10), (11, 12)]
for i, (x1, y1) in enumerate(xss):
    for (x2, y2) in xss[:i]:
        print((x1, y1), (x2, y2))

for i, (x1, y1) in enumerate(xss):
    for (x2, y2)in xss[i+1:]:
        print((x1, y1), (x2, y2))

for i in range(0,len(xss),2):
    print(xss[i], xss[i+1])

def smrekica(p):
    for i in range (1,p):
        n = 2*i-1
        for j in range(0,i):
            print(" "*j, "*"*(n-2*j), " "*j)
        print("")
smrekica(5)

def smrekica(n):
    for j in range(1,n-1):
        print(" "*(n-(j+2)), "*"*(2*j-1), " "*(n-(j+2)) )
smrekica(5)

english = "xywqXYQW"
def preberi_datoteko(file):
    number_of_lines = 0
    number_of_chars = 0
    for line in open(file,"rt"):
        for l in line:
            if l in english:
                number_of_chars +=1
    return number_of_chars
print(preberi_datoteko("family.txt"))

niz = "aabcdeabcabdeaabcabababc"
podniz = "abc"
def isci(niz, podniz):
    stej = 0
    for i in range(len(niz)-2):
        if podniz == niz[i:i+3]:
            stej +=1
    return stej
print(isci(niz, podniz))

besedilo = "123 109 as34 as a84r9s"
def prestej_stevke(besedilo):
    stevke = {}
    for b in besedilo:
        if str(b).isdigit():
            if b not in stevke:
                stevke[b] = 1
            else:
                stevke[b] += 1
    return stevke
print(prestej_stevke(besedilo))

besedilo = "123 109 as34 as a84r9s"
def inicializiraj(stevke):
    for i in range(0,10):
        stevke[i] = 0
    return stevke

def prestej_stevke(besedilo):
    stevke = {}
    stevke = inicializiraj(stevke)
    for b in besedilo:
        if str(b).isdigit():
            stevke[int(b)] += 1
    return stevke
print(prestej_stevke(besedilo))

def preberi_tecaje(file):
    imena = []
    vrednosti = []
    vred = []
    for line in open(file,"rt"):
        if str(line[0]).isalpha():
            imena.append(line[:4])
            vr = line[5:].strip().split(" ")
            vrednosti.append([float(v) for v in vr])
    return imena, vrednosti

def ustvari_tecajnico(imena, vrednosti):
    tecajnica = {}
    for ime, vrednost in zip(imena, vrednosti):
        tecajnica[ime] = vrednost
    return tecajnica

def min_vrednost(tecajnica, indeks):
    return min(tecajnica[indeks])

def max_vrednost(tecajnica, indeks):
    return max(tecajnica[indeks])

def povp_vrednost(tecajnica, indeks):
    return sum(tecajnica[indeks])/len(tecajnica[indeks])

def razlika_vrednosti(tecajnica, indeks):
    return (abs((tecajnica[indeks][-1] - tecajnica[indeks][0])) / tecajnica[indeks][0] )*100

def dnevna_razlika(tecajnica,indeks):
    t = tecajnica[indeks]
    max_raz = 0
    for i in range(len(t)):
        mr = abs((t[i-1] - t[i]) / t[i-1]) * 100
        if max_raz < mr:
           max_raz = mr
    return max_raz

def vse_max_sprememba(tecajnica, imena):
    return max([(razlika_vrednosti(tecajnica,ime),ime) for ime in imena])

def vse_max_dnevna_sprememba(tecajnica, imena):
    return max([(dnevna_razlika(tecajnica,ime),ime) for ime in imena])

def vrednost_portfelja(file, dan, tecajnica):
    vrednost_port = 0
    for line in open(file,"rt"):
        moje_delnice, delnice = line.split(" ")
        vrednost_port += tecajnica[moje_delnice][dan]*int(delnice)
    return vrednost_port

def izpis_delnic_tecaj(im, tecajnica):
    return "".join([ime + ": " + str(tecajnica[ime]) + " \n" for ime in im])

def izpis_statistike_delnic(im, tecajnica, dan, file):
    rez = []
    a = "Statistika delnice"
    b = "najnizja vrednost"
    c = "najvisja vrednost"
    d = "povprecna vrednost"
    e = "mesecna sprememba"
    f = "najvecja dnevna sprememba"
    g = "Skupna statistika vseh delnic"
    h = "delnica z najvecjo mesecno spremembo"
    i = "delnica z najvecjo spremembo"
    j = "Vrednost vasega portfelja na dan"
    for ime in im:
        rez.append("{} {} \n  -{} {} \n  -{} {} \n  -{} {} \n  -{} {} \n  -{} {} \n\n".format(a, ime,
                                      b, min_vrednost(tecajnica, ime),
                                      c, max_vrednost(tecajnica, ime),
                                      d, povp_vrednost(tecajnica, ime),
                                      e, razlika_vrednosti(tecajnica, ime),
                                      f, dnevna_razlika(tecajnica, ime)))

    rezz = "{} \n{} {}\n{} {}\n{} {} {}\n\n".format(g, h, vse_max_sprememba(tecajnica,im)[1],
                                           i, vse_max_dnevna_sprememba(tecajnica, im)[1],
                                           j, dan, vrednost_portfelja(file, dan, tecajnica))
    return "".join(rez) + rezz

def go(indeks, seznam_delnic, dan, delnice, portfelj):
    imena, vrednosti = preberi_tecaje(delnice)
    tecajnica = ustvari_tecajnico(imena, vrednosti)
    min_v = min_vrednost(tecajnica, indeks)
    max_v = max_vrednost(tecajnica, indeks)
    povp_v = povp_vrednost(tecajnica, indeks)
    razlika_v = razlika_vrednosti(tecajnica, indeks)
    max_razlika = dnevna_razlika(tecajnica,indeks)
    mesec_iskan_papir = vse_max_sprememba(tecajnica, imena)
    dan_iskan_papir = vse_max_dnevna_sprememba(tecajnica, imena)
    vrednost_port = vrednost_portfelja(portfelj, dan, tecajnica)
    izpis_delnic = izpis_delnic_tecaj(seznam_delnic, tecajnica)

    izpis_statistike = izpis_statistike_delnic(seznam_delnic, tecajnica, dan, portfelj)
    print(izpis_statistike)

indeks = "KRKG"
seznam_delnic = ["GRVG", "IEKG", "KBMR", "KRKG", "LKPG", "PETG", "TLSG", "ABKN", "RS32", "ZT02"]
dan = 5
delnice = "delnice.txt"
portfelj = "portfelj.txt"
go(indeks, seznam_delnic, dan, delnice, portfelj)

isbn = "013110362"
isbn = "961200991"
isbn = "020512669"
isbn = "030640615"

def preveri_isbn(isbn):
    isbn = isbn.replace("-","")
    stevilka = sum([int(mark) * i for mark, i in zip(reversed(isbn),range(2,11))])
    ostanek = stevilka % 11
    kontrola_stevilka = 11 - ostanek
    blah = stevilka + kontrola_stevilka
    if (stevilka + kontrola_stevilka) % 11 == 0:
       return isbn  + str(kontrola_stevilka)
    return False
print(preveri_isbn(isbn))

file = "vesolje.txt"
def preglej_vesolje(file):
    max_min = list
    space_dict_sorted = 0
    space_dict = collections.defaultdict()
    for line in open(file, "rt"):
        line = line.split(" ")
        for word in line:
            if not word.isdigit() and word != "":
                if word not in space_dict:
                    space_dict[word] = 0
                space_dict[word] +=1
    space_dict_sorted = sorted(space_dict.values())
    space_dict_reversed = space_dict_sorted[::-1]
    izpisi(space_dict, space_dict_sorted, space_dict_reversed)

def izpisi(space_dict, space_dict_sorted, space_dict_reversed):
    pprint.pprint(space_dict)
    print(space_dict_sorted)
    print(space_dict_reversed)
preglej_vesolje(file)

def beri_izpite(file1):
    izpiti = []
    for line in open(file1, "rt"):
        vpisna, izpit = line.strip().split(" ")
        izpiti.append([vpisna, izpit])
    return izpiti

def beri_naloge(file2):
    naloge = []
    for line in open(file2, "rt"):
        vpisna, nalogice, naloga1, naloga2, naloga3, naloga4 = line.strip().split(" ")
        naloge.append([vpisna, nalogice, naloga1, naloga2, naloga3, naloga4])
    return naloge

def izracunaj_nalog(naloge):
    xs = []
    for vpisna in naloge:
        ocene_nalog = sum([int(s) for s in vpisna[1:]])
        xs.append([vpisna[0], ocene_nalog])
    return xs

def izracunaj_izpite(izpiti, naloge):
    ocena = []
    for student in izpiti:
        vpisna1, izpit = student
        izpit = int(izpit)
        for s in naloge:
            vpisna2, naloga = s
            naloga = int(naloga)
            if vpisna1 == vpisna2 and izpit > 25 and naloga > 25:
                ocena.append([vpisna1, naloga, izpit, izpit + naloga])
            elif vpisna1 == vpisna2 and (naloga < 25 or izpit < 25):
                ocena.append([vpisna1, naloga, izpit, "--"])
    return ocena

file1 = "izpiti.txt"
file2 = "vaje.txt"
naloge = beri_naloge(file2)
izpiti = beri_izpite(file1)
rezultati_nalog = izracunaj_nalog(naloge)
konec = izracunaj_izpite(izpiti, rezultati_nalog)
pprint.pprint(konec)
drevo = collections.defaultdict(list)
def druzina():
    for vrstica in open("family.txt","rt"):
        oce, otrok = vrstica.split()
        if oce not in drevo:
            drevo[oce] = []
        drevo[oce].append(otrok)
    return drevo
d = druzina()
pprint.pprint(drevo)

def children(drevo, name):
    if name in drevo:
        return drevo[name]
    else:
        return []
print(children(drevo, "alice"))

def grandchildren(drevo, name):
    vnuk = []
    for otrok in children(drevo, name):
        vnuk.extend(drevo[otrok])
    return vnuk
print(grandchildren(drevo, "renee"))

def grandchildren1(drevo, name):
    vnuk = []
    for otrok in children(drevo, name):
        for otrok in children(drevo, otrok):
            vnuk.append(otrok)
    return vnuk
print(grandchildren1(drevo, "renee"))

name = "alice"
def successors(drevo, name):
    names = []
    for otrok in children(drevo, name):
        names.append(otrok)
        names.extend(successors(drevo, otrok))
    return names
print(successors(drevo, name))

stavek = "in to in ono smo mi"
nasledniki = collections.defaultdict(list)
stavek = stavek.split()
for s1, s2 in zip(stavek, stavek[1:]):
    nasledniki[s1].append(s2)
print(nasledniki)

stavek = "in to in ono smo mi"
nasledniki = {}
stavek = stavek.split()
for s1, s2 in zip(stavek, stavek[1:]):
    if s1 not in nasledniki:
        nasledniki[s1] = []
        nasledniki[s1].append(s2)
    else:
        nasledniki[s1].append(s2)

stavek = "Napisi funkcijo skritopis(s), ki (kar predobro) skrije besedilo tako, " \
         "da vsako besedo zamenja z njeno prvo crko."

beseda = re.sub("\w+",lambda mo: mo.group()[0], stavek)
print(beseda)

def skriptopis(stavek):
    if not stavek:
        return stavek
    beseda = stavek[0]
    for i in range(1,len(stavek)):
        if not str(stavek[i]).isalpha() or not stavek[i-1].isalpha():
            beseda += stavek[i]
    return beseda
print(skriptopis(stavek))

tekmovalci = ['Alice', 'Bob', 'Tom', 'Judy']
def turnir(tekmovalci):
    while len(tekmovalci) > 1:
        noviTekm = []
        for i in range(1, len(tekmovalci), 2):
            if (len(tekmovalci[i]) + len(tekmovalci[i-1])) % 2 == 0:
                noviTekm.append(tekmovalci[i-1])
            else:
                noviTekm.append(tekmovalci[i])
        tekmovalci = noviTekm
    return tekmovalci
t = turnir(tekmovalci)
print(t)

s1 = "Po-et tvoj nov Slo-ven-cem ve-nec vi-je,  " \
     "z pet-najst so-ne-tov ti ta-ko ga sple-ta, " \
     "de Ma-gi-stra-le, pe-sem tri-krat pe-ta, " \
     "vseh dru-gih sku-paj ve-ze ha-rmo-ni-je."

s2= "Ti si ziv-lje-nja moj-ga ma-gi-stra-le, " \
    "gla-sil se z nje-ga, ko ne bo vec me-ne, " \
    "ran mo-jih bo spo-min in tvo-je hva-le."

s3 = "To ni pe-sem, " \
     "so le ne-ke pi-sa-ri-je, " \
     "kar brez ri-me, " \
     "(ce se kam ne skri-je)."

def rime(s):
    besede = {}
    rima =""
    for vrstice in s.split("\n"):
        zadnjaBeseda = vrstice.split()[-1]
        zlog = zadnjaBeseda.split("-")[-1].strip(".!,?)")
        if zlog not in besede:
            besede[zlog] ="ABCEDEFGHIJKL"[len(besede)]
        rima +=besede[zlog]
    return rima
print(rime(s3))

def valid(isbn):
    check_digit = '0123456789X'[sum(i * int(d) for i, d in zip(range(1, 10), isbn)) % 11]
    print(check_digit)
    return len(isbn) == 10 and isbn[-1] == check_digit
print(valid('0306406152'), valid('0553382578'), valid('0553293370'), valid('912115628X'))
print(valid('03064061522'), valid('1553382578'), valid('91211562811'))
ena = {"ena", "dva", "tri"}
dva = {"ena"}
rez = ena.difference(dva)
print(rez)