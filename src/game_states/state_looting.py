import math
import time
import pyautogui
import settings
from game_states.sub_state import SubState
import base.keyboard_helper as keyboard_helper
import random

class StateLooting (SubState):
    LOOT_FILTER_ACTIVE = 0
    CLICK = 1
    PICK_UP = 2
    COMPLETED = 3

    def __init__(self) -> None:
        super().__init__()
        self.isRotateAllowed = False
        self.state = StateLooting.LOOT_FILTER_ACTIVE
        self.idx = -1
        self.angle = 0, 180, 45, 225, 90, 270, 135, 315

    def onFrameUpdate(self, deltaTime, screenshot, vm):
        self.time = self.time + deltaTime
        if self.state == StateLooting.CLICK:
            self.idx = self.idx + 1
        elif self.state == StateLooting.PICK_UP:
            self.time += deltaTime
        if self.idx >= len(self.angle):
            self.state = StateLooting.COMPLETED
            self.nextState = SubState.FIND_ENEMY
            keyboard_helper.keyUp('a', 0.0, 'Stop Loot')

    def onFrameRender(self, screenshot, vm):
        if self.state == StateLooting.LOOT_FILTER_ACTIVE:
            self.state = StateLooting.CLICK
            time.sleep(0.2)
            keyboard_helper.keyDown('a', 0, 'Start Loot')
        elif self.state == StateLooting.CLICK:
            r = 50
            radian = self.angle[self.idx] / 180 * math.pi
            pos = vm.getMiddleScreenPosition()
            x = pos[0] + r * math.sin(radian)
            y = pos[1] + r * math.cos(radian)
            pos_mouse = x, y
            pyautogui.moveTo(pos_mouse[0], pos_mouse[1], 0.1)
            time.sleep(0.1)
            pyautogui.mouseDown()
            pyautogui.mouseUp()
            self.state = StateLooting.PICK_UP
        elif self.state == StateLooting.PICK_UP:
            if self.time >= 0.5:
                self.state = StateLooting.CLICK