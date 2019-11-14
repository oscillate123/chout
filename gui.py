import random
from appJar import gui

app = gui()



IP = '127.0.0.1'
PORT = 6663
SERVER_INFO = 'You successfully connected to: ' + IP + ':' + str(PORT)

connections = ['  ## CONNECTIONS ##', 'racso', 'mercur', 'hyperX', '127.0.0.1']

busy_nums = []

# FUNCTIONS
def random_name():
    ran = random.randint(1, 1000)
    if ran not in busy_nums:
        busy_nums.append(ran)
        return ran
    else:
        random_name()


def update_inputs():
    app.addListItem(title='chatbox', item='Test', select=False)


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
# app.setSize(x, y)
app.setSize(600, 400)
app.setFont(14)
app.setBg('LightGrey')
app.setTransparency(97)


for y in range(15):
    app.addLabel(f'y--x_0_y_{y}', '[]', row=x_0, column=y_0+y)

for x in range(15):
    app.addLabel(f'x--x_{x}_y_0', '{}', row=x_1+x, column=y_0)





# app.addVerticalSeparator(row=x_0, column=y_5, rowspan=1, colour="grey")

# app.addListBox(name='chatbox',
#                values=[SERVER_INFO],
#                row=x_0,
#                column=y_1,)

# app.addListBox(name='connected',
#                values=connections,
#                row=x_0,
#                column=y_7,)


app.go()




