
from dino_runner.components.powerups.powerup import PowerUP
from dino_runner.utils.constants import SHIELD, SHIELD_TYPE

class Shield(PowerUP):
    def __init__(self):
        selec_image = SHIELD
        super().__init__(selec_image)
        self.type = SHIELD_TYPE
        