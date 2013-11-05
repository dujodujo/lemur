zap =  [2, 5, 7, 8, 4, 6, 9, 14, 7, 8, 3, 2, 5, 6]
zap = [2, 5, 7, 5, 8, 11, 12, 14]

def nepadajoc(zap):
    for i,j in zip(zap,zap[1:]):
        if i > j:
            return False
    return True
print(nepadajoc(zap))

def nepad_pod(zap):
    podzaporedje = []
    to = zap[:1]
    for i, j in zip(zap, zap[1:]):
        if i > j:
            podzaporedje.append(to)
            to = [j]
        else:
            to.append(j)
    podzaporedje.append(to)
    return podzaporedje
print(nepad_pod(zap))
