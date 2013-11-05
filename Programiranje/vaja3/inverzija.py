"""
Napišite program, ki v seznamu xs prešteje število parov indeksov i in j,
tako da velja i < j in xs[i] > xs[j].
V seznamu xs =  so štirje taki pari:
par (1, 2), ker 1 < 2 in xs[1] = 4 > xs[2] = 3
par (1, 4), ker 1 < 4 in xs[1] = 4 > xs[4] = 2
par (2, 4), ker 2 < 4 in xs[2] = 3 > xs[4] = 2
par (3, 4), ker 3 < 4 in xs[3] = 5 > xs[4] = 2
"""
xs = [1, 4, 3, 5, 2]

inverzija = 0
for i in range(len(xs)):
    for j in range(i):
        if xs[j] > xs[i]:
            inverzija +=1
print(inverzija)