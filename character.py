import pygame
import constants
import math
#Todo lo relacionado al jugador, o que realice el juagdor se hara dentro de la clase player
class Character():

    def __init__(self, x, y,animation_list):

        self.flip=False #Aqui
        self.animation_list = animation_list
        self.frame_index =0
        self.update_time=pygame.time.get_ticks()
        self.image=animation_list[self.frame_index]
        self.rect =pygame.Rect(0,0,40,40)
        self.rect.center=(x,y)

    ##metodos
    #Se declara surface pero se le esta pasando el argumento screen que se transforma en surface
    def draw(self,surface):
        flipped_image=pygame.transform.flip(self.image,self.flip,False) #Aqui
        surface.blit(flipped_image,self.rect)#Aqui
        pygame.draw.rect(surface,constants.RED,self.rect,1)

    def move(self, dx, dy):

        if dx<0: ##Aqui
            self.flip =True
        elif dx>0:
            self.flip=False
        #Control diagonal speed
        if dx != 0 and dy !=0:

            #Estamos normalizando el vector
            dx = dx * (math.sqrt(2)/2)
            dy = dy * (math.sqrt(2)/2)

        self.rect.x +=dx
        self.rect.y +=dy

    def update(self): ## Aqui
        animation_cooldown=70
        #update image
        self.image = self.animation_list[self.frame_index]
        #check if enough time has pass since the last update
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.frame_index +=1
            self.update_time = pygame.time.get_ticks()

        if self.frame_index>= len(self.animation_list):
            self.frame_index=0
        

