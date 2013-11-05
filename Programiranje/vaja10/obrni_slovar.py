slovar = {"key1":1,"key2":2,"key3":3}

def obrni(slovar):
    imenik = {}
    for a,b in slovar.items():
        imenik[b]=a
    return imenik
print("obrni",obrni(slovar))

def obrni_slovar(slovar):
    return  {v: k for k,v in slovar.items}
print("obrni drugic",obrni(slovar))