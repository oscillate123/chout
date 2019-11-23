from appJar import gui

app = gui()

IP = '127.0.0.1'
PORT = 6663
SERVER_INFO = 'You successfully connected to: ' + IP + ':' + str(PORT)

connections = ['racso', 'mercur', 'hyperX', '127.0.0.1', 'oSCar', 'willepille']


def update_inputs(text):
    app.addListItem(title='chatbox', item=text, select=False)


def click(buttontype):
    if buttontype == "Send":
        update_inputs(app.getTextArea('message'))
        app.clearTextArea(title='message', callFunction=False)
    elif buttontype == "Clear":
        app.clearListBox(title='chatbox', callFunction=False)
    else:
        pass

# BODY SETTINGS
# app.setSize(x, y)
app.setSize(600, 600)
app.setFont(14)
app.setBg('LightGrey')
app.setTransparency(99)


# creating 40 columns (y)
for y in range(40):
    app.addLabel(f'y--x_0_y_{y}', '', row=0, column=0+y)

# creating 15 rows (x)
for x in range(25):
    app.addLabel(f'x--x_{x}_y_0', '', row=1+x, column=0)


app.addLabel('connected_users', 'CONNECTED', row=4, column=35)
app.addLabel('chat', 'CHAT', row=4, column=15)

app.addVerticalSeparator(row=2, column=30, rowspan=21, colour="grey")

app.addListBox(name='chatbox',
               values=[SERVER_INFO],
               row=6,
               column=1,
               rowspan=15,
               colspan=28)

app.addListBox(name='connected',
               values=connections,
               row=6,
               column=32,
               rowspan=15,
               colspan=7)

app.addTextArea('message', row=22, column=3, colspan=24, rowspan=1)

app.addButtons(['Send', 'Clear'], click)

app.go()




