import random

from dino_runner.components.winds.obstacle_wind import ObstacleWind
from dino_runner.utils.constants import (
    WIND
)

class Wind(ObstacleWind):
    def __init__(self):
        image_list = WIND
        select_image = random.choice(image_list)
        super().__init__(select_image)
        self.rect.y = 30