
from dino_runner.components.powerupsSte.powerupSte import PowerSte
from dino_runner.utils.constants import HAMMER, HAMMER_TYPE

class Hamer(PowerSte):
    def __init__(self):
        selec_image = HAMMER
        super().__init__(selec_image)
        self.type = HAMMER_TYPE
        