import unittest
import server
from server import findRecievers

class TestStringMethods(unittest.TestCase):

    def test_receivers(self):
	    msg = "@oscar @wille hejhej"
	    receivers = findRecievers(msg)
	    correct = ["oscar", "wille"]

	    self.assertEqual(correct, receivers, msg="findReceivers not working")

if __name__ == '__main__':
    unittest.main()