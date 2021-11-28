import math
from base.color import Color
from hub.action_gui_key import ActionGuiKey

class PotionBar (ActionGuiKey):
    def __init__(self, x, yLow, yHigh):
        print('PotionBar')
        super().__init__()
        self.x = x
        self.yLow = yLow
        self.yHigh = yHigh
        self.color = Color.BLACK()
        self.key = 'none'
        self.setPercent(1.0)

    def setColor(self, color):
        self.color = color

    def setActionKey(self, key):
        self.key = key

    def setPercent(self, percent):
        self.setPercent = percent
        self.calculate()

    def calculate(self):
        self.triggerPosition = self.x, self.lerp(self.yLow, self.yHigh, self.setPercent)

    def lerp(self, a, b, t):
        return a * (1-t) + b * t

    def onFrameUpdate(self, deltaTime, screenshot):
        print('PotionBar::onFrameUpdate')