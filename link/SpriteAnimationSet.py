import pygame, os
import SpriteAnimation as sa
import json
import simplejson

class SpriteAnimationSet:
    def __init__(self):
        self.animations=dict()
        self.spriteSurfaces=dict()

        self.loadSprites()
        self.loadAnimations()
        self.initAnimations()

    def loadSprites(self):
        self.path=os.path.join(os.curdir, "data", "sprites")
        for root, dirs, files in os.walk(self.path):
            for afile in files:
                surface=pygame.image.load(os.path.join(root, afile))
                name=afile[:-4]
                self.spriteSurfaces[name]=surface

    def loadAnimations(self):
        with open('animations.json') as f:
            self.animations=json.load(f)

    def initAnimations(self):
        for animation in self.animations['animations']:
            name=animation['animation']
            directions=animation['directions']
            frames=animation['frames']
            numFrames=animation['numFrames']
            frameDelay=animation['frameDelay']
            limited=animation['limited']
            surfaceName=animation['image']
            directions=self.loadDirections((directions, numFrames, frames))
            self.animations[name]=sa.SpriteAnimation(
                self.spriteSurfaces[surfaceName], frameDelay, directions, limited)

    def loadDirections(self, directionData):
        directions=list()
        numDirections, numFrames, frameData=directionData
        x, y, width, height=frameData
        for i in range(numDirections):
            frames=list()
            for row in range(numFrames):
                frames.append(pygame.Rect(x + width*row, y + height*i, width, height))
            directions.append(frames)
        return directions