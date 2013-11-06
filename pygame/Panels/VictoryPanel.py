from System import*
import InputCommands

class VictoryPanel:
    def __init__(self, scene):
        self.scene = scene
        self.engine = self.scene.engine

        battle_path = os.path.join('scenes', 'battlesystem')

        self.background = ImageObject(Texture(os.path.join(battle_path, 'victory.png')))
        self.background.set_scale(self.engine.width, self.engine.height, pixels=True)
        self.background.set_position(self.engine.width/2, self.engine.height/2)

        self.hero = self.engine.hero
        self.enemies = self.engine.enemies

        self.gold = 0
        self.exp = 0

        for enemy in self.enemies:
            self.gold += enemy.gold
            self.exp += enemy.exp