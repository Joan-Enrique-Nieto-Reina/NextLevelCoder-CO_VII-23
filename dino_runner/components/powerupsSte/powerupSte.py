from dino_runner.utils.constants import (
    SCREEN_WIDTH,
    DEFAULT_TYPE
)

from pygame.sprite import Sprite

class PowerSte(Sprite):
    def __init__(self, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH - 80 
        self.rect.y = 300
        self.type = DEFAULT_TYPE

    def update(self, game_speed):
        self.rect.x -= game_speed
        return self.rect.x < 1100 and self.rect.x >= 0 #Tre if image is still on the screen, false otherwise

    def draw(self, screen):
        screen.blit(self.image, self.rect)
