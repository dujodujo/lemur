ly = ("CVIVS IN HOC RENOVATA LOCO PIA FVLGET IMAGO SIS CVSTOS POPVLI SANCTE IACOBE TVI")


def kronogram(ly):
    vrednosti = (1, 5, 10, 50, 100, 500, 1000)
    imena = ("I", "V", "X", "L", "C", "D", "M")
    vsota =0
    for y in ly:
        for ime, vrednost in zip(imena, vrednosti):
            if y in ime:
                vsota +=vrednost
    return vsota
print(kronogram(ly))


