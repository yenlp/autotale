from hub.potion_bar import PotionBar
from base.color import Color

class HealthBar (PotionBar):
    def __init__(self, x, yLow, yHigh):
        print('HealthBar')
        super().__init__(x, yLow, yHigh)
        self.key = '2'

    def onFrameUpdate(self, deltaTime, screenshot):
        print('PotionBar::onFrameUpdate')
        color = screenshot.getpixel(self.triggerPosition)
        print('PotionBar::onFrameUpdate triggerPosition', self.triggerPosition)
        print('Color screenshot', color[0], color[1], color[2])
        print('Color', self.color.red(), self.color.green(), self.color.blue())
        if self.color.isEqual(Color(color[0], color[1], color[2]), 20):
            self.isActionRequired = False
        else:
            self.isActionRequired = True