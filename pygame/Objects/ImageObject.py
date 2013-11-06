import pygame
from pygame.locals import*

from OpenGL.GL import*
from OpenGL.GLU import*

import numpy as np
from numpy import*

from System import*
from Object import Object

class ImageObject(Object):
    clickables = []

    def __init__(self, texture, frame_x = 1, frame_y = 1, clickable = False):
        Object.__init__(self, texture)
        self.position = (0, 0)

        self.frame_size = (1/float(frame_x), 1/float(frame_y))
        self.rect = (0, 0, self.frame_size[0], self.frame_size[1])
        self.pixel_size = (self.texture.pixel_size[0]/frame_x,
                           self.texture.pixel_size[1]/frame_y)

        self.width, self.height = self.pixel_size
        self.size = (self.width, self.height)

        self.frames = [frame_x, frame_y]
        self.current_frame = (frame_x, frame_y)
        self.reverse_animation = False

        if clickable:
            ImageObject.clickables.append(self)

        self.create_arrays()

    def create_arrays(self):
        self.vertex_array = np.zeros((4, 3), dtype = np.float32)
        self.texture_array = np.zeros((4, 2), dtype = np.float32)
        self.index_array = [0, 1, 2, 3]

        self.create_vertices()
        self.create_textures()

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

    def set_rect(self, rect):
        self.rect = rect
        self.create_textures()

    def set_frame(self, x = 1, y = 1):
        self.current_frame = (x, y)
        self.rect = ((x-1) * self.frame_size[0], (y-1) * self.frame_size[1],
                      x * self.frame_size[0], y * self.frame_size[1])
        self.create_textures()

    def test_collision(self, point):
        x, y = point
        x1, y1 = self.position[0], self.position[1]

        x1 -= self.width/2
        y1 += self.height/2

        x2 = x1 + self.width
        y2 = y1 - self.height

        if x1 <= x <= x2:
            if y2 <= y <= y1:
                return True
        return False

    def set_clickable(self, clickable):
        self.clickable = clickable
        if self.clickable:
            if self.clickable not in ImageObject.clickables:
                ImageObject.clickables.append(self)
        else:
            if self in ImageObject.clickables:
                ImageObject.clickables.remove(self)

    def draw(self):
        glPushMatrix()

        glTranslatef(self.position[0], self.position[1], -.1)
        glScalef(self.scale[0], self.scale[1], 1)
        glColor4f(*self.color)

        self.texture.bind()
        glEnableClientState(GL_TEXTURE_COORD_ARRAY)
        glEnableClientState(GL_VERTEX_ARRAY)
        glVertexPointerf(self.vertex_array)
        glTexCoordPointerf(self.texture_array)
        glDrawElements(GL_QUADS, len(self.index_array), GL_UNSIGNED_BYTE, self.index_array)
        glDisableClientState(GL_VERTEX_ARRAY)
        glDisableClientState(GL_TEXTURE_COORD_ARRAY)
        glPopMatrix()