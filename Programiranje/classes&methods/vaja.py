class WordDict():
        def __init__(self, v):
            """Create an empty dictionary, or update from 'dict'."""
            self._dict = dict(v)

        def __getitem__(self, key):
            """Retrieve the value associated with 'key' (in any case)."""
            k = key.lower()
            return self._dict[k][1]

        def __setitem__(self, key, value):
            """Associate 'value' with 'key'. If 'key' already exists, but
            in different case, it will be replaced."""
            k = key.lower()
            self._dict[k] = (key, value)

        def has_key(self, key):
            """Case insensitive test wether 'key' exists."""
            k = key.lower()
            return self._dict.has_key(k)

        def keys(self):
            """List of keys in their original case."""
            return [v[0] for v in self._dict.values()]

        def values(self):
            """List of values."""
            return [v[1] for v in self._dict.values()]

        def items(self):
            """List of (key,value) pairs."""
            return self._dict.values()

        def get(self, key, default=None):
            """Retrieve value associated with 'key' or return default value
            if 'key' doesn't exist."""
            try:
                return self[key]
            except KeyError:
                return default

        def setdefault(self, key, default):
            """If 'key' doesn't exists, associate it with the 'default' value.
            Return value associated with 'key'."""
            if not self.has_key(key):
                self[key] = default
            return self[key]

        def update(self, dict):
            """Copy (key,value) pairs from 'dict'."""
            for k,v in dict.items():
                self[k] = v

        def __repr__(self):
            """String representation of the dictionary."""
            items = ", ".join([("%r: %r" % (k,v)) for k,v in self.items()])
            return "{%s}" % items

        def __str__(self):
            """String representation of the dictionary."""
            return repr(self)


v = {"ana":10}
velikost = WordDict(v)
velikost["AnA"] = 5
print(velikost["ANA"])


import unittest

class TestWordDict(unittest.TestCase):
    def setUp(self):
        # Pred vsakim testom ustvarimo tri objekte razreda WordDict.
        self.d1 = WordDict([])
        self.d2 = WordDict(
            [('i have', 'Imam'),
            ('He Has', 'ima'),
            ('sHE hAS', 'ima')])
        self.d3 = WordDict(
            [('pRime', [2, 3, 5]),
             ('EVEN', [2, 4, 6]),
             ('Odd', [1, 3, 5]),
             ('Pi', 3.14),
             ('E', 2.71828)])

    def test_keys(self):
        self.assertCountEqual(self.d1.keys(), [])
        self.assertCountEqual(self.d2.keys(),
            ['i have', 'He Has', 'sHE hAS'])
        self.assertCountEqual(self.d3.keys(),
            ['pRime', 'EVEN', 'Odd', 'Pi', 'E'])

    def test_values(self):
        self.assertCountEqual(self.d1.values(), [])
        self.assertCountEqual(self.d2.values(),
            ['Imam', 'ima', 'ima'])
        self.assertCountEqual(self.d3.values(),
            [[2, 3, 5], [2, 4, 6], [1, 3, 5], 3.14, 2.71828])

    def test_items(self):
        self.assertCountEqual(self.d1.items(), [])
        self.assertCountEqual(self.d2.items(),
            [('i have', 'Imam'), ('sHE hAS', 'ima'), ('He Has', 'ima')])
        self.assertCountEqual(self.d3.items(),
            [('pRime', [2, 3, 5]),
            ('EVEN', [2, 4, 6]),
            ('Pi', 3.14),
            ('Odd', [1, 3, 5]),
            ('E', 2.71828)])

    def test_getitem(self):
        self.assertEqual(self.d2['I HAVE'], 'Imam')
        self.assertEqual(self.d3['PRIme'], [2, 3, 5])
        self.assertEqual(self.d3['eVeN'], [2, 4, 6])
        self.assertEqual(self.d3['PI'], 3.14)
        self.assertEqual(self.d3['pi'], 3.14)
        self.assertEqual(self.d3['Pi'], 3.14)

    def test_setitem(self):
        self.d1['C++'] = 'Stroustrup'
        self.d1['Go'] = 'Pike'
        self.assertCountEqual(self.d1.items(),
            [('C++', 'Stroustrup'), ('Go', 'Pike')])
        self.d1['GO'] = 'Thompson'
        self.assertCountEqual(self.d1.items(),
            [('C++', 'Stroustrup'), ('GO', 'Thompson')])
        self.d1['go'] += ', Pike'
        self.assertCountEqual(self.d1.items(),
            [('C++', 'Stroustrup'), ('go', 'Thompson, Pike')])

    def test_len(self):
        self.assertEqual(len(self.d1), 0)
        self.assertEqual(len(self.d2), 3)
        self.assertEqual(len(self.d3), 5)
        self.assertEqual(len(WordDict([('A', 1), ('a', 1)])), 1)

    def test_all(self):
        italian = WordDict([('hvala', 'grazie')])

        self.assertEqual(len(italian), 1)
        italian['nasvIdenje'] = 'Arrivederci'
        italian['IN'] = 'e'
        self.assertEqual(len(italian), 3)

        italian['NASVIDENJE'] = 'arrivederci'
        self.assertEqual(len(italian), 3)

        it = []
        for word in 'nasvidenje in hvala'.split():
            it.append(italian[word])
        self.assertEqual(' '.join(it), 'arrivederci e grazie')

        self.assertCountEqual(italian.items(),
            [('hvala', 'grazie'), ('IN', 'e'), ('NASVIDENJE', 'arrivederci')])

if __name__ == '__main__':
    unittest.main(verbosity=2)
