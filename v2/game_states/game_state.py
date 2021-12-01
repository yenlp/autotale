import time
import base.keyboard_helper as keyboard_helper
from hub.hub_controller import HubController

class GameState:
    def __init__(self):
        #print('GameState')
        #keyboard_helper.pressKey('a')
        time.sleep(0.2)
        self.isRunning = True
        self.vm = None
        self.hubController = HubController()

    def setVM(self, vm):
        self.vm = vm
        if self.hubController != None:
            self.hubController.setVM(vm)

    def onPercentChanged(self):
        if self.hubController != None:
            self.hubController.onPercentChanged()

    def onFrameUpdate(self, deltaTime, screenshot):
        if self.hubController != None:
            self.hubController.onFrameUpdate(deltaTime, screenshot)

    def onFrameRender(self, screenshot):
        if self.hubController != None:
            self.hubController.onFrameRender(screenshot)