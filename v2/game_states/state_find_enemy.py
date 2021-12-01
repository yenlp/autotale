import time
import pyautogui
import math
from game_states.sub_state import SubState
import base.keyboard_helper as keyboard_helper

class StateFindEnemy (SubState):
    FINDING = 0
    CONFIRMING = 1
    FOUND = 2

    def __init__(self) -> None:
        print('Find Enemy')
        super().__init__()
        self.state = StateFindEnemy.FINDING
        self.isRotateAllowed = False
        self.idx = -1
        self.angle = 0, 180, 45, 225, 90, 270, 135, 315

    def onFrameUpdate(self, deltaTime, screenshot, vm):
        result = {
            StateFindEnemy.FINDING : self.onFindingUpdate,
            StateFindEnemy.CONFIRMING : self.onConfirmingUpdate,
            StateFindEnemy.FOUND: self.onFoundUpdate
        }.get(self.state, self.doNothing)(deltaTime, screenshot, vm)

    def onFrameRender(self, screenshot, vm):
        result = {
            StateFindEnemy.FINDING : self.onFindingRender,
            StateFindEnemy.CONFIRMING : self.onConfirmingRender,
            StateFindEnemy.FOUND: self.onFoundRender
        }.get(self.state, self.doNothing)(0.0, screenshot, vm)

    def onFindingUpdate(self, deltaTime, screenshot, vm):
        pass

    def onConfirmingUpdate(self, deltaTime, screenshot, vm):
        self.time = self.time + deltaTime
        if self.time >= 0.5:
            if self.isOnEnemy(screenshot):
                self.state = StateFindEnemy.FOUND
                self.nextState = SubState.COMBAT
            else:
                self.state = StateFindEnemy.FINDING
            self.time = 0.0

    def onFoundUpdate(self, deltaTime, screenshot, vm):
        pass

    def onFindingRender(self, deltaTime, screenshot, vm):
        self.idx = (self.idx + 1) % len(self.angle)
        radian = self.angle[self.idx] / 180 * math.pi
        pos = vm.getMiddleScreenPosition()
        r = 75
        x = pos[0] + r * math.sin(radian)
        y = pos[1] + r * math.cos(radian)
        pyautogui.moveTo(x, y, 0.15)
        time.sleep(0.1)
        keyShift = 'shift'
        keyboard_helper.keyDown(keyShift, 0.15)
        pyautogui.mouseDown()
        pyautogui.mouseUp()
        keyboard_helper.keyUp(keyShift, 0.15)
        self.time = 0
        self.state = StateFindEnemy.CONFIRMING

    def onConfirmingRender(self, deltaTime, screenshot, vm):
        pass

    def onFoundRender(self, deltaTime, screenshot, vm):
        pass
