from hub.potion_bar import PotionBar

class HealthBar(PotionBar):
    def __init__(self, x, yLow, yHigh):
        print('HealthBar')
        super().__init__(x, yLow, yHigh)