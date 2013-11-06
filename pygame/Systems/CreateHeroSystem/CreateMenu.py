from System import*

class CreateMenu(MenuObject):
    def __init__(self, scene, scene_path):
        MenuObject.__init__(self, scene)
        self.scene = scene
        self.scene.engine = scene.engine

        self.ok_button = ButtonObject(Texture(Paths.OK_BTN_PATH))

    def button_clicked(self, button):
        if isinstance(button, ButtonObject):
            if button == self.ok_button:
                self.scene.step = None

    def draw(self):
        self.ok_button.set_position(300, 150)
        self.ok_button.draw()

