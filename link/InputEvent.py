import pygame

class InputEvent:
    @classmethod
    def getEvents(cls):
        return pygame.event.get()

    @classmethod
    def isWindowClosing(cls, event):
        return event.type==pygame.QUIT

    @classmethod
    def isKeyboardPressed(cls, event):
        return event.type==pygame.KEYDOWN

    @classmethod
    def isKeyBoardReleased(cls, event):
        return event.type==pygame.KEYUP

    @classmethod
    def getKeyboardKey(cls, event):
        return event.key

    @classmethod
    def isMouseDown(cls, event):
        return event.type==pygame.MOUSEBUTTONDOWN

    @classmethod
    def getMousePosition(cls):
        return pygame.mouse.get_pos()