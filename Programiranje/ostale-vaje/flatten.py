l = [[[1,2]],[3,4],[5,6]]

def flaten(l):
    out = []
    for x in l:
        if isinstance(x,list):
            out.extend(flaten(x))
            print(out)
        else:
            out.append(x)
    return out
print(flaten(l))


