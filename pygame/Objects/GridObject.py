from math import*
from ImageObject import ImageObject
from WindowObject import WindowObject

class GridObject(ImageObject):
    def __init__(self, texture, cells=(0,0), position=(250,250)):
        ImageObject.__init__(self, texture)
        self.texture.change_texture(texture.texture_surface, False)

        self.position = position
        self.cells = cells
        self.create_grid(self.cells[0], self.cells[1])

    def create_grid(self, xx, yy):
        self.windows = [WindowObject(self.texture) for xi in range(0, xx*yy)]
        for i, window in enumerate(self.windows):
            window.set_scale(0.6, 0.6)
            if i == 0:
                window.set_position(self.position[0], self.position[1])
            else:
                if (i % xx) != 0:
                    x = self.windows[i-1].position[0] + self.windows[i-1].width
                    window.set_position(x, self.position[1])
                else:
                    x = self.position[0]
                    y = self.windows[i-1].position[1] + self.windows[i-1].height
                    self.position = (x,y)
                    window.set_position(x, y)

    def set_position(self, x, y):
        if self.position != (x, y):
            self.position = (x, y)
        self.create_grid(self.cells[0], self.cells[1])

    def draw(self):
        for window in self.windows:
            window.draw()