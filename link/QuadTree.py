import pygame

class QuadTree(object):
    def __init__(self, items, depth=8, worldRect=None):
        self.topLeft=None
        self.topRight=None
        self.bottomLeft=None
        self.bottomRight=None

        depth-=1
        if not depth or not items:
            self.items=items
            return
        if worldRect:
            rec=worldRect
        else:
            rec=items[0].rect
            for item in items[1:]:
                rec.union_ip(item)
        self.midx=(rec.left+rec.right)*0.5
        self.midy=(rec.top+rec.bottom)*0.5

        self.items=[]
        topLeftItems=[]
        topRightItems=[]
        bottomLeftItems=[]
        bottomRightItems=[]

        for item in items:
            topLeft=item.rect.left <= self.midx and item.rect.top <= self.midy
            topRight=item.rect.right >= self.midx and item.rect.top <= self.midy
            bottomLeft=item.rect.left <= self.midx and item.rect.bottom >= self.midy
            bottomRight=item.rect.right >= self.midx and item.rect.bottom >= self.midy

            if topLeft and topRight and bottomLeft and bottomRight:
                self.items.append(item)
            else:
                if topLeft: topLeftItems.append(item)
                if topRight: topRightItems.append(item)
                if bottomLeft: bottomLeftItems.append(item)
                if bottomRight: bottomRightItems.append(item)

        if topLeftItems:
            self.topLeft=QuadTree(topLeftItems, depth,
                pygame.Rect(worldRect.left, worldRect.top, self.midx, self.midy))
        if topRightItems:
            self.topRight=QuadTree(topRightItems, depth,
                pygame.Rect(self.midx, worldRect.top, worldRect.right, self.midy))
        if bottomLeftItems:
            self.bottomLeft=QuadTree(bottomLeftItems, depth,
                pygame.Rect(worldRect.left, self.midy, self.midx, worldRect.bottom))
        if bottomRightItems:
            self.bottomRight=QuadTree(bottomRightItems, depth,
                pygame.Rect(self.midx, self.midy, worldRect.right, worldRect.bottom))

    def testCollision(self, entity):
        hits=set([self.items[i] for i in entity.rect.collidelistall(self.items)])

        if self.topLeft and entity.rect.left <= self.midx and entity.rect.top <= self.midy:
            hits |= self.topLeft.testCollision(entity.rect)
        if self.topRight and entity.rect.right >= self.midx and entity.rect.top <= self.midy:
            hits |= self.topRight.testCollision(entity.rect)
        if self.bottomLeft and entity.rect.right <= self.midx and entity.rect.bottom >= self.midy:
            hits |= self.bottomLeft.testCollision(entity.rect)
        if self.bottomRight and entity.rect.left >= self.midx and entity.rect.bottom >= self.midy:
            hits |= self.bottomRight.testCollision(entity.rect)
        return hits