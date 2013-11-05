


def podana(podana_beseda):
    besede = ["ana", "berta", "cilka", "dani", "ema", "fanci", "greta", "hilda"]
    maksimum = 0
    iskana = ""
    rez = []

    for beseda in besede:
        mnozice_ime = set()
        mnozice_beseda = set()
        for a in podana_beseda:
            mnozice_beseda.add(a)
        for b in beseda:
            mnozice_ime.add(b)
        rezultat = len(mnozice_beseda.intersection(mnozice_ime))
        if rezultat > maksimum:
            maksimum, iskana= rezultat, beseda
    return iskana
#podana_beseda = "krava"
#podana_beseda = "merjasec"
podana_beseda = "zmaj"
rezultat = podana(podana_beseda)
print(rezultat)