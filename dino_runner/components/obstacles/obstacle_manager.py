
from dino_runner.components.obstacles.cactus import Cactus

class ObstacleManager():
    def __init__(self):
        self.has_obstacle = False
        self.obstacle = None

    def update(self, game):
        if not self.has_obstacle:
            self.create_obstacle()
        self.has_obstacle = self.obstacle.update(game.game_speed) 

    def create_obstacle(self):
        self.obstacle = Cactus()
        self.has_obstacle = True

    def draw(self, screen):
        if self.has_obstacle:
            self.obstacle.draw(screen) 
    # voy en el 1: 20 del video de la clase de ayer.
    