import pygame
from pygame.locals import*

from OpenGL.GL import*
from OpenGL.GLU import*

import numpy as np
from numpy import*

from System import*

class FontObject(object):
    def __init__(self, path='default.ttf', text = '', size = 32, shadow = True):
        self.font = pygame.font.Font(os.path.join('data', 'fonts', path), int(size))

        self.position = (0, 0)
        self.angle = 0
        self.rect = (0, 0, 1, 1)
        self.scale = (1, 1)
        self.color = [255, 255, 255, 255]
        self.shadow = shadow
        self.set_text(text)

    def dimensions(self):
        self.width = self.pixel_size[0] * self.scale[0]
        self.height = self.pixel_size[1] * self.scale[1]

    def set_text(self, text):
        if not text:
            self.text = ''
        else:
            self.text = str(text)

        self.texture = Texture(surface = self.font.render(self.text, True, (255, 255, 255)))
        self.pixel_size = self.texture.pixel_size
        self.create_arrays()

    def create_arrays(self):
        self.vertex_array = np.zeros((4, 3), dtype = np.float32)
        self.texture_array = np.zeros((4, 2), dtype = np.float32)

        self.create_vertices()
        self.create_textures()
        self.dimensions()

    def create_vertices(self):
        self.vertex_array[0,0] = -self.pixel_size[0]/2
        self.vertex_array[0,1] =  self.pixel_size[1]/2
        self.vertex_array[1,0] =  self.pixel_size[0]/2
        self.vertex_array[1,1] =  self.pixel_size[1]/2
        self.vertex_array[2,0] =  self.pixel_size[0]/2
        self.vertex_array[2,1] = -self.pixel_size[1]/2
        self.vertex_array[3,0] = -self.pixel_size[0]/2
        self.vertex_array[3,1] = -self.pixel_size[1]/2

    def create_textures(self):
        self.texture_array[0,0] = self.rect[0]
        self.texture_array[0,1] = self.rect[1]
        self.texture_array[1,0] = self.rect[2]
        self.texture_array[1,1] = self.rect[1]
        self.texture_array[2,0] = self.rect[2]
        self.texture_array[2,1] = self.rect[3]
        self.texture_array[3,0] = self.rect[0]
        self.texture_array[3,1] = self.rect[3]

    def set_position(self, (x, y)):
        if not self.position == (x, y):
            self.position = x, y

    def move(self, x, y):
        self.position = (self.position[0] + x, self.position[1] + y)

    def set_color(self, color):
        for i in range(len(self.color)):
            self.color[i] = color[i]

    def set_angle(self, angle):
        if not self.angle == angle:
            self.angle = angle

    def set_rect(self, rect):
        self.rect = rect
        self.create_textures()

    def set_scale(self, width = 1, height = 1):
        if self.scale[0] != width and self.scale[1] != height:
            if(0 <= width <= 1) and (0 <= height <= 1):
                self.scale = (width, height)
            else:
                self.scale = (float(width)/float(self.pixel_size[0]),
                    float(height)/float(self.pixel_size[1]))
            self.dimensions()

    def draw(self):
        glPushMatrix()
        glColor4f(*self.color)

        x, y = self.position

        glTranslatef(x, y, -.1)
        glScalef(self.scale[0], self.scale[1], 1)
        glRotatef(self.angle, 0, 0, 1)

        self.texture.bind()
        glEnableClientState(GL_TEXTURE_COORD_ARRAY)
        glEnableClientState(GL_VERTEX_ARRAY)
        glVertexPointerf(self.vertex_array)
        glTexCoordPointerf(self.texture_array)
        glDrawArrays(GL_QUADS, 0, self.vertex_array.shape[0])
        glDisableClientState(GL_VERTEX_ARRAY)
        glDisableClientState(GL_TEXTURE_COORD_ARRAY)
        glPopMatrix()