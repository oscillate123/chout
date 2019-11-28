import socket
import errno
import sys
from threading import Thread
import time
from appJar import gui

app = gui()

HEADER_LENGTH = 10
HOST = "127.0.0.1"
PORT = 65432
UTF8 = 'utf-8'
my_username = input("Username: ")


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST,PORT))
client_socket.setblocking(False)

username = my_username.encode(UTF8)
username_header = f"{len(username):<{HEADER_LENGTH}}".encode(UTF8)
client_socket.send(username_header + username)
client_socket.setblocking(1)

users = []

def receive(client):
    main_flag = True
    while main_flag:
        time.sleep(0.5)
        try:
            username_header = client.recv(HEADER_LENGTH)
            if not len(username_header):
                warning_box("Connection closed by the server")
                sys.exit()
            username_length = int(username_header.decode(UTF8).strip())
            username = client.recv(username_length).decode(UTF8)

            message_header = client.recv(HEADER_LENGTH)
            message_length = int(message_header.decode(UTF8).strip())
            message = client.recv(message_length).decode(UTF8)
            

            if username == "##USER_JOINED##":
                username = "HOST"
                new_user = message.split()[0]
                if new_user == my_username:
                    continue
                users.append(new_user)
                app.clearListBox("connected")
                app.addListItems("connected", users)
            elif username == "##USER_LEFT##":
                username = "HOST"
                user_leaving = message.split()[0]
                users.remove(user_leaving)
                app.clearListBox("connected")
                app.addListItems("connected", users)
            elif username == "##USER_LIST##":
                username = "HOST"
                message = message.split()
                for word in message:
                    users.append(word)
                app.clearListBox("connected")
                app.addListItems("connected", users)
                continue
                
            else:
                pass

            # updates GUI
            update_inputs(f'{message_polishing(who=username, what=message)}')

        except Exception as e:
            warning_box(f'{e}')

def send(client, message):
    main_flag = True
    while main_flag:
        try:
            if message:
                message = message.encode(UTF8)
                message_header = f"{len(message):<{HEADER_LENGTH}}".encode(UTF8)
                client.send(message_header + message)
                return
            else:
                warning_box(f'Error sending message:\n{message}')
                return
        except BrokenPipeError as e:
            warning_box(f'Lost connection: {str(e)}')
            client.close()
        except Exception as e:
            warning_box(f'General error: {e}')

def message_polishing(who, what):
    return f' {who}:  {what}'

def warning_box(text):
    app.warningBox(title='temp_warning', message=f'Error!\n{text}')

def update_inputs(text):
    app.addListItem(title='chatbox', item=f'{text}', select=False)

def clearTextArea(TextArea):
    app.clearTextArea(title=f'{TextArea}', callFunction=False)

def click(buttontype):
    if buttontype == "Send":
        user_message = app.getTextArea('message')
        update_inputs(f'{message_polishing(who=my_username, what=user_message)}')
        Thread(target=send, args=(client_socket, user_message), daemon=True).start()
        clearTextArea('message')
    elif buttontype == "Clear chat":
        app.clearListBox(title='chatbox', callFunction=False)
    elif buttontype == 'Disconnect':
        client_socket.close()
        sys.exit()
    else:
        pass

def enterPress():
    if app.getFocus() == "message":
        click("Send")

# BODY SETTINGS
# app.setSize(x, y)
app.setSize(600, 600)
app.setFont(14)
app.setBg('LightGrey')
app.setTransparency(99)

# creating columns (y-axis)
for y in range(40):
    app.addLabel(f'y--x_0_y_{y}', '', row=0, column=0+y)

# creating rows (x-axis)
for x in range(25):
    app.addLabel(f'x--x_{x}_y_0', '', row=1+x, column=0)


app.addLabel('connected_users', 'CONNECTED', row=4, column=35)
app.addLabel('chat', 'CHAT', row=4, column=15)

app.addVerticalSeparator(row=2, column=30, rowspan=21, colour="grey")

app.addListBox(name='chatbox',
               values=[f'Connected to {HOST}:{PORT}'],
               row=6,
               column=1,
               rowspan=15,
               colspan=28)

app.addListBox(name='connected',
               values=users,
               row=6,
               column=32,
               rowspan=15,
               colspan=7)

app.addTextArea('message', row=22, column=3, colspan=24, rowspan=1)

app.addButtons(['Send', 'Clear chat', 'Disconnect'], click, column=3, row=23)


try:
    read_thread = Thread(target=receive, args=(client_socket,), daemon=True)
    read_thread.start()

except IOError as e:
    if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
        warning_box(f'Reading error: {str(e)}')
        sys.exit()

except Exception as e:
    warning_box(f'General error: {str(e)}')
    sys.exit()

app.enableEnter(enterPress)
app.go()




