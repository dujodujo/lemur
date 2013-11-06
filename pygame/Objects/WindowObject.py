from OpenGL.GL import*
from OpenGL.GLU import*

import numpy as np
from numpy import*

from math import*
from ImageObject import ImageObject
from Constants import*

class WindowObject(ImageObject):
    def __init__(self, texture, position=(0,0), scale=(1,1)):
        ImageObject.__init__(self, texture)
        self.texture.change_texture(texture.texture_surface, False)

        self.scale = scale
        self.position = position
        self.transition_time = 32

    def draw(self):
        super(WindowObject, self).draw()