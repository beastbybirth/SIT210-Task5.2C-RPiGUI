from tkinter import*
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

red = LED(5)
green = LED(6)
white = LED(13)

win = Tk()
win.title("LED Toggler")
myFont = tkinter.font.Font(family= "hello", size = 12, weight = "bold")

def toggle_leds(red, white, green): 		# function to make leds turned on and off
	if red == 1:				# if red button is on then following functions are performed
		red.on()			# red led pin = high
		redled["text"] = "RED LED ON"	# change GUI text
	else:					# if red button is off then following functions are performed
		red.off()			# red led pin = low
		redled["text"] = "RED LED OFF"	# change GUI text
		
	if white == 1:				# if white button is on then following functions are performed
		white.on()			# white led pin = high
		whiteled["text"] = "WHITE LED ON" # change GUI text
	else:					# if white button is off then following functions are performed
		white.off()			# white led pin = low
		whiteled["text"] = "WHITE LED OFF" # change GUI text
		
	if green == 1:				# if green button is on then following functions are performed
		green.on()			# green led pin = high
		greenled["text"] = "GREEN LED ON" # change GUI text
	else:					# if green button is off then following functions are performed
		green.off()			# green led pin = low
		greenled["text"] = "GREEN LED OFF" # change GUI text
		
def ledToggle():
    if red.is_lit:
	toggle_leds(0,0,0)
    else:
	toggle_leds(1,0,0)


def ledToggle1():
	if green.is_lit:
		toggle_leds(0,0,0)
	else:
		toggle_leds(0,0,1)


def ledToggle2():
	if white.is_lit:
		toggle_leds(0,0,0)
	else:
		toggle_leds(0,1,0)


def close():
    RPi.GPIO.cleanup()
    win.destroy()

redled = Button(win, font = myFont, command = ledToggle, text = 'RED LED OFF', bg = 'red', height = 2, width = 25)
redled.grid(row = 0, column = 0)
greenled = Button(win, font = myFont, command = ledToggle1, text = 'GREEN LED OFF', bg = 'green', height = 2, width = 25)
greenled.grid(row = 1, column = 0)
whiteled = Button(win, font = myFont, command = ledToggle2, text = 'WHITE LED OFF', bg = 'white', height = 2, width = 25)
whiteled.grid(row = 2, column = 0)
Exitbotton = Button(win, text = 'Exit', font = myFont, command = close, bg = 'orange', height = 1, width = 15)
Exitbotton.grid(row = 3, column = 0)

win.protocol("WM_DELETE_WINDOW")
win.mainloop()
