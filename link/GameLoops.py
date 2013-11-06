import pygame, sys
import GameClock as gc

class Game:
    def __init__(self):
        pygame.init()
        self.running=True
        self.FPS=25
        self.skipTicks=1000/self.FPS
        self.nextGameTick=pygame.time.get_ticks()

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.nextGameTick+=self.skipTicks
            sleep=self.nextGameTick-pygame.time.get_ticks()
            if sleep >= 0:
                pygame.time.delay(sleep)