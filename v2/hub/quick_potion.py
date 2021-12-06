import pyautogui
import time
from base.color import Color
from hub.action_gui import ActionGui
from hub.inventory import Inventory
import base.keyboard_helper as keyboard_helper

class QuickPotion (ActionGui):
    STATUS_LOW = 0
    STATUS_SAFE = 1
    STATUS_HIGH = 2

    def __init__(self, x, y, color):
        #print('QuickPotion')
        super().__init__()
        self.name = ''
        self.position = x, y
        self.color = color
        self.key = 'none'
        self.inventoryPosition  = 0, 0
        self.isAddingMore = False
        self.isAddingCompleted = False
        self.lastMousePosition = 0, 0
        self.counterPositions = []
        self.status = QuickPotion.STATUS_SAFE
        self.balancingFrequency = 0
        self.balancingTime = 0

    def setKey(self, key):
        self.key = key

    def setInventoryPosition(self, position):
        self.inventoryPosition = position

    def addCounterPositions(self, start, end):
        pos = (start, end)
        self.counterPositions.append(pos)

    def onFrameUpdate(self, deltaTime, screenshot):
        if self.counterPositions == None or len(self.counterPositions) == 0:
            return
        if self.balancingFrequency <= 0:
            return
        self.balancingTime += deltaTime
        if self.balancingTime < self.balancingFrequency:
            self.status = QuickPotion.STATUS_SAFE
            return
        self.balancingTime -= self.balancingFrequency
        xmin = 99999
        xmax = 0
        pos = 0,0
        c = 240
        for t in self.counterPositions:
            if xmin > t[0][0]:
                xmin = t[0][0]
            if xmax < t[1][0]:
                xmax = t[1][0]
            y = (t[0][1] + t[1][1]) / 2
            for x in range(t[1][0], t[0][0] - 1, -1):
                color = screenshot.getpixel((x,y))
                if color[0] > c and color[1] > c and color[2] > c:
                    if pos[0] < x:
                        pos = (x,y)
                    break
        percent = (pos[0] - xmin) / (xmax - xmin)
        if percent > 0.65:
            self.status = QuickPotion.STATUS_HIGH
        elif percent > 0.3:
            self.status = QuickPotion.STATUS_HIGH
        else:
            self.status = QuickPotion.STATUS_LOW

    def onFrameRender(self, screenshot):
        #print('PotionBar::onFrameRender')
        if self.isActionRequired:
            self.doAction(screenshot)

    def doAction(self, screenshot):
        self.addMore(screenshot)

    def addMore(self, screenshot):
        if self.isAddingMore:
            return
        print('Add More', self.name)
        self.isAddingMore = True
        self.lastMousePosition = pyautogui.position() 
        pos = self.vm.convertGameToScreen(self.inventoryPosition)
        if self.isPotionInventoryEmpty(screenshot):
            self.teleport()
        else:
            t = 0.1
            pyautogui.moveTo(pos[0], pos[1], t)
            time.sleep(t + 0.1)
            keyboard_helper.keyDown('shift')
            keyboard_helper.keyDown(self.key)
            #time.sleep(0.1)
            keyboard_helper.keyUp(self.key)
            keyboard_helper.keyUp('shift')
            time.sleep(0.05)
            pyautogui.moveTo(self.lastMousePosition[0], self.lastMousePosition[1], 0.1)
            #keyboard_helper.pressKey('v', 0.1, 'Close inventory')
            self.isAddingCompleted = True

    def isCompleted(self):
        return self.isAddingCompleted

    def setBalancingCheckFrequency(self, t):
        self.balancingFrequency = t

    def isHighStatus(self):
        return self.status == QuickPotion.STATUS_HIGH

    def reset(self):
        self.isAddingMore = False
        self.isAddingCompleted = False

    def isPotionInventoryEmpty(self, screenshot):
        return False

    def teleport(self):
        pos_core = self.inventoryPosition[0], self.inventoryPosition[1] + 20
        pos = self.vm.convertGameToScreen(pos_core)
        t = 0.1
        pyautogui.moveTo(pos[0], pos[1], t)
        time.sleep(t + 0.1)
        pyautogui.mouseDown(button = pyautogui.RIGHT)
        pyautogui.mouseUp(button = pyautogui.RIGHT)
        self.vm.home()
        keyboard_helper.pressKey('space', 0.1, 'Close Inventory')
