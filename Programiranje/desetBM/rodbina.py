def ustvari_rodbinslo_drevo(trodbina):
    rodbina = {}
    for vrstica in open(trodbina,"rt"):
        stars, otrok = vrstica.split()
        if stars not in rodbina:
            rodbina[stars] = [otrok]
        else:
            rodbina[stars].append(otrok)
    return rodbina

def je_stars(rodbina,oce,otrok):
    if otrok in rodbina[oce]:
        return True
    return False

def je_potomec(rodbina,oce,oseba):
    if oseba in rodbina[oce]:
        return "je potomec"
    else:
        for otrok in rodbina[oce]:
            oce = otrok
            for otroci in rodbina[oce]:
                je_potomec(rodbina,oce,otroci)


rodbina = ustvari_rodbinslo_drevo("rodbina.txt")
rodbina = {"Sid":["Bob"],"Bob":["Tom"],"Tom":["Ken"],"Ken":["Suzana"]}
print(je_potomec(rodbina,"Sid","Suzana"))


