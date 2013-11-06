
class Object(object):
    def __init__(self, texture):
        self.texture = texture
        self.pixel_size = self.texture.pixel_size
        self.scale = (1, 1)
        self.width, self.height = self.pixel_size
        self.size = (self.width, self.height)
        self.color = [1, 1, 1, 1]

    def set_scale(self, width = 1, height = 1, pixels = False):
        if not pixels:
            if not self.scale == (width, height):
                self.scale = (width, height)
                self.width = self.scale[0] * self.pixel_size[0]
                self.height = self.scale[1] * self.pixel_size[1]
                self.transformed = True
            self.size = (self.width, self.height)
        else:
            if not self.scale == (float(width)/float(self.pixel_size[0]),
                                  float(height)/float(self.pixel_size[1])):
                self.scale = (float(width)/float(self.pixel_size[0]),
                              float(height)/float(self.pixel_size[1]))
                self.transformed = True
                self.width = width
                self.height = height

    def set_color(self, color):
        for i in range(len(self.color)):
            self.color[i] = color[i]

    def set_position(self, x, y):
        if not self.position == (x, y):
            self.position = (x, y)