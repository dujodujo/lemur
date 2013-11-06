import Entity as entity
import Config as config
import pygame

class Bomb(entity.Entity):
    def __init__(self, imagePath, entityName, position):
        entity.Entity.__init__(self, entityName, position)
        self.imagePath=imagePath
        self.entiyName=entityName
        self.image=imagePath

    def tick(self):
        pass

    def updateBomb(self):
        if not self.tick():
            self.activateBomb()

    def activateBomb(self):
        self.explode()
        explosion=pygame.image.load_basic(config.Config.imagePath+"screen/explosion.png")
        self.blit(explosion, self.position)

    def explode(self):
        pass

    def updateTimer(self):
        pass