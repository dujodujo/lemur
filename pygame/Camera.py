from OpenGL.GL import*
from OpenGL.GLU import*

class Camera:
    def __init__(self, position, zoom = 100):
        self.focus_x = position[0]
        self.focus_y = position[1]
        self.zoom = zoom

        self.old_focus_x = self.focus_x
        self.old_focus_y = self.focus_y
        self.old_zoom = self.zoom

    def focus(self, x, y, zoom):
        self.old_focus_x = self.focus_x
        self.old_focus_y = self.focus_y
        self.old_zoom = self.zoom

        self.focus_x = x
        self.focus_y = y
        self.zoom = zoom

    def reset_focus(self):
        self.focus_x = self.old_focus_x
        self.focus_y = self.old_focus_y
        self.zoom = self.old_zoom