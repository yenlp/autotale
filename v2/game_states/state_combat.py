import math
import random
import pyautogui
import settings
from game_states.sub_state import SubState

class StateCombat (SubState):
    RADIUS_MIN = 200
    RADIUS_MAX = 400
    def __init__(self) -> None:
        print('Start Combat')
        super().__init__()
        self.nextState = None
        self.lostEnemyDuration = 0
        self.radius = StateCombat.RADIUS_MIN
        self.angle = random.randrange(0, 360)

    def onFrameUpdate(self, deltaTime, screenshot, vm):
        self.time = self.time + deltaTime
        if self.time > settings.combatDuration:
            self.nextState = SubState.LOOT
            return
        if self.isOnEnemy(screenshot):
            self.lostEnemyDuration = 0
            self.radius = StateCombat.RADIUS_MIN
        else:
            self.lostEnemyDuration += deltaTime
            if self.lostEnemyDuration > 0.5:
                if self.radius > StateCombat.RADIUS_MAX:
                    self.nextState = SubState.FIND_ENEMY
                else:
                    self.radius = self.radius + 10
    
    def onFrameRender(self, screenshot, vm):
        self.angle = (self.angle + random.randrange(10, 30)) % 360
        radian = self.angle / 180 * math.pi
        pos = vm.getMiddleScreenPosition()
        x = pos[0] + self.radius * math.sin(radian)
        y = pos[1] + self.radius * math.cos(radian) * 0.7
        pos_mouse = x, y
        pyautogui.moveTo(pos_mouse[0], pos_mouse[1], 0.15)

    def isCompleted(self):
        return self.nextState != None

