from System import*
from Constants import*

from ButtonObject import ButtonObject

class MenuObject(object):
    def __init__(self, scene, commands=None, position=(0, 0)):
        self.scene = scene
        self.engine = scene.engine

        self.commands = commands
        self.position = position

        if commands:
            self.buttons  = [ButtonObject(Texture(Paths.BTNS_PATH))
                for n in self.commands]
            for i, button in enumerate(self.buttons):
                button.set_position(self.position[0], self.position[1])
        self.window = WindowObject(Texture(Paths.WINDOW_PATH))

    def button_clicked(self, image):
        pass

    def draw(self):
        self.window.draw()
        if self.commands:
            for i, button in enumerate(self.buttons):
                button.draw()