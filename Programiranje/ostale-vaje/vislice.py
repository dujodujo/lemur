import pprint
from random import*

def get_char_position(word,letter):
    return [i for i,w in enumerate(word) if w == letter]

def have_all_chars(word,chars):
    prazna = set()
    for w in word:
        prazna.add(w)
    kontrola = prazna.intersection(chars)
    if prazna != kontrola:
        return False
    return True

def have_all_chars(word,chars):
    return set(word) <= chars

def show_chars(words,chars):
    str=""
    for w in words:
        if w in chars:
            str += w
        else:
            str +="."
    return str

def show_chars(words,chars):
    return "".join((w if w in chars else ".") for w in words)

def get_rand_samostalnik():
    samostalniki = open("samostalniki.txt","rt").read().strip().split()
    samostalnik = samostalniki[randrange(0,len(samostalniki))]
    return samostalnik

def vislice():
    zivljenja = 6
    izbira_crk = set()
    samostalnik = get_rand_samostalnik()
    print(samostalnik)
    print(show_chars(samostalnik,izbira_crk),zivljenja)
    while zivljenja:
        guess = (input("-->"))
        guess = guess.upper()
        print(guess)

        izbira_crk.add(guess)

        if not get_char_position(samostalnik,guess) :
            print(show_chars(samostalnik,izbira_crk),zivljenja)
            if have_all_chars(samostalnik,izbira_crk):
                return print("BRAVO")
        else:
            zivljenja -=1
            print(show_chars(samostalnik,izbira_crk),zivljenja)
    konec_vislic = "Konec, iskana beseda je " + samostalnik
    return print(konec_vislic)
vislice()

