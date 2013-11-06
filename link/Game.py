import sys, pygame, os
import Player as p
import Board as board
import Vector as vector
import InputEvent as ie
import GameClock as gc

class Game:
    def __init__(self):
        self.running=True

        pygame.init()
        self.size=(800, 640)
        self.screen=pygame.display.set_mode(self.size)
        pygame.display.set_caption("Kaboom")
        self.initGame()

    def initGame(self):
        self.initPlayer()
        #self.initBoard()
        self.initBackGround()
        self.initClock()
        self.run()

    def initClock(self):
        #self.clock=gc.GameClock(time=pygame.time.get_ticks, fps=24,
        #    updateCallback=self.update, drawCallback=self.draw)
        self.clock=pygame.time.Clock()

    def initBoard(self):
        self.board=board.Board(1)

    def initPlayer(self):
        self.player=p.Player(pygame.Rect(100, 100, 24, 32))

    def initBackGround(self):
        background = os.getcwd() + "\\data\\"
        self.backgroundImage=pygame.image.load(background + 'background.png').convert()
        self.backgroundImage=pygame.transform.scale(self.backgroundImage, self.size)

    def run(self):
        while self.running:
            self.clock.tick(10)
            for event in ie.InputEvent.getEvents():
                if ie.InputEvent.isWindowClosing(event):
                    self.quit()
                elif ie.InputEvent.isKeyboardPressed(event):
                    if ie.InputEvent.getKeyboardKey(event)==pygame.K_ESCAPE:
                        self.quit()
                elif ie.InputEvent.isMouseDown(event):
                    self.notifyInput(ie.InputEvent.getMousePosition())

            self.draw()
            self.update()

    def notifyInput(self, event):
        self.player.notifyPositionChanged(event)

    def quit(self):
        pygame.quit()
        sys.exit()

    def drawBackground(self):
        self.screen.blit(self.backgroundImage, (0, 0))

    def draw(self):
        self.drawBackground()
        #self.board.draw(self.screen)
        self.player.draw(self.screen)
        pygame.display.flip()

    def update(self):
        self.player.update()
        pygame.display.update()