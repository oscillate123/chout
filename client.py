import socket
import select
import errno
import sys
from threading import Thread
import time


HEADER_LENGTH = 10

HOST = "127.0.0.1"
PORT = 1234
UTF8 = 'utf-8'

my_username = input("Username: ")
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST,PORT))
client_socket.setblocking(False)

username = my_username.encode(UTF8)
username_header = f"{len(username):<{HEADER_LENGTH}}".encode(UTF8)
client_socket.send(username_header + username)
client_socket.setblocking(1)

def receive(client):
    global HEADER_LENGTH
    while 1:
        time.sleep(0.5)
        try:
            username_header = client.recv(HEADER_LENGTH)
            if not len(username_header):
                print("Connection closed by the server")
                sys.exit()
            username_length = int(username_header.decode(UTF8).strip())
            username = client.recv(username_length).decode(UTF8)

            message_header = client.recv(HEADER_LENGTH)
            message_length = int(message_header.decode(UTF8).strip())
            message = client.recv(message_length).decode(UTF8)

            print(f"\r\n{username} > {message}")
        except Exception as e:
            print(e)


def send(client):
    while 1:
        try:
<<<<<<< HEAD
            message = input(f"{my_username} > ")
            if message:
                message = message.encode(UTF8)
                message_header = f"{len(message):<{HEADER_LENGTH}}".encode(UTF8)
                client.send(message_header + message)
        except Exception as e:
            print(e)

=======
            payload = input('')
            if len(payload):
                client.send(payload.encode(UTF8))
        except BrokenPipeError as e:
            print('Lost connection', str(e))
            client.close()
            retry = input('Do you want to reconnect? y/N')
            if 'y' in retry:
                try:
                    run_program()
                except:
                    print('General error, closing.')
                    main_flag = False


def run_program():
    client_socket.connect((HOST, PORT))
    client_socket.send(f"username#{username}".encode())
>>>>>>> f29784504f0ab430c173a618bc519378d851813b

if __name__ == "__main__":
    try:
        read_thread = Thread(target=receive, args=(client_socket,), daemon=True)
        read_thread.start()

        send_thread = Thread(target=send, args=(client_socket,), daemon=True)
        send_thread.start()

        send_thread.join()


    except IOError as e:
        if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
            print('Reading error',str(e))
            sys.exit()

    except Exception as e:
        print('General error',str(e))
        sys.exit()