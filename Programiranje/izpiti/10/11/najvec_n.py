seznam = [1, 2, 3, 1, 1, 2, 1, 2, 3, 3, 2, 4, 5, 3, 1]
n = 3

ns = []
for s in seznam:
    if ns.count(s) < 3:
        ns.append(s)
print(ns)