from System import*
from Scene import*
from Hero import*

class Menu(MenuObject):
    def __init__(self, scene):
        MenuObject.__init__(self, scene)

        self.scene = scene
        self.engine = self.scene.engine

        self.buttons = []

