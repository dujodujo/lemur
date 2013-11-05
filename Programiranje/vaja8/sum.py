xs = [1, [], [2, 3, [4]], 5]

def sum(xs):
    vsota = 0
    for x in xs:
        if isinstance(x,list):
            vsota+=sum(x)
        else:
            vsota+=x
    return vsota
print(sum(xs))
