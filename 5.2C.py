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

def toggle_leds(red, white, green):
	if red == 1: 
		red.on()
		redled["text"] = "RED LED ON"
	else:
		red.off()
		redled["text"] = "RED LED OFF"
		
	if white == 1:
		white.on()
		whiteled["text"] = "WHITE LED ON"
	else:
		white.off()
		whiteled["text"] = "WHITE LED OFF"
		
	if green == 1:
		green.on()
		greenled["text"] = "GREEN LED ON"
	else:
		green.off()
		greenled["text"] = "GREEN LED OFF"
		
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
