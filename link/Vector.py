import math

class Vec2d:
    def __init__(self, x, y):
        self.x, self.y=x, y

    def __getitem__(self, key):
        if key==0:
            return self.x
        elif key==1:
            return self.y
        else:
            return None

    def __add__(self, other):
        return Vec2d(self.x+other.x, self.y+other.y)

    def __iadd__(self, other):
        self.x+=other
        self.y+=other
        return self

    __radd__=__add__

    def __sub__(self, other):
        return Vec2d(self.x-other.x, self.y-other.y)

    def __isub__(self, other):
        self.x-=other.x
        self.y-=other.y
        return self

    __rsub__=__sub__

    def __mul__(self, other):
        return Vec2d(self.x*other.x, self.y*other.y)

    def __imul__(self, other):
        self.x*=other
        self.y*=other
        return self

    __rmul__ = __mul__

    def __div__(self, other):
        return Vec2d(self.x/other, self.y/other)

    def __idiv__(self, other):
        self.x/=other
        self.y/=other
        return self

    __rmul__ = __mul__

    def zero(self):
        self.x=0
        self.y=0

    def length(self):
        return math.sqrt(self.x**2+ self.y**2)

    def dot(self, other):
        return (self.x*other.x) + (self.y*other.y)

    def distance(self, other):
        YSeperation = self.y-other.y
        XSeperation = self.x-other.x
        return math.sqrt((YSeperation*YSeperation) + (XSeperation*XSeperation))

    def normalize(self):
        l = self.length()
        if l != 0:
            return Vec2d(self.x/l, self.y/l)
        return None

    def __repr__(self):
        return "%s(%r, %r)" % (self.__class__.__name__, self.x, self.y)
