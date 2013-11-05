ss = [[2, 4, 1], [3, 1], [], [8, 2], [1, 1, 1, 1]]
def max_seznam(ss):
    max = 0
    for s in range(len(ss)):
        if sum(ss[s-1]) > sum(ss[s]):
            max = ss[s-1]
    return max
print(max_seznam(ss))
