import os, sys
import pygame
from pygame.locals import*

import InputCommands
from System import*
from Scene import*
from DB.DBReader import*
from Entities.Entities import Entities

width, height = 800, 600
resolution = (int(width), int(height))
fullscreen = False

video_flags = DOUBLEBUF|OPENGL|HWPALETTE|HWSURFACE
if fullscreen:
    video_flags |= FULLSCREEN

splash_scene = "SplashSystem"
test_scene = "CreateHeroSystem"

class Main:
    def __init__(self, flags):
        self.finished = False
        pygame.init()
        os.environ['SDL_VIDEO_WINDOW_POS'] = 'center'

        self.screen = pygame.display.set_mode(resolution, flags)

        self.viewport = Viewport(self, resolution)
        self.db = self.create_db()
        self.clock = pygame.time.Clock()
        self.current_fps = 60

        self.width, self.height = resolution

        self.entities = Entities()
        self.viewport.push_scene(splash_scene)

    def run(self):
        global finished

        InputCommands.update()
        self.finished = InputCommands.finished
        self.viewport.run()
        InputCommands.reset()

        self.clock.tick(self.current_fps)
        self.current_fps = int(self.clock.get_fps())
        pygame.time.delay(85)
        pygame.display.set_caption("motu")

    def list_path(self, path,):
        items = os.listdir(path)
        return items

    def draw_animation(self, image, loop = True):
        if not isinstance(image, ImageObject):
                return
        x, y = image.current_frame

        if x >= image.frames[0]:
            if loop and x != 1:
                image.reverse_animation = True
                x -= 1
            else:
                x = 1
        elif image.reverse_animation and x <= 2:
            image.reverse_animation = False
            x = 1
        else:
            if image.reverse_animation:
                x -= 1.0
            else:
                x += 1.0
        image.set_frame(x, y)
        image.draw()

    def draw_text(self, font, text, position = (width, height),
            scale = (1, 1), color = (1,1,1,1)):
        if not font and not text:
            return

        font.set_text(text)
        font.set_position(position)
        font.set_scale(scale)
        font.set_color(color)
        font.draw()

    def create_db(self):
        db = DBReader('')
        for i in Paths.DB_FILES:
            file = open(i, "r")
            db.execute_script("BEGIN TRANSACTION;" + file.read() + "COMMIT;")
        return db


game = Main(video_flags)
while not game.finished:
    game.run()