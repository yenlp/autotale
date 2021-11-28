from hub.potion_bar import PotionBar
from base.color import Color

class HealthBar (PotionBar):
    def __init__(self, x, yLow, yHigh):
        print('HealthBar')
        super().__init__(x, yLow, yHigh)
        self.key = '2'