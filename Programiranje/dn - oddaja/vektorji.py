a = [8, 5,8,9]
b = [1,2,6]
import math

def pomozna(a,b):
    for i in range(max(len(a),len(b))):
        if len(a) < len(b):
            a.append(0)
        elif len(b) < len(a):
            b.append(0)

def zero(n):
    zs = [0]*n
    return zs
print("zero",zero(1))

def zero(n):
    return [0 for i in range(n)]
print("zero",zero(1))

def vector(a):
    a = a[:]
    return a
print("vector",vector(a))

def add(a,b):
    a=a[:]
    b=b[:]
    pomozna(a,b)
    return [a*b for a,b in zip (a,b)]
print("add",add(a,b))

def iadd(a,b):
    b=b[:]
    pomozna(a,b)
    for i,(x,y) in enumerate(zip(a,b)):
        a[i] = x+y
print("iadd",iadd(a,b))

def sub(a,b):
    a=a[:]
    b=b[:]
    pomozna(a,b)
    return [a-b for a,b in zip(a,b)]
print("sub",sub(a,b))

def isub(a,b):
    b=b[:]
    pomozna(a,b)
    for i,(x,y) in enumerate(zip(a,b)):
        a[i] = x-y
print("isub",isub(a,b))

def mul(a,k):
    return [a*k for a in a]
print("mul",mul(a,3))

def imul(a,k):
    for i,x in enumerate(a):
        a[i] = x*k
print("imul",imul(a,2))

def inner(a,b):
    return sum([a*b for a,b in zip(a,b)])
print("inner",inner(a,b))

def euclid(a,b):
    a = sub(a,b)
    a = [math.pow(a,2) for a in a]
    return math.sqrt(sum(a))
print("euclid",euclid(a,b))

s = [[1,2,3],[2,3,4],[3,4,5],[3,4,5]]
def median(s):
    vektor = s
    xs = []
    for vek1 in vektor:
        zs = []
        for vek2 in vektor:
            zs.append(euclid(vek1,vek2))
        xs.append(sum(zs)/len(s))
    i = xs.index(min(xs))
    return vektor[i]
print("www",median(s))


import unittest

class VectorTest(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(zero(0), [])
        self.assertEqual(zero(1), [0])
        self.assertEqual(zero(10), [0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

    def test_vector(self):
        x = [5, 1, 1, 2, 1, 1234978, 0, -1234]
        y = vector(x)
        self.assertEqual(x, y)
        y[0] += 1
        self.assertNotEqual(x, y)

    def test_add(self):
        x = [1234, -1234, 1, 5, 2, 4]
        y = [9, 8, 3]
        z = [1243, -1226, 4, 5, 2, 4]
        self.assertEqual(add(x, y), z)
        self.assertEqual(x, [1234, -1234, 1, 5, 2, 4])
        self.assertEqual(y, [9, 8, 3])

        self.assertEqual(add(y, x), z)
        self.assertEqual(x, [1234, -1234, 1, 5, 2, 4])
        self.assertEqual(y, [9, 8, 3])

    def test_iadd(self):
        x = [7, 3, 9, 0]
        y = [1, 2]
        self.assertIsNone(iadd(x, y), None)
        self.assertEqual(x, [8, 5, 9, 0])
        self.assertEqual(y, [1, 2])

        x = [-7, 0, 7]
        y = [1, 2, 3, 4, 5]
        self.assertIsNone(iadd(x, y), None)
        self.assertEqual(x, [-6, 2, 10, 4, 5])
        self.assertEqual(y, [1, 2, 3, 4, 5])

    def test_sub(self):
        x = [1, 2, 3]
        y = [1, 2, 3, 4]
        self.assertEqual(sub(x, y), [0, 0, 0, -4])
        self.assertEqual(x, [1, 2, 3])
        self.assertEqual(y, [1, 2, 3, 4])

        self.assertEqual(sub(y, x), [0, 0, 0, 4])
        self.assertEqual(x, [1, 2, 3])
        self.assertEqual(y, [1, 2, 3, 4])

    def test_isub(self):
        x = [9, 1, -3, 0]
        y = [4, 2, 1]
        self.assertIsNone(isub(x, y), None)
        self.assertEqual(x, [5, -1, -4, 0])
        self.assertEqual(y, [4, 2, 1])

        x = [4, 2, 1]
        y = [9, 1, -3, 0]
        self.assertIsNone(isub(x, y), None)
        self.assertEqual(x, [-5, 1, 4, 0])
        self.assertEqual(y, [9, 1, -3, 0])

    def test_mul(self):
        x = [0, 4, 1, -4, 5]

        self.assertEqual(mul(x, 0), [0, 0, 0, 0, 0])
        self.assertEqual(mul(x, 1), [0, 4, 1, -4, 5])
        self.assertEqual(mul(x, 2), [0, 8, 2, -8, 10])
        self.assertEqual(x, [0, 4, 1, -4, 5])

    def test_imul(self):
        x = [4, 1, 0]
        self.assertIsNone(imul(x, 0))
        self.assertEqual(x, [0, 0, 0])

        x = [-1, 3, 5, 6]
        self.assertIsNone(imul(x, -2))
        self.assertEqual(x, [2, -6, -10, -12])

    def test_inner(self):
        self.assertEqual(inner([], []), 0)
        self.assertEqual(inner([1, 5, 3], []), 0)
        self.assertEqual(inner([], [2]), 0)
        self.assertEqual(inner([1, 4, -3], [3, -4, 7, 2]), -34)
        self.assertEqual(inner([1, 2, 3], [3, 2]), 7)

        x = [1, 2, 3]
        y = [4, 5, 6]
        inner(x, y)
        self.assertEqual(x, [1, 2, 3])
        self.assertEqual(y, [4, 5, 6])

    def test_euclid(self):
        self.assertAlmostEqual(euclid([1, 2], [3, 4]), 2.828427124746190)
        self.assertAlmostEqual(euclid([1], [3, 4]), 4.47213595499958)
        self.assertAlmostEqual(euclid([1, 2], [3]), 2.828427124746190)
        self.assertAlmostEqual(euclid([1, 2, -3, 0, 0, 1], [3, 1, 3, 8, -3]), 10.723805294763608)

        x = [1, 2, 3]
        y = [4, 5, 6]
        euclid(x, y)
        self.assertEqual(x, [1, 2, 3])
        self.assertEqual(y, [4, 5, 6])

    def test_median(self):
        self.assertEqual(median([[]]), [])
        self.assertEqual(median([[], [1], [1, 2], [3]]), [1])
        self.assertEqual(median([[1, 1, 1], [3, 2, 1], [1, 0, 3], [1, 2, 3], [4, 4, 4]]), [1, 2, 3])
        self.assertEqual(median([[1, 1], [2, 1], [3], [], [4, 4, 4], [-1, 1]]), [1, 1])
        self.assertEqual(median([[1], [1, 2, 1], [3, 4], [], [4, 4], [1], [2], [1, 1]]), [1, 1])
        self.assertEqual(median([[4, 6, 5], [1, 0], [7, 2, 8]]), [4, 6, 5])
        self.assertEqual(median([[-7, -10, -6, 10], [2, -4], [10, -6], [0, -10, -4], [10, 4, 10, -4, 1]]), [2, -4])
        self.assertEqual(median([[0, 7, 10], [-5, -3], [-8]]), [-8])
        self.assertEqual(median([[7, 10], [5, 9, -4], [4, -4, -1]]), [5, 9, -4])
        self.assertEqual(median([[-5, -5, 0], [-7], [6]]), [-5, -5, 0])
        self.assertEqual(median([[4], [-10, -8], [-9, -10, 9, 10, 6], [-8], [9, -5, 4, -10], [-2, -4, 6], [-6]]), [-6])
        v = [-7, -2]
        self.assertIs(median([v, [-1], [-8, -2]]), v)

if __name__ == '__main__':
    unittest.main(verbosity=2)