from System import*
from Scene import*

scene_path = os.path.join(Paths.EQUIPMENT_SYSTEM)

class EquipmentSystem(Scene):
    def __init__(self, engine):
        Scene.__init__(self)
        self.engine = engine

        self.create_equipment_images()

        scene_path = os.path.join(Paths.EQUIPMENT_SYSTEM, 'background.png')
        self.background = ImageObject(Texture(os.path.join(scene_path)))
        self.background.set_scale(self.engine.width, self.engine.height)
        self.background.set_position(self.engine.width/2, self.engine.height/2)

        self.equipment_buttons = EquipmentButtons(self)
        self.equipment_buttons.load_equipment_buttons(self.image_equipment)

    def button_clicked(self, image): pass

    def select(self): pass

    def run(self): pass

    def create_equipment_images(self):
        self.heroes = self.engine.entities.heroes()
        self.image_equipment = []
        for item_key in self.heroes[0].inventory.available_items():
            if item_key in self.engine.all_items.keys():
                self.image_equipment.append(self.engine.all_items[item_key][1])

    def draw(self):
        self.background.draw()
        self.equipment_buttons.draw()

        for img in self.image_equipment:
            img.draw()

class EquipmentButtons(object):
    def __init__(self, scene):
        self.scene = scene
        self.engine = self.scene.engine

        self.position = (self.engine.width/2, self.engine.height/2)
        self.window = WindowObject(Texture(os.path.join(Paths.EQUIPMENT_SYSTEM,
            'window.png')), scale=(1, 1))
        self.window.set_position(self.position[0], self.position[1])

    def load_equipment_buttons(self, image_equipment):
        self.item_buttons = [ImageObject(Texture(os.path.join(scene_path, 'icon.png')),
            frame_y=2) for i in range(0, len(image_equipment))]

        for i, button in enumerate(image_equipment):
            button.set_position(self.position[0] + (i*50), self.position[1])
            image_equipment[i].set_position(button.position[0], button.position[1])
            image_equipment[i].set_scale(2, 2)

    def draw(self):
        self.window.draw()
        for button in self.item_buttons:
            button.draw()