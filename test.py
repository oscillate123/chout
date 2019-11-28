import unittest
import server
from server import findReceivers
from server import create_message


class TestFunctions(unittest.TestCase):

	def test_receivers(self):
		msg = "@oscar @wille hejhej"
		receivers = findReceivers(msg)
		correct = ["oscar", "wille"]

		self.assertEqual(correct, receivers, msg="findReceivers failed, check msg")

	def test_servermessage_create(self):
		HEADER_LENGTH = 10

		user = "oscar"
		user_data = user.encode('utf-8')
		user_header = f"{len(user):<{HEADER_LENGTH}}".encode('utf-8')
		user_payload = {"header": user_header, "data": user_data}

		message = "testing awesome stuff"
		message_data = message.encode('utf-8')
		message_header = f"{len(message):<{HEADER_LENGTH}}".encode('utf-8')
		message_payload = {"header": message_header, "data": message_data}

		correct_user, correct_message = create_message(user=user, message=message)

		self.assertEqual(correct_user, user_payload, msg="create_message failed, check user")
		self.assertEqual(correct_message, message_payload, msg="create_message failed, check message")


if __name__ == '__main__':
	unittest.main()


# {'header': b'15        ', 'data': b'##USER_JOINED##'} 
# {'header': b'44        ', 'data': b'wille joined the server from 127.0.0.1:37514'}

# def create_message(user, message):
#     user_data = user.encode(UTF8)
#     user_header = f"{len(user):<{HEADER_LENGTH}}".encode(UTF8)
#     user = {"header": user_header, "data": user_data}

#     message_data = message.encode(UTF8)
#     message_header = f"{len(message):<{HEADER_LENGTH}}".encode(UTF8)
#     message = {"header": message_header, "data": message_data}

#     return user, message