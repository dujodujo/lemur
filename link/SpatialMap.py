import math
import pygame

def pixels(v, value):
    return int(v/value)

class SpatialMap:
    def __init__(self, size):
        self.data={}
        self.size=size

    def add(self, entity):
        for y in range(pixels(entity.rect.top, self.size),
            pixels(entity.rect.bottom, self.size)):
            for x in range(pixels(entity.rect.left, self.size),
                pixels(entity.rect.right, self.size)):
                self.data.setdefault((x,y), set()).add(entity)

    def __add(self, entity):
        self.data.setdefault((entity.rect.left/self.size, entity.rect.top/self.size), set()).add('entity')
        self.data.setdefault((entity.rect.left/self.size, entity.rect.bottom/self.size), set()).add('entity')
        self.data.setdefault((entity.rect.width/self.size, entity.rect.top/self.size), set()).add('entity')
        self.data.setdefault((entity.rect.width/self.size, entity.rect.bottom/self.size), set()).add('entity')

    def remove(self, object):
        for y in range(pixels(object.rect.top, self.size),
            pixels(object.rect.bottom, self.size)):
            for x in range(pixels(object.rect.left, self.size),
                pixels(object.rect.right, self.size)):
                self.data[(x,y)].remove(object)

    def __remove(self, entity):
        self.data[(entity.rect.left/self.size, entity.rect.top/self.size)].remove('entity')
        self.data[(entity.rect.left/self.size, entity.rect.bottom/self.size)].remove('entity')
        self.data[(entity.rect.width/self.size, entity.rect.top/self.size)].remove('entity')
        self.data[(entity.rect.width/self.size, entity.rect.bottom/self.size)].remove('entity')

    def hits(self, entity):
        entities=set()
        for y in range(pixels(entity.rect.top, self.size),
            pixels(entity.rect.bottom, self.size)):
            for x in range(pixels(entity.rect.left, self.size),
                pixels(entity.rect.right, self.size)):
                for ent in self.data.get((x,y), []):
                    if not ent in entities:
                        entities.add(ent)
                    if entity.rect.colliderect(ent.rect):
                        yield ent