import pygame
import datetime
from dino_runner.components.clouds.obstacle_cloud_manager import ObstacleCloudManager
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.obstaclesbird.obstacle_bird_manager import ObstacleBirdManager
from dino_runner.components.powerups.powerup_manager import PowerupManager
from dino_runner.components.powerupsSte.powerupSte_manager import PowerSteManager
from dino_runner.components.winds.obstacles_wind_manager import ObstacleWindManager
from dino_runner.utils.constants import BG2, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS

from dino_runner.components.dinosaur import Dinosaur

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 0 #Cambie el tamaño a 0 para que se ajustara al tamaño de mi imagen.
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.powerup_manager = PowerupManager()
        self.obstacle_bird_manager = ObstacleBirdManager()
        self.obstacle_cloud_manager = ObstacleCloudManager()
        self.obstacle_wind_manager = ObstacleWindManager()
        self.powerSte_manager = PowerSteManager()
        self.score = 0
        self.start_time = datetime.datetime.now() #Tiempo inical.
        
    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
        pygame.quit() # Fin del evento o el while.

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        self.player.update(pygame.key.get_pressed())
        self.obstacle_manager.update(self)# Se encarga de mostrar o actualizar el obstaculo.
        self.powerup_manager.update(self)
        self.obstacle_bird_manager.update(self)
        self.obstacle_cloud_manager.update(self)
        self.obstacle_wind_manager.update(self)
        self.increase_score()

    def increase_score(self):
        self.score += 1

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255)) #Se encarga de el color de la pantalla y recetearla.
        self.draw_background()
        font = pygame.font.SysFont(None, 40)
        score_text = font.render(f"Score: {self.score}", True, (0, 0, 0))
        self.screen.blit(score_text, (10, 10))  # Ajusta la posición del texto como desees
        # Calcula el tiempo transcurrido
        current_time = datetime.datetime.now()
        elapsed_time = current_time - self.start_time
        elapsed_time_seconds = elapsed_time.total_seconds()
        time_text = font.render(f"Time: {int(elapsed_time_seconds)} seconds", True, (0, 0, 0))
        self.screen.blit(time_text, (10, 50))
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.powerup_manager.draw(self.screen)
        self.obstacle_bird_manager.draw(self.screen)
        self.obstacle_cloud_manager.draw(self.screen)
        self.obstacle_wind_manager.draw(self.screen)
        pygame.display.update() # Se encarga de dibujar en la pantalla. 
        pygame.display.flip() # Cambiar de pagina.

    def draw_background(self): 
        image_width = BG2.get_width()
        self.screen.blit(BG2, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG2, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG2, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed
