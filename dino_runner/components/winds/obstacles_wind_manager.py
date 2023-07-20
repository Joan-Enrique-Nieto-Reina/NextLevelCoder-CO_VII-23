import pygame

from dino_runner.components.winds.wind import Wind

class ObstacleWindManager():
    def __init__(self):
        self.has_wind = False
        self.wind = None
        wind = pygame.sprite.Group()

    def update(self, game):
        if not self.has_wind:
            self.create_wind()
        self.has_wind = self.wind.update(game.game_speed)
        
    def create_wind(self):
        self.wind = Wind()
        self.has_wind = True

    def draw(self, screen):
        if self.has_wind:
            self.wind.draw(screen) 