l = [5, 4, -7, 2, 9, -3, -4, -11, 7]

min = 0
for i in l:
    if abs(i) > abs(min):
        min = i
print(min)