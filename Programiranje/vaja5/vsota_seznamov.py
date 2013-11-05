ss = [[2, 4, 1], [3, 1], [], [8, 2], [1, 1, 1, 1]]
def vsota_seznama(ss):
    xs= []
    for s in ss:
        xs.append(sum(s))
    return xs
print(vsota_seznama(ss))
