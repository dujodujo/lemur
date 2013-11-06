import pygame

class Button(pygame.sprite.Sprite):
    def __init__(self, rect, name, image):
        self.sprite=pygame.sprite.Sprite.__init__(self)
        self.rect=pygame.Rect(rect.left, rect.top, rect.width, rect.height)
        self.image=pygame.Surface.subsurface(image, rect)
        self.name=name

    def inside(self, point):
        if self.rect.collidepoint(point[0], point[1]):
            return True
        return False

    def getName(self):
        return self.name

    def position(self):
        return self.rect.topleft

    def surface(self):
        return self.image

    def xmove(self,x):
        self.xymove(x,0)

    def ymove(self,y):
        self.xymove(0,y)

    def xymove(self, x, y):
        self.rect.move_ip(x,y)
