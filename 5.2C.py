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

def ledToggle():
    if red.is_lit:
        red.off()
        redled["text"]= "RED LED OFF"
    else:
        red.on()
        white.off()
        whiteled["text"] = "WHITE LED OFF"        
        green.off()
        greenled["text"] = "GREEN LED OFF"
        redled["text"] = "RED LED ON"

def ledToggle1():
	if green.is_lit:
		green.off()
		greenled["text"] = "GREEN LED OFF"
	else:
		green.on()
		white.off()
		whiteled["text"] = "WHITE LED OFF"
		red.off()
		redled["text"]= "RED LED OFF"
		greenled["text"] = "GREEN LED ON"

def ledToggle2():
	if white.is_lit:
		white.off()
		whiteled["text"] = "WHITE LED OFF"
	else:
		white.on()
		green.off()
		greenled["text"] = "GREEN LED OFF"
		red.off()
		redled["text"]= "RED LED OFF"
		whiteled["text"] = "WHITE LED ON"

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