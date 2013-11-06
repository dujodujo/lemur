from math import*

import pygame
import numpy as numpy

from System import*
import WorldScene

from OpenGL.GL import*
from OpenGL.GLU import*

import InputCommands

class Scene:
    def __init__(self): pass

    def image_clicked(self, clicked): pass

    def draw(self): pass

    def run(self): pass

class Viewport:

    def __init__(self, engine, resolution):
        self.engine = engine
        self.resolution = resolution
        self.width, self.height = self.resolution
        self.camera = Camera((0,0), 100)

        self.current_scene = None
        self.scenes = list()

        self.transition_time = 32
        self.fade = 0

        self.setup_viewport()

    def setup_viewport(self):
        glViewport(0, 0, self.width, self.height)

        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)
        glEnable(GL_COLOR_MATERIAL)
        glShadeModel(GL_SMOOTH)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glEnable(GL_BLEND)
        glClearColor(0, 0, 0, 0)
        glClearDepth(1)
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_ALPHA_TEST)
        glDepthFunc(GL_LEQUAL)
        glAlphaFunc(GL_NOTEQUAL, 0)

        glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE)
        glEnable(GL_TEXTURE_2D)
        glEnable(GL_FOG)
        glEnable(GL_LIGHTING)

    def set_perspective_projection(self):
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glPushMatrix()
        gluPerspective(45, self.width/self.height, -500, 1000)

    def set_ortho_projection(self):
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glPushMatrix()
        glOrtho(0, self.width, 0, self.height, -500, 1000)
        glScalef((self.width/800), (self.height/600), 1.0)
        glTranslatef(-self.camera.focus_x, -self.camera.focus_y, 1.0)
        glScalef(self.camera.zoom/100, self.camera.zoom/100, 1)

    def set_reset_projection(self):
        glMatrixMode(GL_PROJECTION)
        glPopMatrix()

    def change_scene(self, scene):
        if scene not in self.scenes:
            InputCommands.reset()
            scene = WorldScene.create(self.engine, scene)
            self.current_scene = scene

    def push_scene(self, scene):
        InputCommands.reset()
        scene = WorldScene.create(self.engine, scene)
        self.current_scene = scene

    def pop_scene(self, scene):
        if scene in self.scenes:
            InputCommands.reset()
            self.scenes.remove(scene)

    def check_clicks(self, scene):
        for click_position in InputCommands.mouse_clicks:
            for clickable in ImageObject.clickables:
                if clickable.test_collision(click_position):
                    scene.image_clicked(clickable)

    def draw(self, scene):
        scene.draw()

    def run(self):
        glClear(GL_DEPTH_BUFFER_BIT)
        glClear(GL_COLOR_BUFFER_BIT)
        #reset matrix every frame
        glLoadIdentity()

        #ticks/rate of change in time
        t = 1.0 / self.transition_time

        if self.current_scene:
            self.fade = min(1.0, self.fade + t)
            if self.fade >= 1.0:
                if self.scenes:
                    self.scenes.pop(-1)
                self.scenes.append(self.current_scene)
                self.current_scene = None
        else:
            self.fade = max(0.0, self.fade - t)

        #all scenes should be rendered but not checked for input
        for i, scene in enumerate(self.scenes):
            top = scene == self.scenes[-1]
            if top:
                scene.run()
            try:
                self.set_ortho_projection()
                self.draw(scene)
                self.set_reset_projection()
            finally:
                self.set_perspective_projection()
                self.set_reset_projection()
        pygame.display.flip()

        if self.scenes:
            self.check_clicks(self.scenes[-1])