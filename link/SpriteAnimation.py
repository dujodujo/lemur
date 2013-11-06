import pygame
import GameClock as gc

class SpriteAnimation:
    def __init__(self, surface, frameDelay, directions, limited=True):
        self.surface=surface
        self.frameDelay=frameDelay
        self.directions=directions
        self.numFrames=len(self.directions[0])
        self.limited=limited
        self.reset()

    def update(self):
        pass

    def getSurface(self):
        return pygame.Surface.subsurface(self.surface, self.directions[0][self.currentFrame])

    def finished(self):
        if self.currentFrame < self.numFrames-1:
            self.currentFrame+=self.step
        else:
            if not self.limited:
                self.reset()
            else:
                self.stop()

    def stop(self):
        self.currentFrame=0
        self.playing=False

    def reset(self):
        self.currentFrame=0
        self.step=1
        self.timePassed=-1
        self.playing=True