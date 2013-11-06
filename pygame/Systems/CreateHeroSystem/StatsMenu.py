from System import*
from pygame import*
import math

from Objects.GridObject import*

class StatsMenu(MenuObject):
    def __init__(self, scene, scene_path):
        MenuObject.__init__(self, scene)
        self.scene = scene
        self.engine = self.scene.engine
        self.entities = self.engine.entities

        self.width, self.height = self.engine.width, self.engine.height
        self.commands = self.scene.stats

        self.load_window()
        self.load_texts(scene_path)
        self.load_buttons()
        self.load_hero_selection_grid()
        self.load_hero_selected_grid()

    def load_hero_selection_grid(self):
        self.hero_selection_grid = GridObject(Texture(Paths.WINDOW_PATH), (3, 3))
        self.hero_selection_grid.set_position(self.width/2, self.height/2)

    def load_hero_selected_grid(self):
        self.hero_selected_grid = GridObject(Texture(Paths.WINDOW_PATH), (3, 1))
        self.hero_selected_grid.set_position(self.width/2, self.height/6)

    def load_window(self):
        self.window = WindowObject(Texture(Paths.WINDOW_PATH))
        self.window.set_position(self.width/6, self.height/2)
        self.window.set_scale(2,3)

    def load_buttons(self):
        self.load_labels()
        self.load_stats_buttons()
        self.ok_button = ButtonObject(Texture(Paths.OK_BTN_PATH), clickable=True)
        self.ok_button.set_position(self.window.position[0] + self.window.width/2,
            self.window.position[1] - self.window.height/2)

    def load_stats_buttons(self):
        button_texture = Texture(os.path.join('data', 'scenes', 'creationsystem',
            "button_stats.png"))
        self.stats_buttons = [[ButtonObject(button_texture, frame_x = 2, clickable=True)
            for n in range(2)] for i in range(len(self.buttons))]

        for i, buttons in enumerate(self.stats_buttons):
            for n, button in enumerate(buttons):
                button.set_scale(0.8, 0.8)
                x, y = self.buttons[i].position
                w, h = self.buttons[i].size
                if n == 0:
                    button.set_position((x+w/2)+20,(y+h)-30)
                else:
                    button.set_position((x+w/2)+50,(y+h)-30)
                button.x = n+1

    def load_labels(self):
        button_texture = os.path.join('data', 'scenes', 'creationsystem', 'btn_b.png')
        self.buttons = [ButtonObject(Texture(button_texture), frame_y = 2, clickable=False)
                        for n in range(len(self.commands))]

        for i, button in enumerate(self.buttons):
            button.set_frame(1,1)
            button.set_scale(0.8, 0.8)
            button.set_position(self.width/8, self.height*3/4 - i*50)

    def load_texts(self, scene_path):
        self.text = FontObject(size=20)
        self.max_stats_text = FontObject(size=20)
        self.stats_text = FontObject(size=20)

    def button_clicked(self, button):
        if isinstance(button, ButtonObject):
            for i, buttons in enumerate(self.stats_buttons):
                for btn in buttons:
                    if button == btn:
                        if button.x == 1:
                            self.scene.current_stats_points +=1
                            self.scene.current_stats_points = min(self.scene.current_stats_points,
                                self.scene.max_stats_points)
                            self.scene.points[i] += 1
                    elif button.x == 2:
                            self.scene.current_stats_points -=1
                            self.scene.current_stats_points = max(0, self.scene.current_stats_points)
                            self.scene.points[i] -= 1

            if button == self.ok_button:
                self.scene.step = self.scene.steps[1]

    def draw_max_stats_text(self):
        self.max_stats_text.set_text(self.scene.max_stats_points)
        self.max_stats_text.set_color((1,0,0,1))
        self.max_stats_text.set_position((100, 500))
        self.max_stats_text.draw()

    def draw_current_stats_text(self):
        self.stats_text.set_text(self.scene.current_stats_points)
        self.max_stats_text.set_color((1,1,0,1))
        self.stats_text.set_position((200, 500))
        self.stats_text.draw()

    def draw(self):
        self.window.draw()
        for i, button in enumerate(self.buttons):
            self.stats_buttons[i][0].set_frame(x=1)
            self.stats_buttons[i][1].set_frame(x=2)
            self.stats_buttons[i][0].draw()
            self.stats_buttons[i][1].draw()
            button.set_frame(y = 2)
            button.draw()

            x, y = button.position
            self.text.set_text(self.commands[i])
            self.text.set_position((x, y))
            self.text.draw()

        self.ok_button.draw()
        self.draw_max_stats_text()
        self.draw_current_stats_text()
        self.hero_selected_grid.draw()
        self.hero_selection_grid.draw()