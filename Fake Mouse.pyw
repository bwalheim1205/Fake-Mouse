#-----------------------------
# Fake Mouse
#   Creator: Brian Walheim
#   Version: 1.0
#
#   Moves mouse randomly around the screen
#-----------------------------

#-------------
#Imports
#-------------

#Pygame Imports
from pynput.mouse import Button, Controller
import pygame

#Misc
import time
import random
import sys

#------------
#Variables
#------------

#Mouse Variables
mouse = Controller()
active = False

#Starts Pygame
pygame.init()
pygame.display.set_mode((50,50))

#-----------
#Functions
#-----------

#Moves the mouse small random increments
def mouseMove():

    mouse.move(random.randint(-10,10),random.randint(-10,10))
    time.sleep(0.1)

#----------
#Main
#----------

#Infinite Loop
while True:

    if active:
       mouseMove()
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.display.quit()
                pygame.quit()
                sys.exit()
            elif event.key == pygame.K_BACKQUOTE:
                if not active:
                    active = True
                else:
                    active = False



