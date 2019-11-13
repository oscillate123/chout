import random
from appJar import gui

app = gui()

busy_nums = []

IP = '127.0.0.1'
PORT = 6663
SERVER_INFO = 'You successfully connected to: ' + IP + ':' + str(PORT)

connections = ['racso', 'mercur', 'hyperX', '127.0.0.1']


# RANDOM VARIABLES
def random_name():
    ran = random.randint(1, 1000)
    if ran not in busy_nums:
        busy_nums.append(ran)
        return ran
    else:
        random_name()


# POSITION GROUPS

x_0 = 0
x_1 = 1
x_2 = 2
x_3 = 3
x_4 = 4
x_5 = 5
x_6 = 6
x_7 = 7
x_8 = 8

y_0 = 0
y_1 = 1
y_2 = 2
y_3 = 3
y_4 = 4
y_5 = 5
y_6 = 6
y_7 = 7
y_8 = 8
y_9 = 9
y_10 = 10

# BODY SETTINGS
# app.setSize(y, x)
app.setSize(700, 500)
app.setFont(14)
app.setBg('LightGrey')
app.setTransparency(97)

# BODY CONTENT ROW 0 #X_0
app.addLabel(f'{random_name()}', 'col 0', row=x_0, column=y_0)
app.addLabel(f'{random_name()}', 'column 1', row=x_0, column=y_1)
app.addLabel(f'{random_name()}', 'column 2', row=x_0, column=y_2)
app.addLabel(f'{random_name()}', 'column 3', row=x_0, column=y_3)
app.addLabel(f'{random_name()}', 'column 4', row=x_0, column=y_4)
app.addLabel(f'{random_name()}', 'column 5', row=x_0, column=y_5)
app.addLabel(f'{random_name()}', 'column 6', row=x_0, column=y_6)
app.addVerticalSeparator(row=x_1, column=y_6, rowspan=7, colour="grey")
app.addLabel(f'{random_name()}', 'column 7', row=x_0, column=y_7)
app.addLabel(f'{random_name()}', 'column 7', row=x_0, column=y_8)

# BODY CONTENT ROW 1 #X_1
app.addLabel(f'{random_name()}', 'X1', row=x_1, column=y_0)
app.addLabel(f'{random_name()}', 'Connected:', row=x_1, column=y_7)

# BODY CONTENT ROW 2 #X_2
app.addListBox(name='chatbox',
               values=[SERVER_INFO],
               row=x_2,
               column=y_1,
               colspan=5,
               rowspan=4)

app.addListBox(name='connected',
               values=connections,
               row=x_2,
               column=y_7,
               rowspan=5)

# BODY CONTENT BELOW ROW 1
app.addLabel(f'{random_name()}', 'X6', row=x_6, column=y_0)
app.addLabel(f'{random_name()}', 'X7', row=x_7, column=y_0)
app.addLabel(f'{random_name()}', 'X8', row=x_8, column=y_0)

app.addListItem(title='chatbox', item='Test', select=False)

app.go()


if __name__ == "__main__":
    print()
