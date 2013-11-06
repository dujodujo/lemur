import math
import random

from System import*
from Scene import*

class SplashSystem(Scene):
    def __init__(self, engine):
        Scene.__init__(self)

        self.engine = engine
        self.camera = self.engine.viewport.camera
        self.width, self.height = self.engine.width, self.engine.height

        self.delay_intro = True
        self.delay_time = 25

        self.load_base_sprites()

    def load_base_sprites(self):
        self.background = ImageObject(Texture(self.random_background()))
        self.background.set_position(self.engine.width/2, self.engine.height/2)

        self.logo = ImageObject(Texture(Paths.LOGO_PATH))
        self.logo.set_position(self.engine.width/2, self.engine.height/2)

    def random_background(self):
        backgrounds = os.listdir(Paths.BACKGROUNDS_PATH)
        b = random.randrange(0, len(backgrounds))
        return os.path.join(Paths.BACKGROUNDS_PATH, backgrounds[b])

    def run(self):
        if self.delay_time > 0:
            self.delay_time -= 5
        else:
            self.delay_intro = False
            self.engine.viewport.push_scene("CreateHeroSystem")

    def draw(self):
        if self.delay_intro:
            self.background.draw()
            self.logo.draw()