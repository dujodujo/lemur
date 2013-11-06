import sys, pygame
import Game as game
import InputEvent as ie
import Box as b
import GameClock as gc
import os

class TitleScreen:
    def __init__(self):
        self.running=True
        self.boxes=[]
        self.initBoxes()
        size=800, 600

        while self.running:
            self.screen=pygame.display.set_mode(size)
            pygame.display.set_caption("Kaboom")
            for box in self.boxes:
                box.xymove(size[0]/3, size[1]/3)
                self.draw(box.surface(), box.position())

            while self.running:
                for event in ie.InputEvent.getEvents():
                    if ie.InputEvent.isWindowClosing(event):
                        self.quit()
                    elif ie.InputEvent.isKeyboardPressed(event):
                        if ie.InputEvent.getKeyboardKey(event)==pygame.K_ESCAPE:
                            self.quit()
                    if ie.InputEvent.isMouseDown(event):
                        for box in self.boxes:
                            if box.getName()=="SinglePlayer" and self.withinBoundary(box):
                                self.startGame()
                            elif box.getName()=="Exit" and self.withinBoundary(box):
                                self.quit()

    def initBoxes(self):
        self.boxesImage=pygame.image.load(os.getcwd() + "\\data\\sprites\\boxes.png")
        boxes=[[pygame.Rect(0, 0, 260, 80), "SinglePlayer"],
               [pygame.Rect(0, 80, 260, 80), "HighScores"],
               [pygame.Rect(0, 160, 260, 80), "Exit"]]
        for box in boxes:
            self.boxes.append(b.Button(box[0], box[1], self.boxesImage))

    def quit(self):
        pygame.quit()
        sys.exit()

    def withinBoundary(self, box):
        return box.inside(pygame.mouse.get_pos())

    def startGame(self):
        game.Game()

    def draw(self, image, position):
        self.screen.blit(image, position)
        pygame.mouse.set_visible(True)
        pygame.display.flip()

if __name__=="__main__":
    t=TitleScreen()