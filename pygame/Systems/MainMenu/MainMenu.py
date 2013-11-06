from System import*
from Scene import*

from MenuObject import MenuObject

class MainMenu(Scene):
    def __init__(self, engine):
        Scene.__init__(self)
        self.engine = engine

        self.menu = MenuObject(self, position = (150, 150))

        self.background = ImageObject(Texture("main_background.png"))
        self.background.set_position(self.engine.width/2, self.engine.height/2)
        self.background.set_scale(self.engine.width, self.engine.height, pixels = True)

    def run(self): pass

    def draw(self,):
        self.background.draw()