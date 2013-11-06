import pygame
import random
import math
import Vector as v

class Star(pygame.sprite.Sprite):
    def __init__(self, position, angle, speed, size):
        self.sprite=pygame.sprite.Sprite.__init__(self)
        self.position=position
        self.angle=angle
        self.speed=speed.length()

    def draw(self, destPosition):
        destPosition.blit(self.sprite, self.position)

    def move(self):
        pass