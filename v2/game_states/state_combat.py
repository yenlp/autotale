import math
import base.math
import random
import pyautogui
import settings
from game_states.sub_state import SubState

class StateCombat (SubState):
    POS_ATTACK_BUTTONS = ((460, 650), (455, 657), (453, 666))
    RADIUS_MIN = 100
    RADIUS_MAX = 400
    def __init__(self) -> None:
        print('Start Combat')
        super().__init__()
        #self.lostEnemyDuration = 0
        self.radius = (StateCombat.RADIUS_MAX + StateCombat.RADIUS_MIN) / 2
        self.angle = random.randrange(0, 360)

    def onFrameUpdate(self, deltaTime, screenshot, vm):
        self.time = self.time + deltaTime
        if settings.isAutoLoot and self.time > settings.combatDuration:
            print('Combat Timeout')
            self.nextState = SubState.LOOT
            return
        if self.isOnEnemy(screenshot):
            #print('onEnemy')
            #self.lostEnemyDuration = 0
            self.radius = base.math.lerp(self.radius, StateCombat.RADIUS_MAX, 0.9)
            self.radius = min(self.radius, StateCombat.RADIUS_MAX)
        else:
            #self.lostEnemyDuration += deltaTime
            if self.radius < StateCombat.RADIUS_MIN:
                print('Lost Target')
                self.nextState = SubState.LOOT
            else:
                self.radius = base.math.lerp(self.radius, 0, 0.02 * deltaTime)
    
    def onFrameRender(self, screenshot, vm):
        self.angle = (self.angle + random.randrange(30, 45)) % 360
        radian = self.angle / 180 * math.pi
        pos = vm.getMiddleScreenPosition()
        x = pos[0] + self.radius * math.sin(radian)
        y = pos[1] + self.radius * math.cos(radian) * 0.7
        pos_mouse = x, y
        pyautogui.moveTo(pos_mouse[0], pos_mouse[1], 0.15)

    def isOnEnemy(self, screenshot):
        diff = 10
        for pos in StateCombat.POS_ATTACK_BUTTONS:
            pix = screenshot.getpixel(pos)
            if abs(pix[0] - pix[1]) > diff:
                return False
            if abs(pix[1] - pix[2]) > diff:
                return False
            if abs(pix[2] - pix[0]) > diff:
                return False
        return True


