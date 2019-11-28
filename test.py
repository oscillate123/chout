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
		



	# def create_message(user, message):
	#     user_data = user.encode(UTF8)
	#     user_header = f"{len(user):<{HEADER_LENGTH}}".encode(UTF8)
	#     user = {"header": user_header, "data": user_data}

	#     message_data = message.encode(UTF8)
	#     message_header = f"{len(message):<{HEADER_LENGTH}}".encode(UTF8)
	#     message = {"header": message_header, "data": message_data}

	#     return user, message


if __name__ == '__main__':
    unittest.main()
