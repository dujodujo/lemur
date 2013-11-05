
def starost (emsoSt):
    emsoSt = emsoSt[:7]
    dan_rojstvo  = int(emsoSt[:2])
    mesec_rojstvo = int(emsoSt[2:4])
    leto_rojstvo = 1000 + int(emsoSt[4:])

    if leto_rojstvo < 1900:
        leto_rojstvo += 1000
    st = 2009 - leto_rojstvo
    if mesec_rojstvo == 1 and 26 > dan_rojstvo:
        st += 1
    return st

emsoSt = "20029711500123"
rez = starost(emsoSt)
print(rez)