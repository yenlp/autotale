from hub.potion_bar import PotionBar

class ManaBar (PotionBar):
    def __init__(self, x, yLow, yHigh):
        #print('ManaBar')
        super().__init__(x, yLow, yHigh)
        self.key = '3'
        self.name = 'Mana'