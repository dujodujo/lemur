import os, sys

import pygame, pygame.image
from pygame.locals import*

from OpenGL.GL import*
from OpenGL.GLU import*

from PIL import Image, ImageDraw

import OpenGL.GLU
import math

class Texture:
    def __init__(self, path = '', surface = pygame.Surface((1,1)), flip = True):
        self.id = glGenTextures(1)
        if path != '':
            self.texture_surface = pygame.image.load(path)
        else:
            self.texture_surface = surface
        self.change_texture(self.texture_surface, flip)

    def change_texture(self, texture, flip = True):
        self.texture_surface = texture

        #convert PIL image to pygame surfaces
        if isinstance(texture, Image.Image):
            self.texture_surface = pygame.image.fromstring(self.texture_surface.tostring('raw', 'RGBA', 0, -1),
                self.texture_surface.size, 'RGBA')

        self.pixel_size = self.texture_surface.get_size()

        self.destination_surface = self.convert_texture_2(flip)
        self.texture_data = pygame.image.tostring(self.destination_surface, 'RGBA', 1)

        self.bind()
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, self.destination_surface.get_width(),
            self.destination_surface.get_height(), 0, GL_RGBA, GL_UNSIGNED_BYTE, self.texture_data)

    def convert_texture_2(self, flip = True):
        width  = 2**math.ceil(math.log(self.pixel_size[0], 2))
        height = 2**math.ceil(math.log(self.pixel_size[0], 2))

        surface = pygame.transform.smoothscale(self.texture_surface, (int(width), int(height)))
        surface = pygame.transform.flip(surface, False, flip)
        return surface

    def bind(self, repeat = False):
        glBindTexture(GL_TEXTURE_2D, self.id)

        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)

        if repeat:
            glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)