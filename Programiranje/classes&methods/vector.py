import collections

class WordDict():
    def __init__(self,v):
        self.visine = dict(v)

    def __getitem__(self, key):
        k = key.lower()
        return self.visine[k][1]

    def __setitem__(self, key, value):
        k = key.lower()
        self.visine[k] = (key, value)

    def keys(self):
        return self.visine.keys()

    def vaues(self):
        return self.visine.values()

    def items(self):
        return self.visine.items()

    def __str__(self):
        items = ", ".join([("{}: {}".format(k,v)) for k,v in self.visine.items()])
        return "{"+ items +"}"

    __repr__ = __str__

velikost = WordDict([("Ana",160),("Beti",150)])
velikost["aNa"] = 120
print(velikost["AnA"])
print(velikost.items())