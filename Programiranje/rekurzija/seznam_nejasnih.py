s = [True, False,True, False]

def za_1_vec(s):
    print(s)
    t = []
    for e in s:
        t.append(e+1)
    return t

def katerim_ni_jasno(s):
    if not s:
        return []
    else:
        nejasni = katerim_ni_jasno(s[1:]) #komu za mano ni jasno?
        print(nejasni)
        nejasni = za_1_vec(nejasni)       #povečam številke za 1
        print(nejasni)
        if not s[0]:                      #če tudi meni ni jasno, dodam še sebe (kot da sem v 1. vrsti)
            nejasni.append(1)
    return nejasni
print(katerim_ni_jasno(s))

#def katerim_ni_jasno(s, i):
#    if not s:
#        return []
#    else:
#        nejasni = katerim_ni_jasno(s[1:], i+1)
#        if not s[0]:
#            nejasni.append(i)
#        return nejasni
#print(katerim_ni_jasno(s,1))