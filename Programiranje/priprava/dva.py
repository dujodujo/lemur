#
#imeDat = "C:\\Users\\dujo\\PycharmProjects\\Programiranje\\priprava\\emso.txt"
#
#def histogramDni(imeDat):
#    rojstni = {}
#    for line in open(imeDat, "rt"):
#        emso = line.strip()
#        datum = emso[:4]
#        if not datum in rojstni.keys():
#            rojstni[datum] = 1
#        else:
#            rojstni[datum] += 1
#
#    for r in rojstni:
#        print("{}.{:>2}. {}".format(int(r[:2]), int(r[2:4]), rojstni[r]))
#
#histogramDni(imeDat)

#meseci = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#
#def danLetu(d, m):
#    if m == 1:
#        return d
#    else:
#        return sum(meseci[:m-1]) + d
#print(danLetu(26, 12))

#osebe = [("Ana", "2401983505012"), ("Berta", "1509980505132"), ("Cilka",
#"0203001505333"), ("Dani", "1005983505333")]

#def uredi(osebe):
#    xs = []
#    for oseba in osebe:
#        if oseba[1][4] == "9":
#            datum = "1"+ oseba[1][4:7] + oseba[1][2:4] + oseba[1][0:2]
#        else:
#            datum = "2"+ oseba[1][4:7] + oseba[1][2:4] + oseba[1][0:2]
#        xs.append((datum, oseba[0]))
#    xs.sort()
#    return [ime for datum, ime in xs]

#print(uredi(osebe))
#besede = ["RABarbara", "izpit", "zmagA"]

#def najRaz(besede):
#    xs = []
#    najCrk = 0
#    najBes = ""
#    for beseda in besede:
#        crka = len(set(beseda.lower()))
#        if crka > najCrk:
#            najCrk = crka
#            najBes = beseda
#    return najBes
#print("".join(najRaz(besede)))

#def numerologija(ime):
#    vsota = 0
#    for i in ime.upper():
#        vsota += (ord(i) - 64)
#    while vsota > 9:
#        vsota = str(vsota)
#        vs = 0
#        for v in vsota:
#            vs += int(v)
#        vsota = vs
#    return vsota
#print(numerologija("Berta"))

delnica = [1, -2, -4, 1, 2, -1, 3, 4, -2, 1, -5, -5]

#def posrednik(delnica):
#    najDobicek = -1
#    for od in range(len(delnica)):
#        for do in range(od, 12):
#            dobicek = sum(delnica[od:do])
#            if dobicek > najDobicek:
#                najDobicek = dobicek
#                najOd, najDo = od, do
#    return najOd, najDo
#print(posrednik(delnica))

#1, 2, 4, 8, 16
tekmovalci = ['Alice', 'Bob', 'Tom', 'Judy']

def turnir(tekmovalci):
    while len(tekmovalci) > 1:
        noviKrog = []
        for i in range(0, len(tekmovalci), 2):
            if (len(tekmovalci[i]) + len(tekmovalci[i+1])) % 2 == 0:
                noviKrog.append(tekmovalci[i])
            else:
                noviKrog.append(tekmovalci[i+1])
        tekmovalci = noviKrog
    return tekmovalci[0]
print(turnir(tekmovalci))

