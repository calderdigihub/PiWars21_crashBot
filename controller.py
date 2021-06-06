import piconzero as pz
import evdev
#from guizero import App, Text, TextBox, PushButton, Slider
pz.init()
def f_forward(speed):
	if speed > 50 and speed < 150:
		pz.forward(speed-50)
		print("forward at speed: "+str(speed-50))
	#stats.value = speed.value

def f_back(speed):
	if speed > 50 and speed < 150:
		pz.reverse(speed-50)
		print("Reverse at speed: "+str(speed-50))
    #stats.value = "back"

def f_left():
	pz.spinLeft(60)
	print("Spining left")
    #stats.value = "left"

def f_right():
	pz.spinRight(60)
	print("Spining right")
    #stats.value = "right"

def f_angle(angle):
    #pz.setOutputConfig (1, angle)
    #stats.value = "f_angle"
def setSpeed(Speed):
	#speedo.value = Speed


'''app = App(title="Dragon bot", layout = "grid")
stats = Text(app, text="", grid = [4,1])
speed = Slider(app,command = setSpeed, start = 0, end = 100, grid= [4,3,5,3])
speedo = Text(app, text="", grid = [6,3])
angle = Slider(app, command= f_angle, start = 0, end = 180, grid= [4,2,5,2]) 
forward = PushButton(app, args= [speedo.text], command= f_forward, text="F", grid= [1,2])
back = PushButton(app, args= [speedo], command= f_back, text="B", grid= [1,4])
left = PushButton(app, args= [speedo], command= f_left, text="L", grid= [0,3])
right = PushButton(app, args= [speedo], command= f_right, text="R", grid= [2,3])
app.display()'''

#sets the device we are reading input from as event 0 as no other input devices should be attached
controller = InputDevice('/dev/input/event0')


#starts the event loop
for event in controller.read_loop():
	#prints the event and value of it for keys 0 is up and 1 is down 
	print(str(event.code)+" "+str(event.value))
	
	#goes to the forward function if the right trigger is pressed 
	if event.code == 5:
		f_forward(event.value)
	#goes to the back function if the left trigger is pressed 
	if event.code == 2:
		f_back(event.value)
	#goes to the left tank function if the left d pad button is down
	if event.code == 16 and event.value == -1:
		f_left()
	#goes to the right tank function if the right d pad button is down
	if event.code == 16 and event.value == 1:
		f_right()
	#stops all commands is the centeral button is pressed
	if event.code == 316:
		pz.stop( ) 
