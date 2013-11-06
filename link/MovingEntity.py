import Entity as ent
import Vector as vec
import pygame, math

class MovingEntity(ent.Entity):
    def __init__(self, rect):
        ent.Entity.__init__(self, rect)
        self.speed=20
        self.target=None

    def notifyPositionChanged(self, target):
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

    def updateMovement(self):
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
