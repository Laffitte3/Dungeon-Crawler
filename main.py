import pygame
import constants
from character import Character


pygame.init()

screen= pygame.display.set_mode((constants.SCREEN_WITDH,constants.SCREEN_HEIGHT))

#create a player
player=Character(40,50)

running=True
##main game loop
while running:

    #event handler
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

    pygame.display.update()


pygame.quit()