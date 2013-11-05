import collections

studenti = collections.defaultdict(set)
predmeti = collections.defaultdict(set)
for student in open("podatki.txt","rt",encoding="utf-8"):
    vpisna, predmet, letnik, program, kraj = student.strip().split(",")
    if letnik == "3" and program == "VSS" and kraj == "LJ":
        studenti[vpisna].add(predmet)
        predmeti[predmet].add(vpisna)
print(studenti)
print(predmeti)


kode = {
"63701": 'Uvod v računalništvo',
"63702": 'Programiranje 1',
"63703": 'Računalniška arhitektura',
"63704": 'Matematika',
"63705": 'Diskretne strukture',
"63706": 'Programiranje 2',
"63707": 'Podatkovne baze',
"63708": 'Računalniške komunikacije',
"63709": 'Operacijski sistemi',
"63710": 'Osnove verjetnosti in statistike',
"63711": 'Algoritmi in podatkovne strukture 1',
"63712": 'Elektronsko in mobilno poslovanje',
"63713": 'Podatkovne baze 2',
"63714": 'Informacijski sistemi',
"63715": 'Grafično oblikovanje',
"63716": 'Komunikacijski protokoli in omrežna varnost',
"63717": 'Organizacija računalnikov',
"63718": 'Digitalna vezja',
"63719": 'Računalniška grafika',
"63720": 'Umetna inteligenca',
"63721": 'Uporabniški vmesniki',
"63722": 'Prevajalnik in navidezni stroji',
"63723": 'Algoritmi in podatkovne strukture 2',
"63724": 'Testiranje in kakovost',
"63725": 'Razvoj informacijskih sistemov',
"63726": 'Produkcija multimedijskih gradiv',
"63727": 'Spletne tehnologije',
"63728": 'Vhodno izhodne naprave',
"63729": 'Načrtovanje digitalnih naprav',
"63730": 'Odkrivanje zakonitosti iz podatkov',
"63731": 'Projektni praktikum',
"63732": 'Tehnologija programske opreme',
"63733": 'Strateško planiranje informatike',
"63734": 'Multimedijske tehnologije',
"63735": 'Vzporedni in porazdeljeni sistemi in algoritmi',
"63736": 'Sistemska programska oprema',
"63737": 'Procesna avtomatika',
"63738": 'Vgrajeni sistemi',
"63739": 'Robotika in računalniško zaznavanje',
"63740": 'Tehnologija iger in navidezna resničnost',
"63741": 'Odločitveni sistemi',
"63742": 'Numerične metode',
"63744": 'Digitalno procesiranje signalov',
"63746": 'Angleščina',
"63749": 'Računalništvo v praksi',
"63755": 'Projektni praktikum'}

#for koda, vpisne in predmeti.items():
#    print("{:60}: {}".format(kode[koda], len(vpisne)))

#najmanj = 1000
#for koda, vpisne in predmeti.items():
#    if len(vpisne) < najmanj:
#        najPredmet, najmanj = koda, len(vpisne)

#print("Najmanj študentov {} je izbralo predmet {}".format(najmanj,kode[najPredmet]))

unije = []
for koda1, vpisne1 in predmeti.items():
    for koda2, vpisne2 in predmeti.items():
        if koda1 < koda2:
            unije.append((len(vpisne1 | vpisne2),koda1,koda2))

print(unije[:-5])
unije.sort()
for studentov, koda1, koda2 in unije[:-5:-1]:
    print("{} IN {}: {}".format(kode[koda1], kode[koda2], studentov))
