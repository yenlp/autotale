import pyautogui
import time
from base.color import Color
from hub.action_gui import ActionGui
from hub.inventory import Inventory
import base.keyboard_helper as keyboard_helper

class QuickPotion (ActionGui):
    def __init__(self, x, y, color):
        #print('QuickPotion')
        super().__init__()
        self.position = x, y
        self.color = color
        self.key = 'none'
        self.inventoryPosition  = 0, 0
        self.isAddingMore = False
        self.isAddingCompleted = False
        self.lastMousePosition = 0, 0

    def setKey(self, key):
        self.key = key

    def setInventoryPosition(self, position):
        self.inventoryPosition = position

    def onFrameUpdate(self, deltaTime, screenshot):
        pass

    def onFrameRender(self, screenshot):
        #print('PotionBar::onFrameRender')
        if self.isActionRequired:
            self.doAction(screenshot)

    def doAction(self, screenshot):
        self.addMore(screenshot)

    def addMore(self, screenshot):
        if self.isAddingMore:
            return
        print('QuickPotion::addMore')
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
        keyboard_helper.pressKey('v', 0.1, 'Close Inventory')
