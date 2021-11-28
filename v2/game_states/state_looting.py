import math
import pyautogui
from game_states.sub_state import SubState
import base.keyboard_helper as keyboard_helper

class StateLooting (SubState):

    def __init__(self) -> None:
        print('Start Loot')
        super().__init__()
        self.lootFilterActive = False

    def onFrameUpdate(self, deltaTime, screenshot, vm):
        self.time = self.time + deltaTime
        if self.time > 5:
            self.nextState = SubState.FIND_ENEMY
            keyboard_helper.pressKey('a', 0.05)

    def onFrameRender(self, screenshot, vm):
        if self.lootFilterActive:
            r = 20
            pos = vm.getMiddleScreenPosition()
            x = pos[0] + r * math.sin(r)
            y = pos[1] + r * math.cos(r) * 0.7
            pos_mouse = x, y
            pyautogui.moveTo(pos_mouse[0], pos_mouse[1], 0.15)
            pyautogui.mouseDown()
            pyautogui.mouseUp()
        else:
            self.lootFilterActive = True
            p = pyautogui.PAUSE
            pyautogui.PAUSE = 0
            keyboard_helper.pressKey('a', 0.05)
            keyboard_helper.pressKey('a', 0.05)
            pyautogui.PAUSE = p