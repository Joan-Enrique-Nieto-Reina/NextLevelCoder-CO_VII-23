
import random

from dino_runner.components.obstaclesbird.obstacle_bird import ObstacleBird
from dino_runner.utils.constants import (
    BIRD
)

class Bird(ObstacleBird):
    def __init__(self):
        image_list = BIRD
        select_image = random.choice(image_list)
        super().__init__(select_image)
        
        
