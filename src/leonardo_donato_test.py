import unittest
from leonardo_donato import LeonardoDonato

class LeonardoDonatoTest(unittest.TestCase):
    def test_print_name(self):
        leo_one = LeonardoDonato()
        self.assertEqual(leo_one.print_name(), "LeonardoDonato")
