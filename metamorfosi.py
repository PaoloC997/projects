from pyfirmata import ArduinoMega, util
import pyfirmata, pyfirmata.util
import time
import pygame

from random import seed
from random import randint
from random import seed
from random import choice

# Initialize PyGame and PyFirmata


pygame.mixer.init()
board = ArduinoMega('COM7', baudrate=57600)
iterator = pyfirmata.util.Iterator(board)
iterator.start()
time.sleep(1)

# Button Pin Declarations

button2 = board.get_pin('d:2:i')
button4 = board.get_pin('d:4:i')
button6 = board.get_pin('d:6:i')
button8 = board.get_pin('d:8:i')
button10 = board.get_pin('d:10:i')
button12 = board.get_pin('d:12:i')

button30 = board.get_pin('d:30:i')
button32 = board.get_pin('d:32:i')
button34 = board.get_pin('d:34:i')
button36 = board.get_pin('d:36:i')
button38 = board.get_pin('d:38:i')
button40 = board.get_pin('d:40:i')
button42 = board.get_pin('d:42:i')
button44 = board.get_pin('d:44:i')
button46 = board.get_pin('d:46:i')
button48 = board.get_pin('d:48:i')

#"Random" button pin declaration

botonrandom = board.get_pin('d:50:i')

#Led Pin Declarations

led_pin3 = 3                        
led_pin5 = 5
led_pin7 = 7
led_pin9 = 9
led_pin11 = 11
led_pin13 = 13
led_pin31 = 31
led_pin33 = 33
led_pin35 = 35
led_pin37 = 37
led_pin39 = 39
led_pin41 = 41
led_pin43 = 43
led_pin45 = 45
led_pin47 = 47
led_pin49 = 49
led_pin51 = 51


# Set the random button pin to report values

time.sleep(1)
botonrandom.enable_reporting()
time.sleep(1)
botonrandom.read()


# Function to blink randomly all 17 leds while playing a randomly chosen audio file
	
def activarrandom():
    leds = [3,5,7,9,11,13,31,33,35,37,39,41,43,45,47,49,51]

    value = randint(0,16)
    print('value',value)
    selection = value
    print(selection)
    cadena = str(selection) + "_u.aiff" 
    pygame.mixer.music.load(cadena)
    pygame.mixer.music.play()
       
    while pygame.mixer.music.get_busy() == True:

           
            i = choice(leds)
            board.digital[i].write(1)
           
            time.sleep(0.05)
           
            board.digital[i].write(0)
            time.sleep(0.05)
    
randomtrigger = False

# Function to play an audio file and turn on a led by pressing a button. 
# It will allow users to press the button only when the audio has stopped playing

def activaboton(numeroboton,numeroled,audio):
    estadoboton = str(numeroboton.read())
    if estadoboton == 'True':
       board.digital[numeroled].write(1)
       pygame.mixer.music.load(audio)
       pygame.mixer.music.play()
       while pygame.mixer.music.play:
           estadoboton == False
    if pygame.mixer.music.get_busy() == False:
       board.digital[numeroled].write(0)
    

# Main    

while True:

    randomtrigger = str(botonrandom.read())
    if randomtrigger == 'True':
        activarrandom()
        randomtrigger == False
    activaboton(button2,led_pin3,"3.aiff")
    activaboton(button4,led_pin5,"5.aiff")
    activaboton(button6,led_pin7,"7.aiff")
    activaboton(button8,led_pin9,"9.aiff")
    activaboton(button10,led_pin11,"11.aiff")
    activaboton(button12,led_pin13,"13.aiff")
    activaboton(button30,led_pin31,"31.aiff")
    activaboton(button32,led_pin33,"33.aiff")
    activaboton(button34,led_pin35,"35.aiff")
    activaboton(button36,led_pin37,"37.aiff")
    activaboton(button38,led_pin39,"39.aiff")
    activaboton(button40,led_pin41,"41.aiff")
    activaboton(button42,led_pin43,"43.aiff")
    activaboton(button45,led_pin45,"45.aiff")
    activaboton(button47,led_pin47,"47.aiff")
    activaboton(button49,led_pin49,"49.aiff")

    
    


board.exit()
   
 

   


