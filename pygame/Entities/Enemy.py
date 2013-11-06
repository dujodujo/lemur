from System import*
from Entity import Entity
from Animation import Animation

import os

class Enemy(Entity):
    def __init__(self, sprites, animations, world_i, name):
        Entity.__init__(self, sprites, animations, world_i, name)

        self.position = (450, 300)
        self.gold = 10
        self.exp = 10

    def set_current_sprite(self, sprite):
        print(self.sprites, sprite, 'sprite')
        self.current_sprite = self.sprites[sprite]
        self.current_sprite.set_position(self.position[0], self.position[1])

    def set_king_rool_animation(self):
        print('aaa')
        self.animation.set_animation(self.animations['king_rool'])
        self.set_current_sprite('king_rool')

    def draw(self):
        self.animation.draw_animation(self.current_sprite)