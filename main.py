import pygame
import constants
from character import Character


pygame.init()

screen= pygame.display.set_mode((constants.SCREEN_WITDH,constants.SCREEN_HEIGHT))

clock=pygame.time.Clock()
#Define player movements variables
#Estas son variables que no controlan el movimiento sino que avtivan en movimiento
#los utilizaremos para avriar dx y dy

#Estas variables seran conectadas a las entradas por teclado
moving_left=False
moving_right=False
moving_up=False
moving_down=False

#create a player
player=Character(40,50)

running=True
##main game loop
while running:
    screen.fill(constants.BG)
    #calculate player movement
    #change in x and y
    dx=0
    dy=0
    if moving_right==True:
        dx= constants.SPEED
    if moving_left == True:
        dx=-constants.SPEED
    if moving_up==True:
        dy= -constants.SPEED
    if moving_down==True:
        dy= constants.SPEED
    
    #move player
    player.move(dx,dy)


    #draw player
    #le pasamos como argumento screen para que esta variable la pueda utilizar el metodo en el otro archivo .py
    player.draw(screen)

    #event handler
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

        #take keybord presses
        if event.type == pygame.KEYDOWN:
            if event.key== pygame.K_a:
                moving_left=True
            if event.key== pygame.K_d:
                moving_right=True
            if event.key== pygame.K_w:
                moving_up=True
            if event.key== pygame.K_s:
                moving_down=True
        
        #keybord button released
        if event.type == pygame.KEYUP:
            if event.key== pygame.K_a:
                moving_left=False
            if event.key== pygame.K_d:
                moving_right=False
            if event.key== pygame.K_w:
                moving_up=False
            if event.key== pygame.K_s:
                moving_down=False

    
    pygame.display.update()
    clock.tick(constants.FPS)

pygame.quit()