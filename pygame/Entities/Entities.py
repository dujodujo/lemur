from Hero import Hero
from Enemy import Enemy

class Entities(object):
    def __init__(self):
        self.entities = {}

    def add_entity(self, entity):
        if entity.name not in self.entities:
            self.entities[entity.name] = entity

    def remove_entity(self, entity):
        if entity.name in self.entities:
            self.entities[entity.name].pop()

    def heroes(self):
        return [entity for entity in self.entities.values() if isinstance(entity, Hero)]

    def enemies(self):
        return [entity for entity in self.entities if isinstance(entity, Enemy)]

    def all_entities(self):
        return [entity for entity in self.entities.values()]