class EntityNames():
    entities={}

    @classmethod
    def setattr(cls, key, value):
        cls.entities.setdefault(key, value)

    @classmethod
    def getattr(cls, item):
        return cls.entities[item]

    @classmethod
    def readEntities(cls):
        file=open("entityNames.txt", "r").readlines()
        if file:
            for line in file:
                key, value = line.split()
                cls.entities[key]=value