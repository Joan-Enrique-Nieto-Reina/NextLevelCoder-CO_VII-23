from typing import Any
import pygame

from dino_runner.utils.constants import (
    SCREEN_WIDTH
)
from pygame.sprite import _Group, Sprite

class Obstacle(Sprite):
    def __init__(self, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH
        
    def update(self, game_speed):
        self.rect.x -= game_speed 
    
    def draw(self, screen):
        screen.blit(self.image, self.rect )
        