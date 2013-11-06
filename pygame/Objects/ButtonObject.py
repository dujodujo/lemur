from Texture import Texture
from ImageObject import*

import numpy as np
from numpy import*

class ButtonObject(ImageObject):
    def __init__(self, texture, frame_x = 1, frame_y = 1,
            clickable = True, selected = True):
        ImageObject.__init__(self, texture, frame_x, frame_y, clickable)

        self.x, self.y = frame_x, frame_y
        self.set_frame(self.x, self.y)
        self.position = (0, 0)
        self.selected = selected

    def set_active(self, active):
        self.active = active

    def set_command(self, command):
        self.command = command

    def set_selected(self, selection):
        self.selected = selection

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

    def draw(self):
        super(ButtonObject, self).draw()