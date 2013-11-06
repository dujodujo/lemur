from System import*
from Scene import*
from Commands import*

class BattleMenu(Scene):
    def __init__(self, engine):
        Scene.__init__(self)
        self.engine = engine

        self.commands = [Attack(), Defend(), Heal()]
        self.position = (self.engine.width*0.15, self.engine.height*0.15)

        self.load_buttons()

    def load_buttons(self):
        self.buttons = list()
        button_path = Paths.BTNS_PATH

        self.buttons = [ButtonObject(Texture(button_path), 2, 3, (1, i)) for i in range(1,4)]
        [btn.set_position(self.position[0] + 100 * i, self.position[1])
            for i, btn in enumerate(self.buttons)]

        for command, button in zip(self.commands, self.buttons):
            button.set_command(command)

    def button_clicked(self, button):
        heroes = self.engine.entities.heroes()
        for btn in self.buttons:
            if btn == button:
                for hero in heroes:
                    if hero.active:
                        hero.command = btn.command
                        break

    def draw(self):
        for button, command in zip(self.buttons, self.commands):
            button.draw()