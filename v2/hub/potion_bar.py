import math
import random
from base.color import Color
from hub.action_gui_key import ActionGuiKey
import settings

class PotionBar (ActionGuiKey):
    def __init__(self, x, yLow, yHigh):
        #print('PotionBar')
        super().__init__()
        self.x = x
        self.yLow = yLow
        self.yHigh = yHigh
        self.color = Color.BLACK()
        self.pottingCount = 0
        self.antiShock = True
        self.trend = [9, 9, 9, 9, 9]
        self.autoAdjust = False
        self.minPercent = 0.2
        self.maxPercent = 0.2
        self.percent = 1.0
        self.setPercent(1.0)

    def setVM(self, vm):
        self.vm = vm
        
    def setColor(self, color):
        self.color = color

    def setPercent(self, percent):
        self.percent = percent
        self.calculate()

    def setAutoAdjust(self, minPercent, maxPercent):
        self.autoAdjust = True
        self.minPercent = minPercent

    def getCount(self):
        return self.pottingCount

    def calculate(self):
        self.triggerPosition = self.x, self.lerp(self.yLow, self.yHigh, self.percent)

    def lerp(self, a, b, t):
        return a * (1-t) + b * t

    def updateAntiShock(self, deltaTime, screenshot):
        percentHighest = 0
        for percent in range(1, 10):
            position = self.x, self.lerp(self.yLow, self.yHigh, percent / 10.0)
            color = screenshot.getpixel(position)
            if self.isColorMatched(Color(color[0], color[1], color[2])):
                percentHighest = percent
        self.trend.pop(0)
        self.trend.append(percentHighest)
        diff = 0
        for i in range(len(self.trend) - 1):
            n1 = self.trend[i]
            n2 = self.trend[i+1]
            d = n1 - n2
            if d > diff:
                diff = d
        percent = diff / 10.0
        percentX2 = percent * 2 + 0.05
        if percentX2 > self.percent:
            self.setPercent(percentX2)
            settings.percentHP = min(percentX2, 0.9)
            print('Shock Dame ', percent)
            print('Potion percent increase ', self.percent)

    def updateAutoAdjust(self, deltaTime, screenshot):
        position = self.x, self.lerp(self.yLow, self.yHigh, self.minPercent)
        color = screenshot.getpixel(position)
        if not self.isColorMatched(Color(color[0], color[1], color[2])):
            percent = (self.percent + 1.0) / 2
            self.setPercent(percent)
            settings.percentHP = percent
            print('Potion percent increase ', self.percent)
        else:
            position = self.x, self.lerp(self.yLow, self.yHigh, self.maxPercent)
            color = screenshot.getpixel(position)
            if self.isColorMatched(Color(color[0], color[1], color[2])):
                percent = max(self.percent - 0.01, self.minPercent)
                self.setPercent(percent)
                settings.percentHP = percent
                print('Potion percent decrease ', self.percent)

    def onFrameUpdate(self, deltaTime, screenshot):
        if self.antiShock and self.autoAdjust:
            self.updateAntiShock(deltaTime, screenshot)
        color = screenshot.getpixel(self.triggerPosition)
        if self.isColorMatched(Color(color[0], color[1], color[2])):
            self.isActionRequired = False
        else:
            self.isActionRequired = True
        if self.isActionRequired and self.autoAdjust:
            self.updateAutoAdjust(deltaTime, screenshot)

    def onFrameRender(self, screenshot):
        if self.isActionRequired:
            self.potting(screenshot)

    def potting(self, screenshot):
        self.pottingCount = self.pottingCount + 1
        self.doAction(screenshot)

    def isColorMatched(self, color):
        return self.color.isEqual(color, 40)