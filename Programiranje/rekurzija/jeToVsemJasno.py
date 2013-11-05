s = [True, True, True, True]
#def jasno(s):
#    if len(s) == 0:
##   if not s:
#        return True
#    else:
#        return s[0] and jasno(s[1:])

def jasno(s):
    return not s or s[0] and jasno(s[1:])
print(jasno(s))

