import pyautogui
import time
from base.color import Color
from hub.action_gui import ActionGui
import base.keyboard_helper as keyboard_helper

class QuickPotion (ActionGui):
    def __init__(self, x, y, color):
        print('QuickPotion')
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
            self.doAction()

    def doAction(self):
        self.addMore()

    def addMore(self):
        if self.isAddingMore:
            return
        print('QuickPotion::addMore')
        self.isAddingMore = True
        self.lastMousePosition = pyautogui.position() 
        pos = self.vm.convertGameToScreen(self.inventoryPosition)
        pyautogui.moveTo(pos[0], pos[1], 0.1)
        time.sleep(0.1)
        keyboard_helper.keyDown('shift')
        keyboard_helper.keyDown(self.key)
        time.sleep(0.1)
        keyboard_helper.keyUp(self.key)
        keyboard_helper.keyUp('shift')
        time.sleep(0.1)
        pyautogui.moveTo(self.lastMousePosition[0], self.lastMousePosition[1], 0.2)
        keyboard_helper.pressKey('v', 0.1, 'close inventory')
        self.isAddingMore = False
