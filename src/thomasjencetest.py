import unittest
from thomasjence import FirstnameSecondname

class FirstnameSecondnameTest(unittest.TestCase):
    def test_return_name(self):
        me=FirstnameSecondname('ThomasJence')
        self.assertEqual(me.return_name(), 'ThomasJence')
