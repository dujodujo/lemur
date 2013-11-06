import pygame, math
from pygame.locals import *
import Vector as  vec

class Sprite():
    def __init__(self):
        self.image=pygame.image.load("green.png").convert()
        self.rect=pygame.Rect(100, 100, 32, 32)
        x, y, w, h=self.rect
        self.speed=10
        self.direction=0
        self.target=None

    def notifyTarget(self, target):
        x,y=target
        self.target=vec.Vec2d(x,y)

    def get_direction(self):
        if self.target:
            position = vec.Vec2d(self.rect.centerx, self.rect.centery)
            self.distance = self.target - position
            direction = self.distance.normalize()
            return direction

    def distance_check(self):
        if self.distance:
            totalDistance = self.distance.x**2 + self.distance.y**2
            if totalDistance> self.speed**2:
                return True

    def update(self):
        self.direction = self.get_direction()
        if self.direction:
            if self.distance_check():
                x, y=self.rect.center
                x+=self.direction.x*self.speed
                y+=self.direction.y*self.speed
                self.rect.center=(x,y)
            else:
                self.rect.center=(self.target.x, self.target.y)
                self.target=None


def main():

    screen = pygame.display.set_mode((640,480))
    background_color = pygame.Surface(screen.get_size()).convert()
    background_color.fill((0,0,0))

    sprite = Sprite()
    clock = pygame.time.Clock()
    running = True

    while running:
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == MOUSEBUTTONDOWN:
                sprite.target = event.pos
                sprite.notifyTarget(sprite.target)
        screen.blit(background_color, (0,0))

        sprite.update()
        screen.blit(sprite.image, sprite.rect.topleft)

        pygame.display.flip()
    pygame.quit()

if __name__ == "__main__":
    main()

