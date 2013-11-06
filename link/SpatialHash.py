import pygame, sys, math, random
import GameClock as gc

class SpatialHash:
    def __init__(self, csize, wsize):
        self.cells=dict()
        self.rect=wsize
        self.cellSize=csize
        self.columns=int(math.ceil(self.rect.right/self.cellSize))
        self.rows=int(math.ceil(self.rect.bottom/self.cellSize))

    def addEntity(self, entity):
        cells=self.intersectionIndexes(entity.rect)
        if entity in self.cells and cells==self.cells[entity]:
            self.removeEntity(entity)
        self.cells[entity]=cells

    def removeEntity(self, entity):
        if entity in self.cells:
            del self.cells[entity]

    def entitiesInRange(self, entity):
        entities=set()
        self.addEntity(entity)
        for i in self.cells[entity]:
            for ent, value in self.cells.items():
                if i in value and ent!=entity:
                    entities.add(ent)
        return list(entities)

    def intersectionIndexes(self, rect):
        indexes=set()
        xstep=rect.right-rect.left
        ystep=rect.bottom-rect.top

        if rect.left <= self.rect.left: rect.left=self.rect.left+1
        if rect.right >= self.rect.right: rect.right=self.rect.right-1
        if rect.top <= self.rect.top: rect.top=self.rect.top+1
        if rect.bottom >= self.rect.bottom: rect.bottom=self.rect.bottom-1

        for x in range(rect.left, rect.right+1, xstep):
            for y in range(rect.top, rect.bottom+1, ystep):
                i=x/self.cellSize+y/self.cellSize*self.columns
                indexes.add(i)
        return list(indexes)

    def testCollision(self, entity):
        collisions=[]
        for ent in self.entitiesInRange(entity):
            if ent==entity:
                continue
            if entity.rect.colliderect(ent):
                collisions.append(ent)
        return collisions

    def testAllCollisions(self):
        collisions = set()
        for entity in self.cells:
            for aentity in self.testCollision(entity):
                collisions.add(aentity)
        return list(collisions)

    def entites(self):
        return self.cells.keys()

    def getCellGrid(self, i):
        x=i/self.columns
        y=i-x*self.columns
        return x, y

    def getCellPosition(self, id):
        x, y=self.getCellGrid(id)
        x*=self.cellSize
        y*=self.cellSize
        return y+self.rect.top, x+self.rect.left

    def __iter__(self):
        for entity in self.cells:
            yield entity

    def __contains__(self, item):
        return item in self.cells

    def __len__(self):
        return len(self.cells)

class Ball(pygame.sprite.Sprite):
    def __init__(self, position, velocity):
        pygame.sprite.Sprite.__init__(self)
        self.surface = pygame.Surface((8, 8))
        self.surface.fill(pygame.Color('white'))
        self.rect=self.surface.get_rect()
        self.rect.left, self.rect.top=position
        self.velocity=velocity

    def update(self, worldRect, spatial):
        self.testBounds(worldRect)
        self.setColor()
        self.testCollisionsSpatial(spatial)
        #self.testCollisionsBrute(spatial)

    def draw(self, screen, interp):
        vx, vy = self.velocity
        self.rect.left +=vx*interp
        self.rect.top +=vy*interp
        screen.blit(self.surface, self.rect)

    def testCollisionsSpatial(self, spatial):
        bs=spatial.testCollision(self)
        for ball in bs:
            ball.setColor('yellow')
            self.setColor('yellow')

    def testBounds(self, worldRect):
        left, top, right, bottom=worldRect
        if self.rect.left <= left or self.rect.right >= right:
            self.velocity=[-1*vx for vx in self.velocity]
        if self.rect.top <= top or self.rect.bottom >= bottom:
            self.velocity=[-1*vy for vy in self.velocity]

    def setColor(self, color='white'):
        self.surface.fill(pygame.Color(color))

    def speed(self):
        xvel=self.velocity[0]*self.velocity[0]
        yvel=self.velocity[1]*self.velocity[1]
        return math.sqrt(xvel*xvel + yvel*yvel)

class Game:
    def __init__(self):
        pygame.init()
        self.running=True
        self.screen=pygame.display.set_mode((320, 320))

        self.clock=gc.GameClock(time=pygame.time.get_ticks, fps=24,
            updateCallback=self.update, drawCallback=self.draw)

        self.worldRect=pygame.Rect(0, 0, 320, 320)
        self.spatial=SpatialHash(32, self.worldRect)

        width, height=self.worldRect[2:]
        self.background=pygame.Surface((width, height))
        self.background.fill(pygame.Color('black'))

        self.initBalls()

    def initBalls(self):
        self.balls=[]
        for ball in range(300):
            x=int(random.randrange(0,300))
            y=int(random.randrange(0,300))
            vx=int(random.randrange(0,2))
            vy=int(random.randrange(0,2))
            if not vx and not vy: vx=1
            ball=Ball(position=[x,y], velocity=[vx, vy])
            self.balls.append(ball)
            self.spatial.addEntity(ball)

    def run(self):
        while self.running:
            self.clock.tick()
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.update(dt=0)
            self.draw(interp=0)

    def update(self, dt):
        for ball in self.balls:
            ball.update(self.worldRect, self.spatial)
        print len(self.spatial.testAllCollisions())

    def drawGrid(self):
        size=self.spatial.columns*self.spatial.rows
        for i in range(size):
            x, y=self.spatial.getCellPosition(i)
            p1=x, self.worldRect[1]
            p2=x, self.worldRect[3]
            pygame.draw.line(self.screen, pygame.Color('white'), p1, p2)

            p1=self.worldRect[0], y
            p2=self.worldRect[2], y
            pygame.draw.line(self.screen, pygame.Color('white'), p1, p2)

    def draw(self, interp):
        self.screen.blit(self.background, self.worldRect[:2])
        self.drawGrid()
        for ball in self.balls:
            ball.draw(self.screen, interp)
        pygame.display.flip()

game=Game()
game.run()

