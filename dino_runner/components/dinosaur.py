# Clase Nº 1.
# Crear la clase dinosaur. 
# add_ init_ .
# addd loop metodos (update, draw) pass.
import pygame

from pygame.sprite import Sprite
from dino_runner.utils.constants import (
    RUNNING1,
    DUCKING1,
    JUMPING1 
)

class Dinosaur(Sprite):

    POS_x = 80
    POS_Y = 300
    DUCK_POS_Y = 340
    JUMP_VEL = 8.5

    def __init__(self):
        self.image = RUNNING1 [0]
        self.rect = self.image.get_rect()
        self.rect.x = self.POS_x
        self.rect.y = self.POS_Y
        self.step_index = 0
        self.running = True
        self.ducking = False
        self.jumping = False    
        self.jumping_velocity = self.JUMP_VEL

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
        self.image = RUNNING1[0] if self.step_index < 5 else RUNNING1[1] #Cambio de imagne 1 a 2.
        self.rect = self.image.get_rect()
        self.rect.x = self.POS_x
        self.rect.y = self.POS_Y
        self.step_index += 1    

    def jump(self):
        self.image = JUMPING1
        if self.jumping:
            self.rect.y -= self.jumping_velocity * 4
            self.jumping_velocity -= 0.8 # Baja la velocidad del dino.
        if self.jumping_velocity < -self.JUMP_VEL:
            self.rect.y = self.POS_Y
            self.jumping = False
            self.jumping_velocity = self.JUMP_VEL

    def duck(self):
        self.image = DUCKING1[0] if self.step_index < 5 else DUCKING1[1] #Cambio de imagne 1 a 2.
        self.rect = self.image.get_rect()
        self.rect.x = self.POS_x
        self.rect.y = self.DUCK_POS_Y
        self.step_index = 1    