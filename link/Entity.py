import pygame, Config
import Vector as vec

class Entity(pygame.sprite.Sprite):
    def __init__(self, rect):
        pygame.sprite.Sprite.__init__(self)
        self.rect=rect
        x, y, w, h=self.rect
        self.rect.center=((x+w)/2, (y+h)/2)