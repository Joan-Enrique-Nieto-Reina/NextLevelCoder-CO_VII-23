import pygame

from dino_runner.components.obstaclesbird.bird import Bird

class ObstacleBirdManager():
    def __init__(self):
        self.has_Bird = False
        self.bird = None
        bidr = pygame.sprite.Group()
        self.next_bird_show = 200

    def update(self, game):
        if not self.has_Bird and game.score == self.next_bird_show:
            self.create_bird()
        if self.has_Bird:
            self.has_Bird = self.bird.update(game.game_speed)
            if game.player.rect.colliderect(self.bird.rect):
                pygame.time.delay(500)
                game.playing = False  

    def create_bird(self):
        self.bird = Bird()
        self.has_Bird = True

    def draw(self, screen):
        if self.has_Bird:
            self.bird.draw(screen) 
    