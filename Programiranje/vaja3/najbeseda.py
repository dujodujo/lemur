niz = "an ban pet podgan"
l = niz.split()
#for i in range(len(l)):
#    if l[i] > l[i-1]:
#       naj = l[i]
#print(naj)

naj = ""
for i in l:
    if i > naj:
        naj = i
print(naj)

