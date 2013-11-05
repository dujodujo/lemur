
n = str(input("vpisi niz: "))
"""
if n == n[::-1]:
    print("je palindrom")
else:
    print("ni palindrom")
"""

i = 0
j = len(n) - 1
while i < j:
    if n[i] != n[i]:
        print("ni pali")
    i+=1
    j-=1

