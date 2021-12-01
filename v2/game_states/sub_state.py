import time
import base.keyboard_helper as keyboard_helper

class SubState:
    IDLE = 0
    FIND_ENEMY = 1
    COMBAT = 2
    LOOT = 3
    
    def __init__(self) -> None:
        time.sleep(0.2)
        keyboard_helper.pressKey('a')
        self.nextState = None
        self.time = 0
        self.isRotateAllowed = True

    def onFrameUpdate(self, deltaTime, screenshot, vm):
        pass

    def onFrameRender(self, screenshot, vm):
        pass

    def isCompleted(self):
        return self.nextState != None

    def getNextStateId(self):
        return self.nextState

    def doNothing(self, deltaTime, screenshot, vm):
        pass
