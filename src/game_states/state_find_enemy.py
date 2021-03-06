from __future__ import absolute_import
import random
import time
import pyautogui
import math
from game_states.sub_state import SubState
import base.keyboard_helper as keyboard_helper

class StateFindEnemy (SubState):
    INIT = 0
    FINDING = 1
    CONFIRMING = 2
    FOUND = 3

    POS_TOP = 485, 650
    COLOR_TOP = 80, 64, 41

    POS_BOTTOM = 485, 688
    COLOR_BOTTOM= 32, 16, 3

    POS_LEFT = 465, 668
    COLOR_LEFT = 51, 35, 17

    POS_RIGHT = 503, 668
    COLOR_RIGHT = 55, 43, 35

    def __init__(self) -> None:
        print('Find Enemy')
        super().__init__()
        self.state = StateFindEnemy.INIT
        self.isRotateAllowed = False
        self.idx = -1
        self.radius = 75
        self.angle = 0, 180, 45, 225, 90, 270, 135, 315
        # for i in range(30):
        #     angle = random.randrange(0, 359)
        #     self.angle.append(angle)
        #     self.angle.append(angle + 180)

    def onFrameUpdate(self, deltaTime, screenshot, vm):
        result = {
            StateFindEnemy.INIT : self.onInitUpdate,
            StateFindEnemy.FINDING : self.onFindingUpdate,
            StateFindEnemy.CONFIRMING : self.onConfirmingUpdate,
            StateFindEnemy.FOUND: self.onFoundUpdate
        }.get(self.state, self.doNothing)(deltaTime, screenshot, vm)

    def onFrameRender(self, screenshot, vm):
        result = {
            StateFindEnemy.INIT : self.onInitRender,
            StateFindEnemy.FINDING : self.onFindingRender,
            StateFindEnemy.CONFIRMING : self.onConfirmingRender,
            StateFindEnemy.FOUND: self.onFoundRender
        }.get(self.state, self.doNothing)(0.0, screenshot, vm)

    def onInitUpdate(self, deltaTime, screenshot, vm):
        self.time += deltaTime
        if self.time > 1:
            self.state = StateFindEnemy.FINDING

    def onFindingUpdate(self, deltaTime, screenshot, vm):
        pass

    def onConfirmingUpdate(self, deltaTime, screenshot, vm):
        self.time = self.time + deltaTime
        if self.time >= 1:
            if self.isOnEnemy(screenshot):
                self.state = StateFindEnemy.FOUND
                self.nextState = SubState.COMBAT
            else:
                self.state = StateFindEnemy.FINDING
            self.time = 0.0

    def onFoundUpdate(self, deltaTime, screenshot, vm):
        pass

    def onInitRender(self, deltaTime, screenshot, vm):
        pos = vm.getMiddleScreenPosition()
        pyautogui.moveTo(pos[0], pos[1], 0.1)
        #time.sleep(0.1)
        pyautogui.mouseDown(button=pyautogui.RIGHT)
        pyautogui.mouseUp(button=pyautogui.RIGHT)
        #time.sleep(0.2)

    def onFindingRender(self, deltaTime, screenshot, vm):
        self.idx = self.idx + 1
        if self.idx >= len(self.angle):
            self.idx = 0
            self.radius = (self.radius + 15) % 200
        radian = self.angle[self.idx] / 180 * math.pi
        pos = vm.getMiddleScreenPosition()
        x = pos[0] + self.radius * math.sin(radian)
        y = pos[1] + self.radius * math.cos(radian) * 0.5
        pyautogui.moveTo(x, y, 0.1)
        time.sleep(0.1)
        keyShift = 'shift'
        keyboard_helper.keyDown(keyShift, 0.05)
        pyautogui.mouseDown()
        pyautogui.mouseUp()
        keyboard_helper.keyUp(keyShift, 0.1)
        self.time = 0
        self.state = StateFindEnemy.CONFIRMING

    def onConfirmingRender(self, deltaTime, screenshot, vm):
        pass

    def onFoundRender(self, deltaTime, screenshot, vm):
        pass

    def isOnEnemy(self, screenshot):
        pix = screenshot.getpixel(StateFindEnemy.POS_TOP)
        for i in 0,1,2:
            if abs(pix[i] - StateFindEnemy.COLOR_TOP[i]) > 50:
                return True
        
        pix = screenshot.getpixel(StateFindEnemy.POS_BOTTOM)
        for i in 0,1,2:
            if abs(pix[i] - StateFindEnemy.COLOR_BOTTOM[i]) > 50:
                return True

        pix = screenshot.getpixel(StateFindEnemy.POS_LEFT)
        for i in 0,1,2:
            if abs(pix[i] - StateFindEnemy.COLOR_LEFT[i]) > 50:
                return True

        pix = screenshot.getpixel(StateFindEnemy.POS_RIGHT)
        for i in 0,1,2:
            if abs(pix[i] - StateFindEnemy.COLOR_RIGHT[i]) > 50:
                return True

        return False
