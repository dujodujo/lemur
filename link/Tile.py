import pygame
import Entity as ent

class Tile(ent.Entity):
    def __init__(self, surface, rect, subFrame):
        ent.Entity.__init__(self, rect)
        self.subFrame=subFrame
        self.rect=rect
        self.surface=pygame.Surface.subsurface(surface, self.subFrame)

    def draw(self, screen):
        screen.blit(self.surface, self.rect)


width, height=(10,10)
#left, top, right, bottom
rec=pygame.Rect(0, 0, 10, 10)
rec[0],rec[1]
rec[0],rec[3]
rec[2],rec[1]
rec[2],rec[3]
