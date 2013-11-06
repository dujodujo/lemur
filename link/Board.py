import Tile as t
import Vector as v
import pygame, os

class Board:
    def __init__(self, level):
        self.board=list()
        self.tileSurfaces=dict()

        self.loadTiles()
        self.setupBoard(level)

    def loadTiles(self):
        self.path=os.path.join(os.curdir, "data", "tiles")
        for root, dirs, files in os.walk(self.path):
            for afile in files:
                surface=pygame.image.load(os.path.join(root, afile)).convert()
                name=afile[:-4]
                self.tileSurfaces[name]=surface

    def setupBoard(self, level):
        lines=open("level_"+str(level)+".txt", "r").readlines()
        if lines:
            for j, line in enumerate(lines):
                kva=list()
                for i, type in enumerate(line.strip('\n')):
                    if type=='0':
                        frame=[0, 0, 32, 32]
                        kva.append(t.Tile(self.tileSurfaces['tiles'], pygame.Rect(i*32, j*32, 32, 32), frame))
                    else:
                        frame=[32, 0, 32, 32]
                        kva.append(t.Tile(self.tileSurfaces['tiles'], pygame.Rect(i*32, j*32, 32, 32), frame))
                self.board.append(kva)

    def draw(self, screen):
        for row in self.board:
            for tile in row:
                tile.draw(screen)

    def getTile(self, point):
        return self.board[int(point.x/32)][int(point.y/32)]