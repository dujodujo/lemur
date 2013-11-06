from System import*
import os
import json

class Animation(object):
    def __init__(self):
        self.current_frame = 0
        self.finished = False

    #animations
    def set_animation(self, animation):
        self.current_animation = animation
        self.frames_limit = len(self.current_animation[1])

    def draw_animation(self, image, loop = False):
        if not isinstance(image, ImageObject):
            return

        x, y = image.current_frame

        if not self.finished:
            if self.frames_limit == 1:
                image.set_frame(x, y)
                image.draw()
            else:
                x += 1
                if x > self.frames_limit:
                    self.finished = True
                    return
                else:
                    image.set_frame(x, y)
                    image.draw()