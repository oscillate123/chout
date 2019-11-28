import unittest
import server
from server import findReceivers


class TestFunctions(unittest.TestCase):

    def test_receivers(self):
	    msg = "@oscar @wille hejhej"
	    receivers = findReceivers(msg)
	    correct = ["oscar", "wille"]

	    self.assertEqual(correct, receivers, msg="findReceivers not working")

	def test_send(self):
		pass


if __name__ == '__main__':
    unittest.main()