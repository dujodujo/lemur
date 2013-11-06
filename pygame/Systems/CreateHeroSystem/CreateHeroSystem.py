from System import*
from Scene import*
from Entities.Hero import*
from CreateMenu import CreateMenu
from StatsMenu import StatsMenu

import json

class CreateHeroSystem(Scene):
    def __init__(self, engine):
        Scene.__init__(self)

        self.engine = engine
        self.width, self.height = self.engine.width, self.engine.height

        self.scene_path = os.path.join('data', 'scenes', 'creationsystem')

        self.background = ImageObject(Texture(os.path.join(self.scene_path, 'background.png')))
        self.background.set_scale(self.engine.width, self.engine.height, pixels = True)
        self.background.set_position(self.engine.width/2, self.engine.height/2)

        self.name_window = WindowObject(Texture(os.path.join(self.scene_path, 'window.png')))

        self.steps = ['StatsMenu', 'CreateMenu']
        self.step = self.steps[0]

        self.create_hero_menu = CreateMenu(self, self.scene_path)

        self.stats = ["Hit Points", "Strength", "Defense", "Agility", "Resistance"]
        self.create_stat_menu = StatsMenu(self, self.scene_path)

        self.max_stats_points = 25
        self.current_stats_points = 0
        self.points = [0 for n in self.stats]

    def create_hero(self, name):
        print(name)
        animations_path = os.path.join(Paths.ANIMATIONS_PATH, name + '_animations.txt')
        sprites_path = os.path.join(Paths.HERO_PATH, name, name + '_sprites.txt')
        hero_path = os.path.join(Paths.HERO_PATH, name)

        sprites, current_sprite = self.load_hero_sprites(sprites_path, hero_path, name)
        animations = self.load_hero_animations(animations_path, hero_path)

        hero = Hero(sprites, animations, current_sprite, Game.WORLD_ID, name)
        hero.save(self.engine.db)
        hero.init_hero_inventory(self.engine.db)
        hero.inventory.load(self.engine.db)
        self.engine.entities.add_entity(hero)

    def load_hero_sprites(self, sprite_path, hero_path, name):
        sprites = dict()
        for line in open(sprite_path).readlines():
            image, frame_x = line.rstrip('\n').split(',')
            sprites[image.split('.png')[0]] = ImageObject(Texture(os.path.join(hero_path, image)),
                int(frame_x), clickable = True)
        return sprites, name

    def load_hero_animations(self, animations_path, path):
        self.anims = {}
        animations = json.loads(open(animations_path).read())
        for key, item in animations.items():
            animations[key].extend([ImageObject(Texture(os.path.join(path, item[0]), int(len(item[1]))))])
        return animations

    def load_heroes(self):
        #name = self.engine.db("SELECT * FROM hero_names")[0][0]
        for name in ['donkey', 'diddy']:
            self.create_hero(name)

    def run(self):
        self.select()

    def select(self):
        pass

    def image_clicked(self, obj):
        if self.step == self.steps[0]:
            self.create_stat_menu.button_clicked(obj)
        elif self.step == self.steps[1]:
            self.create_hero_menu.button_clicked(obj)

        if not self.step:
            self.engine.viewport.push_scene('InventorySystem')
            self.load_heroes()
            #self.engine.viewport.push_scene('CreateEnemySystem')
            self.engine.viewport.push_scene('BattleSystem')

    def draw(self):
        self.background.draw()
        if self.step == self.steps[0]:
            self.create_stat_menu.draw()
        elif self.step == self.steps[1]:
            self.create_hero_menu.draw()