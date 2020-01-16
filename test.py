import unittest
from Lib import *
class TestStringMethods(unittest.TestCase):

    def test_suma(self):
        a=(3,2)
        b=(5,4)
        c=suma(a,b)
        self.assertEqual(c, (8,7))


if __name__ == '__main__':
    unittest.main()
