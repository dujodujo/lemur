import random
vnos = int(input("vnesi stevilo: "))
stevila = random.randint(0,100)
print(stevila)
poteze = 1;
while stevila != vnos:
    if (stevila < vnos):
        print("PREVELIKO")
    else:
        print("PREMAjHNO")
    poteze +=1
    vnos = int(input("vnesi stevilo: "))
printf("ZADETEK {}".format(poteze))

