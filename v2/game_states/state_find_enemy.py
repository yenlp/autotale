import random
import pyautogui
from game_states.state import SubState

class StateFindEnemy (SubState):
    def __init__(self, nextState) -> None:
        super().__init__(nextState)

    def onFrameUpdate(self, deltaTime, screenshot, vm):
        pass

    def onFrameRender(self, screenshot, vm):
        pos = vm.getMiddleScreenPosition()
        r = 50
        x = pos[0] + random.randrange(-r, r, 1)
        y = pos[1] + random.randrange(-r, r, 1) * 0.6
        pyautogui.moveTo(x, y, 0.15)