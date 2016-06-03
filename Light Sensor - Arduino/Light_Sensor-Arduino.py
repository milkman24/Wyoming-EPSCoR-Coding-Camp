# Light Sensor - Arduino
# Author: Matt Cook
# Created May 25, 2016
# Written for Wyoming EPSCoR Summer Coding Camp
# Version 0.2

# Updated sleep for synchronization times.  Bluetooth may need longer. Added
# util package import to correct errors with locating package. Fixed bug with
# Try block.

# Switched to using PyMata-aio instead of pyFirmata.  PyMata does many things pyFirmata doesn't, like auto-detect
# which port to use.

# TO DO: Test for what moisture levels are acceptable.  Use these in setting
# acceptable ranges in later part of code.

# Import necessary library/ies
from time import sleep
from pymata_aio.pymata3 import PyMata3
from pymata_aio.constants import Constants

# Setup the way we will communicate with the Arduino using PyMata.
board = PyMata3()

# Need to give some time to pyFirmata and Arduino to synchronize
sleep(5)



# This block allows us to quit the program if we want
# by just pressing some keys on the keyboard
while True:
    try:
        lightLevel = board.analog_read(0)
        # Print the values so the user can view them
        print("Light Level: " + lightLevel)

        # Optional: Set up ranges of light levels.  Make it print messages for
        # each range. Hint: if we do this we need a way to 
        low = 1
        medium = 2
        high = 3
        if('between this and that'):
            print("words")
        elif('between that and that'):
            print("more words")
        elif("greater than that"):
            print("even more words")

# If someone enters something, quit the program
    except KeyboardInterrupt() :
        board.exit()

