s = [True, False, True, False]
def komu_ni_jasno(s, i):
    if not s:
        return -1
    elif not s[0]:
        return i
    else:
        return komu_ni_jasno(s[1:], i+1)
print(komu_ni_jasno(s,3))