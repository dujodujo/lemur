import time
import pygame.time
import sys
import Vector as vec

class GameClock:
    def __init__(self,time=pygame.time.get_ticks, fps=24,
            updateCallback=None, drawCallback=None):
        self.time=time
        self.fps=fps
        self.step=1000/self.fps
        self.frameSkip=10
        self.nextGameTick=self.time()

        self.updateCallback=updateCallback
        self.drawCallback=drawCallback

    def interpolation(self):
        interp=(self.time()+self.step-self.nextGameTick)/self.step
        return interp if 0 < interp < 1 else 1

    def tick(self):
        loops=0
        while self.time() > self.nextGameTick and loops < self.frameSkip:
            self.nextGameTick+=self.step
            loops+=1
            self.updateCallback(self.step)
        self.drawCallback(self.interpolation())