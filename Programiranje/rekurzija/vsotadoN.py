def vsota(y):
    if y == 0:
        return 0
    else:
        return(vsota(y-1) + y)
print(vsota(5))
