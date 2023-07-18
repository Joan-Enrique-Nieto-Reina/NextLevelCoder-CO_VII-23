
from dino_runner.components.obstacles.cactus import Cactus

class ObstacleManager():
    def __init__(self):
        self.has_obstacle = False
        self.obstacle = None

    def update(self, game):
        if not self.has_obstacle:
            self.create_obstacle()
        self.obstacle.update(game.game_speed)

    def create_obstacle(self):
        self.obstacle = Cactus()

    def draw(self, screen):
        if self.obstacle