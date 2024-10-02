import pygame
import constants
import math
#Todo lo relacionado al jugador, o que realice el juagdor se hara dentro de la clase player
class Character():

    def __init__(self, x, y):

        self.rect =pygame.Rect(0,0,40,40)
        self.rect.center=(x,y)

    ##metodos
    #Se declara surface pero se le esta pasando el argumento screen que se transforma en surface
    def draw(self,surface):

        pygame.draw.rect(surface,constants.RED,self.rect)

    def move(self, dx, dy):

        #Control diagonal speed
        if dx != 0 and dy !=0:

            #Estamos normalizando el vector
            dx = dx * (math.sqrt(2)/2)
            dy = dy * (math.sqrt(2)/2)

        self.rect.x +=dx
        self.rect.y +=dy


        

