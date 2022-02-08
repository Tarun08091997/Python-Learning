import sys

import pygame
from sprites import *
pygame.init() # it will initiate all the sub moduls of pygame like fonts, display etc it must be in the code

""" Define and create screen """
width = 1366 ## maximum width of screen in pixels
height = 768 # max height

screen = pygame.display.set_mode((width,height))  # create screen
pygame.display.set_caption("Basic_Learning")    # add title of the program
screen.fill('gray')

################## FPS
clock = pygame.time.Clock()


############# Static_moving object

smco = static_moving_collision()

######## Game loop###################
running = True
while running:

    clock.tick(60) # let program run at a FPS of 60 (constant Rate)

    ################# program ###################


    smco.check_collision()
    smco.update(screen)



    """ This function will check for 'event' occured like mouseButton key down / key pressed or released
        then check the 'type' of the event and use them for condions"""


    for event in pygame.event.get():  # check for all elements in list: pygame.event.get()
        if event.type == pygame.QUIT: # check if event is Quit event or cross on right side is pressed
            running = False         #  exit the while loop
            """ we can use 'pygame.quit()' -> it will quit from pygame but not from python/system so other python program
                                             with it will run. Problem is, if you try to run the program again without sys.exit
                                             ie. created GUI and start again without closing GUI it will show error.
                                             Because there is pb with pygame
                pygame.display.quit() -> it will quit out of diplay only, program will run in back. If you want to run 
                                         program again in pygame reset all the values and start it
                                         
                sys.exit() ->     TO exit the python program completely
            """

        if event.type == pygame.KEYDOWN:    # for keydown event, if any key is pressed
            if event.key == pygame.K_SPACE: # if key is preesed and it is SPACE key
                pass

            if event.key == pygame.K_ESCAPE:
                sys.exit()

        if event.type == pygame.KEYUP:      ## event of key released
            if event.key == pygame.K_SPACE:
                pass

        """ the pb is this key works only one time => if kept pressed it has no effect because it will take 
            event -> keydown or keyup then check the key , so they react only when key is pressed or released
            
            to overcome this we use pygame.key.get_pressed() which return a sequence with key as key_name stored as boolean
             if pressed -> True
             .else False"""

        key = pygame.key.get_pressed()
        if(key[pygame.K_SPACE]):  ## this function will remain activated until space is being pressed
            pass




    pass
