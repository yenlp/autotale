import math
import time
import pyautogui
import settings
from game_states.sub_state import SubState
import base.keyboard_helper as keyboard_helper
import random

class StateLooting (SubState):

    def __init__(self) -> None:
        super().__init__()
        self.lootFilterActive = False
        self.isRotateAllowed = False
        self.idx = -1
        self.angle = 0, 180, 45, 225, 90, 270, 135, 315

    def onFrameUpdate(self, deltaTime, screenshot, vm):
        self.time = self.time + deltaTime
        if self.idx >= len(self.angle):
            self.nextState = SubState.FIND_ENEMY
            keyboard_helper.pressKey('a', 0.05, 'Stop Loot')

    def onFrameRender(self, screenshot, vm):
        if self.lootFilterActive:
            self.idx = self.idx + 1
            if self.idx >= len(self.angle):
                return
            r = 30
            radian = self.angle[self.idx] / 180 * math.pi
            pos = vm.getMiddleScreenPosition()
            x = pos[0] + r * math.sin(radian)
            y = pos[1] + r * math.cos(radian)
            pos_mouse = x, y
            pyautogui.moveTo(pos_mouse[0], pos_mouse[1], 0.1)
            time.sleep(0.1)
            pyautogui.mouseDown()
            pyautogui.mouseUp()
            time.sleep(0.4)
        else:
            self.lootFilterActive = True
            time.sleep(0.2)
            p = pyautogui.PAUSE
            pyautogui.PAUSE = 0
            keyboard_helper.pressKey('a', 0.05, 'Start Loot')
            keyboard_helper.pressKey('a', 0.05)
            pyautogui.PAUSE = p