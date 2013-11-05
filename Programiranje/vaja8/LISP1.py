xs = [5, 4, 6, 7, 1]

def convert(xs):
    if not xs:
        return ()
    else:
        return xs[0],convert(xs[1:])
con = convert(xs)
print(convert(xs))
con = (5, (4, (6, (7, (1, ())))))

def lenConvert(con):
    vsota = 0
    for c in con:
        if isinstance(c,tuple):
            vsota +=lenConvert(c)
        else:
            vsota +=1
    return vsota
print(lenConvert(con))

def lenConvert1(con):
    if not con:
        return 0
    else:
        return 1 + lenConvert1(con[1])
print(lenConvert1(con))

con = (5, (4, (6, (7, (1, ())))))
def dup(con):
    if not con:
        return ()
    else:
        return con[0],(con[0],dup(con[1]))
print(dup(con))

