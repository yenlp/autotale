import base.keyboard_helper

class Inventory:
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
        self.isInteractable = False
        self.time = 2
        base.keyboard_helper.pressKey('v', 'open inventory')

    def close(self):
        if not self.isInteractable:
            return
        self.isInteractable = False
        self.time = 2
        base.keyboard_helper.pressKey('v', 'close inventory')