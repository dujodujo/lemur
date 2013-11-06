import pygame
import MovingEntity as me
import Vector as vector
import SpriteAnimationSet as sas
import SpriteAnimation as sa

class Player(me.MovingEntity):
    def __init__(self, rect):
        me.MovingEntity.__init__(self, rect)

        self.spriteAnimationsSet=sas.SpriteAnimationSet()
        self.animations=self.spriteAnimationsSet.animations
        self.animation=self.animations['walking']

    def draw(self, screen):
        screen.blit(self.animation.getSurface(), self.rect.topleft)
        pygame.display.flip()

    def update(self):
        self.animation.update()
        self.updateMovement()