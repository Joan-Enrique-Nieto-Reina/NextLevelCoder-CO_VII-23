import pygame
import random

from dino_runner.components.powerupsSte.steppes import Hamer

class PowerSteManager():
    def __init__(self):
        self.has_steppes = False
        self.steppes = None
        self.next_steppes_show = 300
        
    def update(self, game):
        if not self.has_steppes and game.score == self.next_steppes_show:
            self.create_powerSte()
            self.next_steppes_show += random.randint(100, 500)
        if self.has_steppes:
            self.has_steppes = self.steppes.update(game.game_speed)
            if game.player.rect.colliderect(self.steppes.rect):
                self.has_steppes = False
                game.player.type = self.steppes.type

    def create_powerSte(self):
        self.steppes = Hamer()
        self.has_steppes = True

    def draw(self, screen):
        if self.has_steppes:
            self.steppes.draw(screen) 
    