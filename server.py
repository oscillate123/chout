import socket
import select
from threading import Thread

HEADER_LENGTH = 10
IP = "127.0.0.1"
PORT = 65432
UTF8 = 'utf-8'

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((IP,PORT))
server_socket.listen()

socketlist = [server_socket]
clients = {}
users = []


def create_message(user, message):
    user_data = user.encode(UTF8)
    user_header = f"{len(user):<{HEADER_LENGTH}}".encode(UTF8)
    user = {"header": user_header, "data": user_data}

    message_data = message.encode(UTF8)
    message_header = f"{len(message):<{HEADER_LENGTH}}".encode(UTF8)
    message = {"header": message_header, "data": message_data}

    return user, message


def receive_message(client, client_address=None):
    try:
        message_header = client.recv(HEADER_LENGTH)

        if not len(message_header):
            return False

        message_length = int(message_header.decode(UTF8).strip())
        return {"header": message_header, "data": client.recv(message_length)}

    except:
        return False


def findReceivers(message):
    receivers = []
    word_list = message.split(" ")
    for word in word_list:
        try:
            if word[0] != "@":
                break
            else:
                receivers.append(word[1:])
        except Exception as e:
            print(e)
    return receivers


if __name__ == "__main__":
    while True:
        read_sockets, _, exception_sockets = select.select(socketlist, [], socketlist)
        
        for socket in read_sockets:
            if socket == server_socket:
                client_object, client_address = server_socket.accept()

                user = receive_message(client_object)
                if user is False:
                    continue

                socketlist.append(client_object)

                clients[client_object] = user
                
                print(f"Accepted new connection from {client_address[0]}:{client_address[1]} username:{user['data'].decode(UTF8)}")
                user, message = create_message("##USER_JOINED##", f"{user['data'].decode(UTF8)} joined the server from {client_address[0]}:{client_address[1]}")
                for client_object in clients:
                    client_object.send(user['header'] + user['data'] + message['header'] + message['data'])
                

            else:
                message = receive_message(socket)

                if message is False:
                    print(f"Closed connection from {clients[socket]['data'].decode(UTF8)}")
                    user, message = create_message("##USER_LEFT##", f"{clients[socket]['data'].decode(UTF8)} left the server")
                    for client_object in clients:
                        client_object.send(user['header'] + user['data'] + message['header'] + message['data'])
                    socketlist.remove(socket)
                    del clients[socket]
                    continue

                user = clients[socket]
                
                print(f"Received message from {user['data'].decode(UTF8)}: {message['data'].decode(UTF8)}")
                
                receivers = findReceivers(message['data'].decode(UTF8))
                
                for client_object in clients:

                    if receivers:
                        if clients[client_object]['data'].decode(UTF8) in receivers:
                            client_object.send(user['header'] + user['data'] + message['header'] + message['data'])
                    else:
                        if client_object != socket:
                            client_object.send(user['header'] + user['data'] + message['header'] + message['data'])

        for socket in exception_sockets:
            socketlist.remove(socket)
            del clients[socket]
