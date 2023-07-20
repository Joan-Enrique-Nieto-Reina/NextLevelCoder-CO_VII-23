import random
from dino_runner.components.clouds.obstacle_cloud import ObstacleCloud

from dino_runner.utils.constants import (
    CLOUD1,
    CLOUD2
)

class Cloud(ObstacleCloud):
    def __init__(self):
        image_list = CLOUD1 + CLOUD2
        select_image = random.choice(image_list)
        super().__init__(select_image)
        self.rect.y = 90     
        