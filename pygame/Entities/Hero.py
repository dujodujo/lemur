import os

from Entity import*
from System import*
from Animation import Animation
from Constants import*
from Inventory import*

class Hero(Entity):
    def __init__(self, sprites, animations, current_sprite, world_i, name):
        Entity.__init__(self, sprites, animations, world_i, name)
        self.position = (150, 300)

        self.current_sprite = current_sprite
        self.sprite = None
        self.command = None
        self.active = False

        self.inventory = Inventory(self.entity_i)

        self.add_hero_listeners()

    def save(self, db):
        super(Hero, self).save(db)
        db('INSERT INTO hero(rowid, name, x, y) VALUES(?, ?, ?, ?)',
            self.entity_i, self.name, self.position[0], self.position[1])

    def load(self, db):
        super(Hero, self).load(db)
        x=db('SELECT name, x, y FROM hero WHERE rowid=?', self.entity_i)[0]

    def init_hero_inventory(self, db):
        for item, amount in HERO_START.STARTING_ITEMS.iteritems():
            db('INSERT INTO inventory(rowid, item, amount) VALUES(?, ?, ?)',
            self.entity_i, item, amount)
            self.inventory.add_item(item, amount)

    def set_position(self, position):
        self.position = position
        self.current_sprite.set_position(self.position[0], self.position[1])

    def set_current_sprite(self, sprite):
        self.current_sprite = self.sprites[sprite]
        self.sprite = sprite
        self.current_sprite.set_position(self.position[0], self.position[1])

    def set_animation(self, sprite):
        self.animation.set_animation(self.animations[sprite])
        self.set_current_sprite(sprite)

    def start_level_up(self):
        return False

    def set_clickable(self):
        pass

    def add_hero_listeners(self):
        self.add_change_listener(self.check_health)
        self.add_change_listener(self.check_mana)

    def check_health(self):
        #print('health')
        pass

    def check_mana(self):
        #print('mana')
        pass

    def turn_start(self):
        self.command.execute(self)

    def turn_end(self):
        self.command.reset(self)
        self.command = None

    def draw(self):
        self.animation.draw_animation(self.current_sprite)