import pygame
from dino_runner.components.clouds.cloud import Cloud

class ObstacleCloudManager():
    def __init__(self):
        self.has_cloud = False
        self.cloud = None
        cloud = pygame.sprite.Group()


    def update(self, game):
        if not self.has_cloud:
            self.create_cloud()
        self.has_cloud = self.cloud.update(game.game_speed)
    
    def create_cloud(self):
        self.cloud = Cloud()
        self.has_cloud = True

    def draw(self, screen):
        if self.has_cloud:
            self.cloud.draw(screen) 