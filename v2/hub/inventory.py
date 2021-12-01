import time
import base.keyboard_helper as keyboard_helper

class Inventory:
    ANIMATION_TIME = 1
    def __init__(self) -> None:
        self.vm = None
        self.isOpened = False
        self.isInteractable = False
        self.time = Inventory.ANIMATION_TIME

    def setVM(self, vm):
        self.vm = vm

    def onFrameUpdate(self, deltaTime, screenshot):
        if self.time > 0:
            self.time = self.time - deltaTime
            if self.time <= 0:
                self.isOpened = self.checkInventory(screenshot)
                self.isInteractable = True
                time.sleep(0.2)
        elif self.isInteractable:
            self.isOpened = self.checkInventory(screenshot)
        else:
            self.isOpened = False

    def checkInventory(self, screenshot):
        x = 116
        for y in range(550, 630, 10):
            pix = screenshot.getpixel((x, y))
            if abs(pix[0] - pix[1]) > 2:
                return False
            if abs(pix[1] - pix[2]) > 2:
                return False
            if abs(pix[2] - pix[0]) > 2:
                return False
        return True

    def getInteractable(self):
        return self.isInteractable

    def isOpen(self):
        return self.isOpened

    def open(self):
        if not self.isInteractable:
            return
        if self.isOpened:            
            return
        self.isInteractable = False
        self.time = Inventory.ANIMATION_TIME
        keyboard_helper.pressKey('v', 0.1, 'Open Inventory ' + str(time.time()))

    def close(self):
        if not self.isInteractable:
            return
        if not self.isOpened:
            return
        self.isInteractable = False
        self.time = Inventory.ANIMATION_TIME
        keyboard_helper.pressKey('v', 0.1, 'Close Inventory '+ str(time.time()))