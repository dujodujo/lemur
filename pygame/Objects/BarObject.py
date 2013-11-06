from math import*

from OpenGL.GL import*
from OpenGL.GLU import*

import numpy as np
from numpy import*

from Object import Object

class BarObject(Object):
    def __init__(self, texture, length):
        Object.__init__(self, texture)

        self.length = length
        self.position = (0, 0)
        self.create_arrays()

    def create_arrays(self):
        self.vertex_array = np.zeros((8, 3))
        self.texture_array = np.zeros((8, 2))

        self.index_array = np.array([0, 1, 5, 4,
                                     1, 2, 6, 5,
                                     2, 3, 7, 6])
        self.create_vertices()
        self.create_textures()

    def create_vertices(self):
        border_width = self.pixel_size[0]/3
        border_height = self.pixel_size[1]

        x_coordinates = [0, border_width, self.length - border_width, self.length]
        if self.length < border_width:
            x_coordinates[2] = border_width
            x_coordinates[3] = border_width * 2

        y_coordinates = [0, border_height]
        index = 0
        for i in range(2):
            for n in range(4):
                self.vertex_array[index, 0] = x_coordinates[n]
                self.vertex_array[index, 1] = y_coordinates[i]
                index += 1

    def create_textures(self):
        x_coordinates = [0, 1/3, 2/3, 1]
        y_coordinates = [0, 1]

        index = 0
        for i in range(2):
            for n in range(4):
                self.texture_array[index, 0] = x_coordinates[n]
                self.texture_array[index, 1] = y_coordinates[i]
                index += 1

    def set_length(self, length = 96):
        self.width = length
        self.create_vertices()

    def draw(self):
        glPushMatrix()
        x, y = self.position

        glScalef(self.scale[0], self.scale[1], 1)
        glTranslatef(x, y, -.1)
        glRotatef(0, 0, 0, 1)
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