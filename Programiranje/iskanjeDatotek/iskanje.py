import os
import collections
import pprint

direktorij =".\\dn8_tree"

def preisci0(dir,slovar):
    dir_xs = []
    for xName in os.listdir(dir):
        dirList = os.path.join(dir,xName)
        if os.path.isdir(dirList):
            dir_xs.extend(preisci0(dirList,slovar))
        elif os.path.isfile(dirList):
            dir_xs.append(dirList)
    return dir_xs

def preisci(dir):
    slovar = collections.defaultdict(list)
    xs = preisci0(dir,slovar)
    for l in xs:
        ime_dat, ime_dir= os.path.split(l)
        #normpath /normcase
        ime_dat = ime_dat.replace("\\","/")
        slovar[ime_dir].append(ime_dat)
    return slovar

slovar = preisci(direktorij)
print("preisci",slovar)

def isci(arg,slovar):
    imenik = collections.defaultdict(list)

    for ime_dat, ime_dir in slovar.items():
        if arg in ime_dat:
            imenik[ime_dat] = ime_dir
    return imenik
isci = isci("knjiznica",slovar)
print("isci",isci)

def trojke(slovar):
    imenik = collections.defaultdict(set)
    for k in slovar.keys():
        for i in range(len(k)-2):
            if k[i:i+3] in k:
                imenik[k[i:i+3]].add(k)
    return imenik
trojke = trojke(slovar)

print("trojke",trojke)

import unittest
import os
import shutil
import tempfile
from urllib.request import urlopen

VERSION = "3"

class TestDN8(unittest.TestCase):
    @classmethod
    def setUpClass(cls):

        ver = urlopen('http://butler.fri.uni-lj.si/jure/dn8_version').read().strip().decode()
        if VERSION != ver:
            raise RuntimeError('Nova verzija testov je na voljo na učilnici.')

        structure = [
          'makefile',
          'empty/',
          'obj/lib/knjiznica.so',
          'obj/knjiznica',
          'src/makefile',
          'src/knjiznica.c',
          'src/knjiznica.h',
          'src/knjiznica.py',
          'src/xnji7ni1234512345ca.yp',
          'src/kknji7ni12345ca.yp',
          'src/xnji7n12345ca.yp',
          'src/main.c',
          'src/moin.c',
          'src/maain.c',
          'src/ma12345in.c',
          'src/ainmaiin.c',
          'src/1233333333333333333345.c',
          'src/1233niam3345.cniam3345.c',
          'src/e233niam3345.cniam3345.x',
          'src/1233niam3345.cniam3345.py',
          'src/foo/main.c',
          'src/foo/knjiznica.py',
          'src/bar/knjiznica.py',
          'src/foo/bar/baz/qux/quux/corge/grault/makefile',
          'src/foo/bar/baz/qux/quux/corge/grault/knjiznica.c',
          'src/foo/bar/baz/qux/quux/corge/grault/knjizniii_iiica.cpp',
          'src/foo/bar/baz/qux/quux/corge/grault/knjiznica.h',
          'src/foo/bar/baz/qux/quux/corge/grault/knjiznica.py',
        ]

        cls.tempdir = tempfile.mkdtemp()
        os.chdir(cls.tempdir)
        for entry in structure:
            head, tail = os.path.split(entry)
            if head:
                os.makedirs(os.path.split(entry)[0], exist_ok=True)
            if tail:
                open(entry, 'w').close()


    @classmethod
    def tearDownClass(cls):
        os.chdir(os.path.join(cls.tempdir, '..'))
        shutil.rmtree(cls.tempdir)


    def assertDictListEqual(self, d1, d2):
        self.assertEqual(len(d1), len(d2))
        for k in d1:
            self.assertCountEqual(map(os.path.normpath, d1[k]), map(os.path.normpath, d2[k]))


    def test_preisci(self):
        self.assertDictListEqual(preisci('empty'), {})
        self.assertDictListEqual(preisci('src/bar'), {'knjiznica.py': ['src/bar']})
        self.assertDictListEqual(preisci('obj'),
            {'knjiznica.so': ['obj/lib'], 'knjiznica': ['obj']})
        self.assertDictListEqual(preisci('.'),
            {'1233333333333333333345.c': ['./src'],
             '1233niam3345.cniam3345.c': ['./src'],
             '1233niam3345.cniam3345.py': ['./src'],
             'ainmaiin.c': ['./src'],
             'e233niam3345.cniam3345.x': ['./src'],
             'kknji7ni12345ca.yp': ['./src'],
             'knjiznica': ['./obj'],
             'knjiznica.c': ['./src/foo/bar/baz/qux/quux/corge/grault', './src'],
             'knjiznica.h': ['./src', './src/foo/bar/baz/qux/quux/corge/grault'],
             'knjiznica.py': ['./src',
                              './src/bar',
                              './src/foo',
                              './src/foo/bar/baz/qux/quux/corge/grault'],
             'knjiznica.so': ['./obj/lib'],
             'knjizniii_iiica.cpp': ['./src/foo/bar/baz/qux/quux/corge/grault'],
             'ma12345in.c': ['./src'],
             'maain.c': ['./src'],
             'main.c': ['./src', './src/foo'],
             'makefile': ['.', './src', './src/foo/bar/baz/qux/quux/corge/grault'],
             'moin.c': ['./src'],
             'xnji7n12345ca.yp': ['./src'],
             'xnji7ni1234512345ca.yp': ['./src']})


    def test_isci(self):
        self.assertDictListEqual(isci(preisci('obj'), 'knjiznica'),
            {'knjiznica': ['obj'], 'knjiznica.so': ['obj/lib']})
        self.assertDictListEqual(isci(preisci('src'), 'makefile'),
            {'makefile': ['src', 'src/foo/bar/baz/qux/quux/corge/grault']})
        drevo = preisci('.')
        self.assertDictListEqual(isci(drevo, 'neobstaja'), {})
        self.assertDictListEqual(isci(drevo, 'knjiznica'),
            {'knjiznica': ['./obj'],
             'knjiznica.c': ['./src/foo/bar/baz/qux/quux/corge/grault', './src'],
             'knjiznica.h': ['./src', './src/foo/bar/baz/qux/quux/corge/grault'],
             'knjiznica.py': ['./src',
                              './src/bar',
                              './src/foo',
                              './src/foo/bar/baz/qux/quux/corge/grault'],
             'knjiznica.so': ['./obj/lib']})
        self.assertDictListEqual(isci(drevo, 'njiznica.p'),
            {'knjiznica.py': ['./src',
                              './src/bar',
                              './src/foo',
                              './src/foo/bar/baz/qux/quux/corge/grault']})
        self.assertDictListEqual(isci(drevo, 'main.c'), {'main.c': ['./src', './src/foo']})


    def test_trojke(self):
        self.assertDictEqual(trojke(preisci('empty')), {})
        self.assertDictEqual(trojke(preisci('src/bar')),
            {'.py': {'knjiznica.py'},
             'a.p': {'knjiznica.py'},
             'ca.': {'knjiznica.py'},
             'ica': {'knjiznica.py'},
             'izn': {'knjiznica.py'},
             'jiz': {'knjiznica.py'},
             'knj': {'knjiznica.py'},
             'nic': {'knjiznica.py'},
             'nji': {'knjiznica.py'},
             'zni': {'knjiznica.py'}})

        self.assertDictEqual(trojke(preisci('obj')),
            {'.so': {'knjiznica.so'},
             'a.s': {'knjiznica.so'},
             'ca.': {'knjiznica.so'},
             'ica': {'knjiznica.so', 'knjiznica'},
             'izn': {'knjiznica.so', 'knjiznica'},
             'jiz': {'knjiznica.so', 'knjiznica'},
             'knj': {'knjiznica.so', 'knjiznica'},
             'nic': {'knjiznica.so', 'knjiznica'},
             'nji': {'knjiznica.so', 'knjiznica'},
             'zni': {'knjiznica.so', 'knjiznica'}})

        self.assertDictEqual(trojke(preisci('.')),
            {'.cn': {'1233niam3345.cniam3345.c',
                     '1233niam3345.cniam3345.py',
                     'e233niam3345.cniam3345.x'},
             '.cp': {'knjizniii_iiica.cpp'},
             '.py': {'1233niam3345.cniam3345.py', 'knjiznica.py'},
             '.so': {'knjiznica.so'},
             '.yp': {'kknji7ni12345ca.yp', 'xnji7n12345ca.yp', 'xnji7ni1234512345ca.yp'},
             '123': {'1233333333333333333345.c',
                     '1233niam3345.cniam3345.c',
                     '1233niam3345.cniam3345.py',
                     'kknji7ni12345ca.yp',
                     'ma12345in.c',
                     'xnji7n12345ca.yp',
                     'xnji7ni1234512345ca.yp'},
             '233': {'1233333333333333333345.c',
                     '1233niam3345.cniam3345.c',
                     '1233niam3345.cniam3345.py',
                     'e233niam3345.cniam3345.x'},
             '234': {'kknji7ni12345ca.yp',
                     'ma12345in.c',
                     'xnji7n12345ca.yp',
                     'xnji7ni1234512345ca.yp'},
             '333': {'1233333333333333333345.c'},
             '334': {'1233333333333333333345.c',
                     '1233niam3345.cniam3345.c',
                     '1233niam3345.cniam3345.py',
                     'e233niam3345.cniam3345.x'},
             '33n': {'1233niam3345.cniam3345.c',
                     '1233niam3345.cniam3345.py',
                     'e233niam3345.cniam3345.x'},
             '345': {'1233333333333333333345.c',
                     '1233niam3345.cniam3345.c',
                     '1233niam3345.cniam3345.py',
                     'e233niam3345.cniam3345.x',
                     'kknji7ni12345ca.yp',
                     'ma12345in.c',
                     'xnji7n12345ca.yp',
                     'xnji7ni1234512345ca.yp'},
             '3ni': {'1233niam3345.cniam3345.c',
                     '1233niam3345.cniam3345.py',
                     'e233niam3345.cniam3345.x'},
             '45.': {'1233333333333333333345.c',
                     '1233niam3345.cniam3345.c',
                     '1233niam3345.cniam3345.py',
                     'e233niam3345.cniam3345.x'},
             '451': {'xnji7ni1234512345ca.yp'},
             '45c': {'kknji7ni12345ca.yp', 'xnji7n12345ca.yp', 'xnji7ni1234512345ca.yp'},
             '45i': {'ma12345in.c'},
             '5.c': {'1233333333333333333345.c',
                     '1233niam3345.cniam3345.c',
                     '1233niam3345.cniam3345.py',
                     'e233niam3345.cniam3345.x'},
             '5.p': {'1233niam3345.cniam3345.py'},
             '5.x': {'e233niam3345.cniam3345.x'},
             '512': {'xnji7ni1234512345ca.yp'},
             '5ca': {'kknji7ni12345ca.yp', 'xnji7n12345ca.yp', 'xnji7ni1234512345ca.yp'},
             '5in': {'ma12345in.c'},
             '7n1': {'xnji7n12345ca.yp'},
             '7ni': {'kknji7ni12345ca.yp', 'xnji7ni1234512345ca.yp'},
             '_ii': {'knjizniii_iiica.cpp'},
             'a.c': {'knjiznica.c', 'knjizniii_iiica.cpp'},
             'a.h': {'knjiznica.h'},
             'a.p': {'knjiznica.py'},
             'a.s': {'knjiznica.so'},
             'a.y': {'kknji7ni12345ca.yp', 'xnji7n12345ca.yp', 'xnji7ni1234512345ca.yp'},
             'a12': {'ma12345in.c'},
             'aai': {'maain.c'},
             'aii': {'ainmaiin.c'},
             'ain': {'maain.c', 'main.c', 'ainmaiin.c'},
             'ake': {'makefile'},
             'am3': {'1233niam3345.cniam3345.c',
                     '1233niam3345.cniam3345.py',
                     'e233niam3345.cniam3345.x'},
             'ca.': {'kknji7ni12345ca.yp',
                     'knjiznica.c',
                     'knjiznica.h',
                     'knjiznica.py',
                     'knjiznica.so',
                     'knjizniii_iiica.cpp',
                     'xnji7n12345ca.yp',
                     'xnji7ni1234512345ca.yp'},
             'cni': {'1233niam3345.cniam3345.c',
                     '1233niam3345.cniam3345.py',
                     'e233niam3345.cniam3345.x'},
             'cpp': {'knjizniii_iiica.cpp'},
             'e23': {'e233niam3345.cniam3345.x'},
             'efi': {'makefile'},
             'fil': {'makefile'},
             'i12': {'kknji7ni12345ca.yp', 'xnji7ni1234512345ca.yp'},
             'i7n': {'kknji7ni12345ca.yp', 'xnji7n12345ca.yp', 'xnji7ni1234512345ca.yp'},
             'i_i': {'knjizniii_iiica.cpp'},
             'iam': {'1233niam3345.cniam3345.c',
                     '1233niam3345.cniam3345.py',
                     'e233niam3345.cniam3345.x'},
             'ica': {'knjiznica',
                     'knjiznica.c',
                     'knjiznica.h',
                     'knjiznica.py',
                     'knjiznica.so',
                     'knjizniii_iiica.cpp'},
             'ii_': {'knjizniii_iiica.cpp'},
             'iic': {'knjizniii_iiica.cpp'},
             'iii': {'knjizniii_iiica.cpp'},
             'iin': {'ainmaiin.c'},
             'ile': {'makefile'},
             'in.': {'maain.c', 'main.c', 'ma12345in.c', 'ainmaiin.c', 'moin.c'},
             'inm': {'ainmaiin.c'},
             'izn': {'knjiznica',
                     'knjiznica.c',
                     'knjiznica.h',
                     'knjiznica.py',
                     'knjiznica.so',
                     'knjizniii_iiica.cpp'},
             'ji7': {'kknji7ni12345ca.yp', 'xnji7n12345ca.yp', 'xnji7ni1234512345ca.yp'},
             'jiz': {'knjiznica',
                     'knjiznica.c',
                     'knjiznica.h',
                     'knjiznica.py',
                     'knjiznica.so',
                     'knjizniii_iiica.cpp'},
             'kef': {'makefile'},
             'kkn': {'kknji7ni12345ca.yp'},
             'knj': {'kknji7ni12345ca.yp',
                     'knjiznica',
                     'knjiznica.c',
                     'knjiznica.h',
                     'knjiznica.py',
                     'knjiznica.so',
                     'knjizniii_iiica.cpp'},
             'm33': {'1233niam3345.cniam3345.c',
                     '1233niam3345.cniam3345.py',
                     'e233niam3345.cniam3345.x'},
             'ma1': {'ma12345in.c'},
             'maa': {'maain.c'},
             'mai': {'main.c', 'ainmaiin.c'},
             'mak': {'makefile'},
             'moi': {'moin.c'},
             'n.c': {'maain.c', 'main.c', 'ma12345in.c', 'ainmaiin.c', 'moin.c'},
             'n12': {'xnji7n12345ca.yp'},
             'ni1': {'kknji7ni12345ca.yp', 'xnji7ni1234512345ca.yp'},
             'nia': {'1233niam3345.cniam3345.c',
                     '1233niam3345.cniam3345.py',
                     'e233niam3345.cniam3345.x'},
             'nic': {'knjiznica',
                     'knjiznica.c',
                     'knjiznica.h',
                     'knjiznica.py',
                     'knjiznica.so'},
             'nii': {'knjizniii_iiica.cpp'},
             'nji': {'kknji7ni12345ca.yp',
                     'knjiznica',
                     'knjiznica.c',
                     'knjiznica.h',
                     'knjiznica.py',
                     'knjiznica.so',
                     'knjizniii_iiica.cpp',
                     'xnji7n12345ca.yp',
                     'xnji7ni1234512345ca.yp'},
             'nma': {'ainmaiin.c'},
             'oin': {'moin.c'},
             'xnj': {'xnji7n12345ca.yp', 'xnji7ni1234512345ca.yp'},
             'zni': {'knjiznica',
                     'knjiznica.c',
                     'knjiznica.h',
                     'knjiznica.py',
                     'knjiznica.so',
                     'knjizniii_iiica.cpp'}})


    def test_isci_hitro(self):
        drevo = preisci('obj')
        self.assertDictListEqual(isci_hitro(drevo, trojke(drevo), 'knjiznica'),
            {'knjiznica': ['obj'], 'knjiznica.so': ['obj/lib']})
        drevo = preisci('src')
        self.assertDictListEqual(isci_hitro(drevo, trojke(drevo), 'makefile'),
            {'makefile': ['src', 'src/foo/bar/baz/qux/quux/corge/grault']})
        drevo = preisci('.')
        self.assertDictListEqual(isci_hitro(drevo, trojke(drevo), 'neobstaja'), {})
        self.assertDictListEqual(isci_hitro(drevo, trojke(drevo), 'knjiznica'),
            {'knjiznica': ['./obj'],
             'knjiznica.c': ['./src/foo/bar/baz/qux/quux/corge/grault', './src'],
             'knjiznica.h': ['./src', './src/foo/bar/baz/qux/quux/corge/grault'],
             'knjiznica.py': ['./src',
                              './src/bar',
                              './src/foo',
                              './src/foo/bar/baz/qux/quux/corge/grault'],
             'knjiznica.so': ['./obj/lib']})
        self.assertDictListEqual(isci_hitro(drevo, trojke(drevo), 'njiznica.p'),
            {'knjiznica.py': ['./src',
                              './src/bar',
                              './src/foo',
                              './src/foo/bar/baz/qux/quux/corge/grault']})
        self.assertDictListEqual(isci_hitro(drevo, trojke(drevo), 'main.c'),
            {'main.c': ['./src', './src/foo']})


    def test_isci_regex(self):
        drevo = preisci('.')
        self.assertDictListEqual(isci_regex(drevo, trojke(drevo), 'ain.c'), {})
        self.assertDictListEqual(isci_regex(drevo, trojke(drevo), 'knjiznica.?'),
            {'knjiznica.c': ['./src/foo/bar/baz/qux/quux/corge/grault', './src'],
             'knjiznica.h': ['./src', './src/foo/bar/baz/qux/quux/corge/grault']})
        self.assertCountEqual(isci_regex(drevo, trojke(drevo), 'main.c').keys(),
            ['main.c'])
        self.assertCountEqual(isci_regex(drevo, trojke(drevo), 'm?in.c').keys(),
            ['main.c', 'moin.c'])
        self.assertCountEqual(isci_regex(drevo, trojke(drevo), 'ma*in.c').keys(),
            ['maain.c', 'main.c', 'ma12345in.c'])
        self.assertCountEqual(isci_regex(drevo, trojke(drevo), 'knjiznica.*').keys(),
            ['knjiznica.h', 'knjiznica.so', 'knjiznica.c', 'knjiznica.py'])
        self.assertCountEqual(isci_regex(drevo, trojke(drevo), '?nji?ni*ca.??').keys(),
            ['knjiznica.py', 'xnji7ni1234512345ca.yp', 'knjiznica.so'])
        self.assertCountEqual(isci_regex(drevo, trojke(drevo), '1233*3345.c').keys(),
            ['1233333333333333333345.c', '1233niam3345.cniam3345.c'])
        self.assertCountEqual(isci_regex(drevo, trojke(drevo), '?233*3345.?').keys(),
            ['1233333333333333333345.c', '1233niam3345.cniam3345.c', 'e233niam3345.cniam3345.x'])
        self.assertCountEqual(isci_regex(drevo, trojke(drevo), '*').keys(),
            ['e233niam3345.cniam3345.x',
             'knjiznica.h',
             'xnji7ni1234512345ca.yp',
             'knjiznica.py',
             'main.c',
             'knjiznica.c',
             'makefile',
             'ainmaiin.c',
             'moin.c',
             'knjiznica',
             'knjiznica.so',
             '1233niam3345.cniam3345.c',
             'maain.c',
             'kknji7ni12345ca.yp',
             'xnji7n12345ca.yp',
             'knjizniii_iiica.cpp',
             '1233niam3345.cniam3345.py',
             'ma12345in.c',
             '1233333333333333333345.c'])


if __name__ == '__main__':
    unittest.main(verbosity=2)
