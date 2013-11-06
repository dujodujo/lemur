import os

from Scene import*

class HeroStats:
    def __init__(self, scene, hero):
        self.scene = scene
        self.engine = self.scene.engine

        self.hero = hero
        self.position = (self.engine.width*0.05, self.engine.height*0.25)
        self.font = FontObject('default.ttf', size = 24)

        self.load_frame()
        self.load_bars()

        for bar in self.bars:
            bar.set_position(-500, 300)
            bar.set_scale(6, 1)

    def load_frame(self):
        scene_path = os.path.join('data', 'scenes', 'menusystem')
        self.frame = WindowObject(Texture(os.path.join(scene_path, 'window.png')),
            self.position[0], self.position[1])
        self.frame.set_position(self.position[0], self.position[1])
        self.frame.set_scale(4, 2)

    def draw_texts(self):
        self.engine.draw_text(self.font, 'HERO: %s' % self.hero.name,
            position = (self.position[0] + 188, self.position[1]+100))
        self.engine.draw_text(self.font, 'HP: %s' % self.hero.hp,
            position = (self.position[0] + 150, self.position[1]+150))
        self.engine.draw_text(self.font, 'EXP: %s' % self.hero.exp,
            position = (self.position[0] + 150, self.position[1]+200))

    def load_bars(self):
        self.bars = [
            BarObject(Texture(os.path.join('data', 'scenes', 'menusystem',
                'barbottom.png')), 600),
            BarObject(Texture(os.path.join('data', 'scenes', 'menusystem',
                'bartop.png')), 600)]
            #BarObject(Texture(os.path.join('data', 'scenes', 'menusystem',
            #    'expbar.png')))]

    def draw(self):
        self.frame.draw()
        self.draw_texts()

        for bar in self.bars:
            bar.draw()