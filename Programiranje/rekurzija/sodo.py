def sodo(x):
    if x==0:
        return True
    else:
        return not sodo(x-1)
print(sodo(4))