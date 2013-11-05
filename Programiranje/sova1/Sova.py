msg = """Dragi Ahmed,

kako si kaj? Upam, da so otroci ze zdravi.

Mustafa, Osama in jaz smo se sli danes malo razgledat in
kaze kar dobro. Abdulah pa ni mogel zraven, je sel v Pesavar
prodat se tri kamele. Osama sicer pravi, da se mu to pred
zimo ne splaca, ampak saj ves, kaksen je Abdulah. Harun in
on, nic jima ne dopoves, se Osama ne. Jibril me klice,
moram iti; oglasi se kaj na Skype!

tvoj Husein

PS, oprosti za sumnike - rashmeD nas je preprical, da zdaj
uporabljamo Python.
"""
import re
#re.sub(pattern, replace, string[, count, flags=0])
msg = re.sub("[^\w ]", " ", msg)

imena = []
for ime in imena:
    ime = 
