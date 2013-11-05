#v1
#print(sum([x**2 for x in range(1,101)]))

#v2
#print(sum([x**2 for x in range(101) if str(x)[::-1] == str(x)]))

#v3
#niz = "komar"
#stevilo = "23401"
#print("".join([(niz[int(i)]) for i in stevilo]))

#v4
#xs = []
##print(sum([x for x in xs])/len(xs))
#try:
#    print(sum([x for x in xs])/len(xs))
#except ZeroDivisionError:
#    print("division by zero is not allowed")

#def valid(isbn):
#    valid_list = []
#    for num in isbn:
#        s = sum([int(x)*y for x, y in zip(num, reversed(range(1,11)))])
#        if s % 11 == 0:
#            valid_list.append(s)
#    return valid_list

#'912115628X'
#v = valid(('0306406152', '0553382578',912115628X))
#print(v)


