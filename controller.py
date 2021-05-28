import piconzero as pz
from guizero import App, Text, TextBox, PushButton, Slider
pz.init()
def f_forward(speed):
	pz.forward(speed)
	stats.value = "forward"
 
def f_back(speed):
	pz.reverse(speed)
    stats.value = "back"

def f_left(speed):
	pz.spinLeft(speed)
    stats.value = "f_left"

def f_right(speed):
	pz.spinRight(speed)
    stats.value = "f_right"

def f_angle(angle):
    pz.setOutputConfig (1, angle)
    stats.value = "f_angle"



def f_c_o():
    pz.setOutputConfig (0, angle)
    stats.value = "f_c_o"
def f_shoot():
    pz.setOutputConfig (0, angle)
    stats.value = "f_shoot"





true_speed = 0
true_angle = 0


app = App(title="Dragon bot", layout = "grid")
stats = Text(app, text="", grid = [4,1])
speed = Slider(app, start = 0, end = 100, grid= [4,3,5,3])
angle = Slider(app, command= f_angle, start = 0, end = 180, grid= [4,2,5,2]) 
forward = PushButton(app, args= [speed.value], command= f_forward, text="F", grid= [1,2])
back = PushButton(app, args= [speed.value], command= f_back, text="B", grid= [1,4])
left = PushButton(app, args= [speed.value], command= f_left, text="L", grid= [0,3])
right = PushButton(app, args= [speed.value], command= f_right, text="R", grid= [2,3])
c_o = PushButton(app, command= f_c_o, text="close/open", grid= [3,1])
shoot = PushButton(app, command= f_shoot, text="close/open", grid= [4,1])
pz.cleanup()
app.display()
