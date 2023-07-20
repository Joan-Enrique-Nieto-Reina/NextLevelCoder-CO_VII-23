
import pygame
from dino_runner.components.dinosaur import DEFAULT_TYPE, SHIELD_TYPE
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.powerups.shield import Shield

class ObstacleManager():
    def __init__(self):
        self.has_obstacle = False
        self.obstacle = None
        self.obstacles = pygame.sprite.Group()
        self.shield_active = False
        self.shield_duration = 3000  
        self.shield_timer = 0

    def update(self, game):
        if not self.has_obstacle:
            self.create_obstacle()

        if self.shield_active:
            self.shield_timer -= game.clock.get_rawtime()  
            if self.shield_timer <= 0:
                self.shield_active = False
                game.player.type = DEFAULT_TYPE

        self.has_obstacle = self.obstacle.update(game.game_speed)
        if game.player.rect.colliderect(self.obstacle.rect):
            if game.player.type == SHIELD_TYPE:
                game.player.type = DEFAULT_TYPE
                self.shield_active = True
                self.shield_timer = self.shield_duration
                self.has_obstacle = False
            else:
                pygame.time.delay(500)
                game.playing = False

    def create_obstacle(self):
        obstacle_type = "cactus" 
        if obstacle_type == "cactus":
            self.obstacle = Cactus()
        elif obstacle_type == "shield":
            self.obstacle = Shield()  

        self.has_obstacle = True

    def draw(self, screen):
        if self.has_obstacle:
            self.obstacle.draw(screen)

    
    