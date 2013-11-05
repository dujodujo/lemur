import collections

#vaja5
#cena = []
#articles = dict()
#for line in open("cene.txt","rt",encoding="utf-8"):
#    file = line.strip().split()
#    code = file[0]
#    price = file[1]
#    articles[code] = float(price)
#for line in open("artikli.txt","rt",encoding="utf-8"):
#    file = line.strip().split()
#    code = file[0]
#    quantity = file[1]
#    if code in articles:
#        cena.append(articles[code]*float(quantity))
#        print(cena)
#print(sum(cena))



a = 12
b = 6
def gcd(a,b):
    maks = 0
    n = 0
    if n < 3:
        for i in range(1,b+1):
            if a % i == 0:
                maks = i
        n +=1
        gcd()

    print(maks)

gcd(a,b)