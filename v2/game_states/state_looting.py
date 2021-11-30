import math
import pyautogui
import settings
from game_states.sub_state import SubState
import base.keyboard_helper as keyboard_helper
import random

class StateLooting (SubState):

    def __init__(self) -> None:
        super().__init__()
        self.lootFilterActive = False
        self.angle = 0

    def onFrameUpdate(self, deltaTime, screenshot, vm):
        self.time = self.time + deltaTime
        self.angle = self.angle + 30
        if self.time > settings.lootDuration:
            self.nextState = SubState.FIND_ENEMY
            keyboard_helper.pressKey('a', 0.05, 'Stop Loot')

    def onFrameRender(self, screenshot, vm):
        if self.lootFilterActive:
            r = 30
            radian = self.angle / 180 * math.pi
            pos = vm.getMiddleScreenPosition()
            x = pos[0] + r * math.sin(radian)
            y = pos[1] + r * math.cos(radian) * 0.7
            pos_mouse = x, y
            pyautogui.moveTo(pos_mouse[0], pos_mouse[1], 0.15)
            pyautogui.mouseDown()
            pyautogui.mouseUp()
        else:
            self.lootFilterActive = True
            p = pyautogui.PAUSE
            pyautogui.PAUSE = 0
            keyboard_helper.pressKey('a', 0.05, 'Start Loot')
            keyboard_helper.pressKey('a', 0.05)
            pyautogui.PAUSE = p