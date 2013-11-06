from System import*
from Scene import*

from Entities.Enemy import*

import json

class CreateEnemySystem(Scene):
    def __init__(self, engine):
        Scene.__init__(self)

        self.engine = engine
        self.width, self.height = self.engine.width, self.engine.height
        self.scene_path = os.path.join('data', 'scenes', 'creation')
        self.load_enemies()

    def create_enemy(self, name):
        animations_path = os.path.join('data', 'animations', name+'_animations.txt')
        sprites_path = os.path.join('data', 'enemy', name)
        sprites = self.load_enemy_sprites(sprites_path, name)
        animations = self.load_enemy_animations(animations_path, sprites_path)

        enemy = Enemy(sprites, animations, Game.WORLD_ID, name)
        enemy.save(self.engine.db)
        self.engine.entities.add_entity(enemy)

    def load_enemy_sprites(self, sprite_path, name):
        sprites = dict()
        for line in open(os.path.join(sprite_path,name+'_sprites.txt')).readlines():
            image, frame_x = line.rstrip('\n').split(',')
            sprites[image.split('.png')[0]] = ImageObject(Texture(os.path.join(sprite_path, image)),
                int(frame_x))
        return sprites

    def load_enemy_animations(self, animations_path, sprites_path):
        self.anims = {}
        animations = json.loads(open(animations_path).read())
        print(sprites_path)
        for key, item in animations.items():
            animations[key].extend([ImageObject(Texture(os.path.join(sprites_path, item[0]), int(len(item[1]))))])
        return animations

    def load_enemies(self):
        for enemy in ['king_rool']:
            self.create_enemy(enemy)