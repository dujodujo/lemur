from System import*
from Scene import*

from BattleHud import BattleHud
from BattleMenu import BattleMenu

class BattleSystem(Scene):
    def __init__(self, engine):
        Scene.__init__(self)

        self.engine = engine
        self.camera = self.engine.viewport.camera

        self.width, self.height = self.engine.width, self.engine.height
        self.battle_path = os.path.join('data', 'scenes', 'battlesystem')

        self.load_entities()
        self.load_base_sprites()
        self.load_intro_sprites()
        self.load_particles()

        self.hud = BattleHud(self.engine, (100, 100))
        self.command_menu = BattleMenu(self.engine)

        self.active_entity = None
        self.battle_on = False
        self.delay_intro = True
        self.delay_time = 15

        #turns
        self.turn = 0
        self.total_turns = 0
        self.turns = list()

        #targets
        self.target_menu = None
        self.targeting = False

    def load_particles(self):
        pass

    def load_entities(self):

        for i, hero in enumerate(self.engine.entities.heroes()):
            hero.set_animation(hero.current_sprite)
            hero.set_position((250, 100 * (i+2)))

        for enemy in self.engine.entities.enemies():
            enemy.set_king_rool_animation()

    def load_base_sprites(self):
        self.header = ImageObject(Texture(os.path.join(self.battle_path, "footer.png")))
        self.footer = ImageObject(Texture(os.path.join(self.battle_path, "footer.png")))
        self.active_sprite = ImageObject(Texture(os.path.join(self.battle_path, "active.png")))
        self.pointer = ImageObject(Texture(os.path.join(self.battle_path, 'pointer.png')),
            frame_x = 2)
        heroes = self.engine.entities.heroes()
        self.set_active_hero(heroes[0].current_sprite)

    def load_intro_sprites(self):
        frame_path = os.path.join(self.battle_path,'window.png')
        self.versus = ImageObject(Texture(os.path.join(self.battle_path, "vs.png")))

        hero_face_path=os.path.join('data', 'hero', 'donkey', 'donkey_face.png')
        self.hero_frame=ImageObject(Texture(frame_path))
        self.hero_face=ImageObject(Texture(hero_face_path))

        enemy_face_path=os.path.join('data', 'enemy', 'king_rool', 'king_rool_face.png')
        self.enemy_frame=ImageObject(Texture(frame_path))
        self.enemy_face=ImageObject(Texture(enemy_face_path))

    def image_clicked(self, obj):
        if self.delay_intro > 0:
            return

        if isinstance(obj, ButtonObject):
            self.command_menu.button_clicked(obj)
        elif isinstance(obj, ImageObject):
            self.set_active_hero(obj)

    def set_active_hero(self, obj):
        heroes = self.engine.entities.heroes()
        for hero in heroes:
            if hero.current_sprite == obj:
                x, y = obj.position
                self.pointer.set_position(x, y)
                self.pointer.set_scale(.2, .2)
                hero.active = True
            else:
                hero.active = False

    def run(self):
        if self.battle_on:
            self.execute()

    def select(self, current_scene):
        if current_scene == 0:
            self.engine.change_scene(current_scene)

    def next(self):
        if self.battle_on:
            for hero in self.engine.entities.heroes():
                if hero.animation.finished:
                    hero.turn_end()

    def execute(self):
        for hero in self.engine.entities.heroes():
            hero.check_listeners()

            if hero.command is not None:
                hero.turn_start()
        self.next()

    def draw_intro(self):
        if self.delay_time > 0:
            self.delay_time -= 5
        else:
            self.delay_intro = False
            self.battle_on = True

        x, y = 0.3, 0.6
        m, n = 0.4, 0.6
        i, j = 0.5, 0.6

        self.hero_frame.set_position(self.engine.width * x, self.engine.height * y)
        self.hero_frame.set_scale(.5, .5)
        self.hero_frame.draw()

        self.hero_face.set_position(self.engine.width * x, self.engine.height * y)
        self.hero_face.set_scale(2, 2)
        self.hero_face.draw()

        self.versus.set_position(self.engine.width * m, self.engine.height * n)
        self.versus.set_scale(.5, .5)
        self.versus.draw()

        self.enemy_frame.set_position(self.engine.width * i, self.engine.height * j)
        self.enemy_frame.set_scale(.5, .5)
        self.enemy_frame.draw()

        self.enemy_face.set_position(self.engine.width * i, self.engine.height * j)
        self.enemy_face.set_scale(2, 2)
        self.enemy_face.draw()

    def draw_base(self):
        self.header.set_position(0, self.engine.height)
        self.header.draw()

        self.footer.set_position(0, 0)
        self.footer.draw()

    def draw_command_interface(self):
        self.hud.draw()
        self.command_menu.draw()

    def draw_battle(self):
        for entity in self.engine.entities.all_entities():
            entity.draw()
        self.pointer.draw()

    def draw(self):
        if self.delay_intro:
            self.draw_intro()
        else:
            #self.draw_base()
            self.hud.draw()
            self.draw_command_interface()
            self.draw_battle()