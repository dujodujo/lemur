slovar = {'danes', 'je', 'dan', 'za', 'programiranje', 'pravi', 'in'}
cs = 'dans je prvi dan za programiranje'

#ali je slovar množica ali dict?
def crkuj(cs,slovar):
    css = set()
    cs = cs.split()
    for c in cs:
        css.add(c)
    brez = css.difference(slovar)
    return brez
print(crkuj(cs,slovar))


#set()?? zakaj taka definicija
lis = []
slovar = {}
terka = ()
print(lis,slovar,terka)
