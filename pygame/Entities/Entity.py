import os
from collections import defaultdict
from Animation import*

class ChangeListener(object):
    def __init__(self):
        self.listeners = []

    def call_listeners(self):
        self.event_call =+1
        for listener in self.listeners:
            if listener:
                listener()
        self.event_call -=1

        if self.event_call == 0:
            self.listeners[:] = [listener for listener in self.listeners if listener]

    def add_change_listener(self, listener):
        if listener not in self.listeners:
            self.listeners.append(listener)

    def remove_change_listener(self, listener):
        self.listeners[self.listeners.index(listener)] = None

    def clear_change_listeners(self):
        self.listeners = []

    def check_listeners(self):
        self.call_listeners()

class EntityObject(ChangeListener):
    next_i = 1
    entity_i = 1
    world_entities = defaultdict(list)
    all_entities = defaultdict(list)

    def __init__(self, world_i=None):
        ChangeListener.__init__(self)
        self.world_i = world_i if world_i is not None else EntityObject.next_i
        #EntityObject.world_entities[self.world_i].append(self)

        #self.entity_i = EntityObject.entity_i
        #EntityObject.all_entities[self.entity_i].append(self)
        #EntityObject.entity_i +=1

    def save(self, db):
        pass

    def load(self, db):
        pass

class Entity(EntityObject):
    def __init__(self, sprites, animations, world_i, name):
        EntityObject.__init__(self, world_i)

        self.sprites = sprites
        self.animations = animations
        self.command_sprites = [key for key in self.animations.keys()]
        self.animation = Animation()
        self.name = name
        self.target = None
        self.position = (0, 0)

    def turn_end(self): pass

    def turn_start(self): pass


"""
    @classmethod
    def get_entity(cls, i):
        return EntityObject.world_entities[i]

    @classmethod
    def get_world_entities(cls, i):
        return EntityObject.world_entities[i]

    @classmethod
    def get_all_entities(cls):
        return EntityObject.all_entities

    @classmethod
    def reset(cls):
        EntityObject.entity_i = 1
        EntityObject.next_i = 1
        EntityObject.all_entities.clear()
        EntityObject.world_entities.clear()
"""
