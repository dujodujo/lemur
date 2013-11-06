import pygame
import GameClock as gc
import sys, time, os


class TestTime:
    def __init__(self):
        self.position=0

        self.clock=gc.GameClock(time=pygame.time.get_ticks, fps=25,
            updateCallback=self.update, drawCallback=self.draw)

    def run(self):
        running=True
        self.startTime=time.time()
        while running:
            self.clock.tick()
            self.update(dt=0)
            self.draw(interpolate=0)
            if self.position > 100:
                running=False
                endTime=time.time()-self.startTime
                print endTime


    def update(self, dt):
        self.position+=0.0004

    def draw(self, interpolate):
        pass

tt=TestTime()
tt.run()