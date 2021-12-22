from hub.potion_bar import PotionBar

class StaminaBar (PotionBar):
    def __init__(self, x, yLow, yHigh):
        #print('StaminaBar')
        super().__init__(x, yLow, yHigh)
        self.key = '1'
        self.name = 'Stamina'