import base.keyboard_helper as keyboard_helper

class Inventory:
    ANIMATION_TIME = 1
    def __init__(self) -> None:
        self.vm = None
        self.isOpened = False
        self.isInteractable = True
        self.time = 0

    def setVM(self, vm):
        self.vm = vm

    def onFrameUpdate(self, deltaTime, screenshot):
        if self.time > 0:
            self.time = self.time - deltaTime
            if self.time <= 0:
                self.isOpened = self.checkInventory(screenshot)
                self.isInteractable = True
        elif self.isInteractable:
            self.isOpened = self.checkInventory(screenshot)
        else:
            self.isOpened = False

    def checkInventory(self, screenshot):
        y = 590
        for x in range(420, 510, 20):
            pix = screenshot.getpixel((x, y))
            if pix[0] < 100 or pix[2] > 100:
                return False
        return True

    def isOpen(self):
        return self.isOpened

    def open(self):
        if not self.isInteractable:
            return
        if self.isOpened:
            return
        self.isInteractable = False
        self.time = Inventory.ANIMATION_TIME
        keyboard_helper.pressKey('v', 0.1, 'Open Inventory')

    def close(self):
        if not self.isInteractable:
            return
        if not self.isOpened:
            return
        self.isInteractable = False
        self.time = Inventory.ANIMATION_TIME
        keyboard_helper.pressKey('v', 0.1, 'Close Inventory')