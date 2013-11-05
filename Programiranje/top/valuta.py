import urllib.request
import pprint

tecaji = {}
socket = urllib.request.urlopen("http://www.nlb.si/?a=tecajnica&type=individuals&format=txt")
for line in socket:
    line = line.decode("utf-8")
    if line.startswith("001"):
        podatki = line.split()
        valuta = podatki[5]
        tecaj = float(podatki[6].replace(",","."))
        tecaji[valuta] = tecaj
pprint.pprint((tecaji))