from System import*
from Scene import*

class InventorySystem(Scene):
    def __init__(self, engine):
        Scene.__init__(self)

        self.engine = engine

        scene_path = Paths.EQUIPMENT_SYSTEM

        self.next_btn = ButtonObject(Texture(os.path.join(scene_path, 'nextButton.png')))
        self.last_btn = ButtonObject(Texture(os.path.join(scene_path, 'lastButton.png')))

        self.next_btn.set_position(self.engine.width - self.next_btn.width/2,
            self.engine.height - 96 - self.next_btn.height/2)
        self.last_btn.set_position(self.engine.width - self.last_btn.width/2,
            self.last_btn.height/2)

        window_scale = (self.engine.width/2 - self.next_btn.width/2, self.engine.height - 96)
        self.window = WindowObject(Texture(Paths.WINDOW_PATH), scale=window_scale)
        self.window.set_position(self.engine.width-self.window.scale[0]/2-self.next_btn.width,
            self.window.scale[1]/2)