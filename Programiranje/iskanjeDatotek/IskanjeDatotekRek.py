import collections, os, pprint
cwd = ".\\dn8_tree"

def preisci(direktorij):
    datoteke = collections.defaultdict(set)
    preisci0(direktorij,datoteke)
    return datoteke

def preisci0(direktorij, datoteke):
    for name in os.listdir(direktorij):
        full_name = os.path.join(direktorij,name)
        if os.path.isdir(full_name):
            preisci0(full_name,datoteke)
        else:
            datoteke[name].add(direktorij)

datoteke = preisci(cwd)
pprint.pprint(datoteke)
