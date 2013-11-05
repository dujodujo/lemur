
import collections
fn = "family.txt"
def family_tree(fn):
    drevo = collections.defaultdict(list)
    for line in open(fn,"rt"):
        stars, otrok = line.split()
        drevo[stars].append(otrok)
    return drevo
tree = family_tree(fn)
print(tree)

def children(tree,name):
    if name:
        return tree[name]
c = children(tree,"renee")
print(c)

def grandchildren(tree,name):
    names = []
    for g in children(tree,name):
        for gc in children(tree,g):
            names.append(gc)
    return names
gcc = grandchildren(tree,"renee")
print(gcc)

#
def grandchildren(tree,name):
    names = []
    for child in children(tree,name):
        names.extend(children(tree,child))
    return names
gcc = grandchildren(tree,"renee")
print(gcc)

#rekurzivno
def successors(tree,name):
    names = []
    for child in children(tree,name):
        names.append(child)
        names.extend(successors(tree,child))
    return names
s = successors(tree,"sid")
print("*",s)
