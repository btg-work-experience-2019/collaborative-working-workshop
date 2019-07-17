import unittest
from firstname_secondname import FirstnameSecondname

class nametest(unittest.TestCase):
    def test_print_name(self):
        DanielOne = FirstnameSecondname("Daniel","Paz")
        self.assertEqual(DanielOne.print_name(), "DanielPaz")
