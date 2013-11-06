from System import*

class BattleHudEngage:
    def __init__(self):
        scene_path =os.path.join("scene", "battleSystem")

        self.health_bar = [ImageObject(os.path.join(scene_path, "top_bar.png")),
                           ImageObject(os.path.join(scene_path, "bottom_bar.png")),
                           BarObject(os.path.join(scene_path, "hp_bar.png"))]

        self.health_bar[0].set_alignment("left")
        self.health_bar[1].set_alignment("left")

        self.set_position(0, 20)

    def set_position(self, x, y):
        self.x, self.y = x, y
        for bar in self.health_bar:
            bar.set_position(self.x, self.y + 10)

    def draw(self):
        for bar in self.health_bar:
            bar.draw()