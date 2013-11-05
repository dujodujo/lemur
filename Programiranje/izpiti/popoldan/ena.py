
#def danVletu(dan, mesec):
#    meseci = {1:31, 2:29, 3:31, 4:30, 5:31, 6:31, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
#    zapDan = 0
#    for i in range(1,mesec):
#        zapDan += meseci[i]
#    return zapDan + dan
#rez = danVletu(10,2)
#print(rez)

def danVletu(dan, mesec):
    dnevi = [31,29,31,30,31,31,31,31,30,31,30,31]
    return sum(dnevi[:mesec-1]) + dan
rez = danVletu(10,2)
print(rez)
