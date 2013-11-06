import pygame, os

from System import*

class BattleHud:
    def __init__(self, engine, position = (0, 0)):
        self.x, self.y = position
        self.engine = engine
        self.faces = []

        self.load_face_frames()

    def set_position(self, x, y):
        self.x, self.y = (x, y)

    def load_face_frames(self):
        frame_path = os.path.join('data', 'scenes' ,'battlesystem','window.png')

        i = 0
        print(self.engine.entities.all_entities(), "ents")

        """
        for face in [(entity.sprites[entity.name+'_face'], FontObject("default.ttf", entity.name, 16))
            for entity in self.engine.entities.values() if entity.name+'_face' in entity.sprites.keys()[:]]:

            frame = ImageObject(Texture(frame_path))
            frame.set_position(self.x, self.y + (i+1)*100)
            frame.set_scale(.5,.5)
            face[0].set_scale(2,2)

            x,y = self.x, self.y
            face[0].set_position(x, y+(i+1)*100)
            face[1].set_position((x, y+(i+1)*100))

            self.faces.append([face, frame])
            i += 1
        """

    def draw(self):
        for face in self.faces:
            face[1].draw()
            face[0][1].draw()
            face[0][0].draw()
