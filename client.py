import socket
import time
from socket import AF_INET, SOCK_STREAM
from threading import Thread

HOST = '127.0.0.1'
PORT = 6663
BUFF = 4096
UTF8 = 'utf-8'

client_socket = socket.socket(AF_INET, SOCK_STREAM)
username = input("what is your username? ")


def receive(client):
    while True:
        try:
            data = client.recv(BUFF)
            time.sleep(0.1)
            if len(data):
                print(f'\r  >{data.decode(UTF8)}')
        except:
            print('general failure')


def send(client):

    main_flag = True

    while main_flag:
        try:
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
    client_socket.send(bytes(f"username#{username}"))

    try:
        read_thread = Thread(target=receive, args=(client_socket,), daemon=True)
        read_thread.start()

        send_thread = Thread(target=send, args=(client_socket,), daemon=True)
        send_thread.start()

        send_thread.join()

    except KeyboardInterrupt as e:
        print('CLIENT CLOSED main', str(e))


if __name__ == "__main__":
    run_program()
