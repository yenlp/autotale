import math
import random
from base.color import Color
from hub.action_gui_key import ActionGuiKey

class PotionBar (ActionGuiKey):
    def __init__(self, x, yLow, yHigh):
        #print('PotionBar')
        super().__init__()
        self.x = x
        self.yLow = yLow
        self.yHigh = yHigh
        self.color = Color.BLACK()
        self.pottingCount = 0
        self.percent = 1.0
        self.setPercent(1.0)

    def setVM(self, vm):
        self.vm = vm
        
    def setColor(self, color):
        self.color = color

    def setPercent(self, percent):
        self.percent = percent
        self.calculate()

    def getCount(self):
        return self.pottingCount

    def calculate(self):
        self.triggerPosition = self.x, self.lerp(self.yLow, self.yHigh, self.percent)

    def lerp(self, a, b, t):
        return a * (1-t) + b * t

    def onFrameUpdate(self, deltaTime, screenshot):
        color = screenshot.getpixel(self.triggerPosition)
        if self.color.isEqual(Color(color[0], color[1], color[2]), 40):
            self.isActionRequired = False
        else:
            self.isActionRequired = True

    def onFrameRender(self, screenshot):
        if self.isActionRequired:
            self.potting(screenshot)

    def potting(self, screenshot):
        self.pottingCount = self.pottingCount + 1
        self.doAction(screenshot)