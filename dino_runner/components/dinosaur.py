# Clase Nº 1.
# Crear la clase dinosaur. 
# add_ init_ .
# addd loop metodos (update, draw) pass.
import pygame

from pygame.sprite import Sprite
from dino_runner.utils.constants import (
    RUNNING1,
    DUCKING1,
    JUMPING1,
    DEFAULT_TYPE,
    SHIELD_TYPE,
    HAMMER_TYPE,
    DUCKING_SHIELD,
    RUNNING_SHIELD,
    JUMPING_SHIELD,
    DUCKING_HAMMER,
    JUMPING_HAMMER,
    RUNNING_HAMMER
)

class Dinosaur(Sprite):

    POS_x = 80
    POS_Y = 300
    DUCK_POS_Y = 340
    JUMP_VEL = 8.5

    def __init__(self):
        self.running_img = {DEFAULT_TYPE: RUNNING1, SHIELD_TYPE:RUNNING_SHIELD, HAMMER_TYPE:RUNNING_HAMMER} 
        self.jumping_img = {DEFAULT_TYPE: JUMPING1, SHIELD_TYPE:JUMPING_SHIELD,  HAMMER_TYPE:JUMPING_HAMMER} 
        self.ducking_img = {DEFAULT_TYPE: DUCKING1, SHIELD_TYPE:DUCKING_SHIELD, HAMMER_TYPE:DUCKING_HAMMER}  
        self.type = DEFAULT_TYPE

        self.image = self.running_img[self.type][0]
        self.rect = self.image.get_rect()
        self.rect.x = self.POS_x
        self.rect.y = self.POS_Y
        self.step_index = 0
        self.running = True
        self.ducking = False
        self.jumping = False    
        self.jumping_velocity = self.JUMP_VEL
        self.setup_states()
 
    def setup_states(self):
        self.has_powerup = False
        self.has_shield = False
        self.has_hammer = False
        

    def update(self, user_input):
        if self.jumping:
            self.jump()
        if self.running:
            self.run()
        if self.ducking:
            self.duck()

        if user_input[pygame.K_DOWN] or user_input[pygame.K_s] and not self.jumping:
            self.running = False
            self.ducking = True
            self.jumping = False

        elif user_input[pygame.K_UP] or user_input[pygame.K_SPACE] or user_input[pygame.K_w] and not self.ducking:
            self.running = False
            self.ducking = False
            self.jumping = True

        elif not self.jumping:
            self.running = True
            self.ducking = False
            self.jumping = False

        if self.step_index >= 10: 
            self.step_index = 0

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def run(self):
        self.image = self.running_img[self.type][self.step_index // 5] #Cambio de imagne 1 a 2.
        self.rect = self.image.get_rect()
        self.rect.x = self.POS_x
        self.rect.y = self.POS_Y
        self.step_index += 1    

    def jump(self):
        self.image = self.jumping_img[self.type]
        if self.jumping:
            self.rect.y -= self.jumping_velocity * 4
            self.jumping_velocity -= 0.8 # Baja la velocidad del dino.
        if self.jumping_velocity < -self.JUMP_VEL:
            self.rect.y = self.POS_Y
            self.jumping = False
            self.jumping_velocity = self.JUMP_VEL

    def duck(self):
        self.image = self.ducking_img[self.type][self.step_index // 5] #Cambio de imagne 1 a 2.
        self.rect = self.image.get_rect()
        self.rect.x = self.POS_x
        self.rect.y = self.DUCK_POS_Y
        self.step_index = 1    