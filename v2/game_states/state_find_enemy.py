import random
import pyautogui
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
        pos = vm.getMiddleScreenPosition()
        r = 75
        x = pos[0] + random.randrange(-r, r, 1)
        y = pos[1] + random.randrange(-r, r, 1) * 0.7
        pyautogui.moveTo(x, y, 0.15)
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
