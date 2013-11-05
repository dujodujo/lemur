import os
slike = []

def decode_png(fname):
    slika = open(fname,"rb")
    slika.read(16)
    s = slika.read(8)
    sirina = s[0]*0x1000000 + s[1]*0x10000 + s[2]*0x100 + s[3]
    visina = s[4]*0x1000000 + s[5]*0x10000 + s[6]*0x100 + s[7]
    speks = (fname, sirina, visina)
    return(speks)

def decode_gif(fname):
    slika = open(fname,"rb")
    slika.read(6)
    s = slika.read(4)
    sirina = s[0] + s[1]*0x100
    visina = s[2] + s[3]*0x100
    speks = (fname, sirina, visina)
    return(speks)

for fname in os.listdir("."):
    ext = os.path.splitext(fname)[1]
    if ext == ".png":
        decode_png(fname)
        slike.append(decode_png(fname))
    elif ext == ".gif":
        decode_gif(fname)
        slike.append(decode_gif(fname))
bla = open("slike.txt","wt",encoding="utf-8")
for ime, sirina, velikost in slike:
    bla.write("{:<50} {:>8} x {}\n".format(ime,sirina,velikost))
    print("{:<50} {:>8} x {}".format(ime,sirina,velikost))