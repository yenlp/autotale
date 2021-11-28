import math
import random
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
        self.percent = 1.0
        self.setPercent(1.0)

    def setVM(self, vm):
        self.vm = vm
        
    def setColor(self, color):
        self.color = color

    def setPercent(self, percent):
        self.percent = percent
        self.calculate()

    def calculate(self):
        self.triggerPosition = self.x, self.lerp(self.yLow, self.yHigh, self.percent)

    def lerp(self, a, b, t):
        return a * (1-t) + b * t

    def onFrameUpdate(self, deltaTime, screenshot):
        color = screenshot.getpixel(self.triggerPosition)
        if self.color.isEqual(Color(color[0], color[1], color[2]), 30):
            self.isActionRequired = False
        else:
            self.isActionRequired = True

    def onFrameRender(self, screenshot):
        #print('PotionBar::onFrameRender')
        if self.isActionRequired:
            self.doAction()