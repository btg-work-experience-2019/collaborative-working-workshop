import unittest
from aleksandergornik import Alex

class testing_code101(unittest.TestCase):
      def test_return_name(self):
          me= Alex('aleksander gornik')
          self.assertEqual(me.return_name(),'aleksander gornik')
