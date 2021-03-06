from screen_utils import ScreenUtils
import pygetwindow as gw
import time
from game_states.game_idle import GameIdle
from game_states.game_init import GameInit
from game_states.game_battle import GameBattle
from game_states.game_home import GameHome

VM_WIDTH = 1024
VM_HEIGHT = 705

class VMController:
    def __init__(self, name):
        self.name = name
        self.x = 0
        self.y = 0
        self.width = VM_WIDTH
        self.height = VM_HEIGHT
        self.marginTop = 0
        self.marginBot = 0
        self.isSaving = False
        self.screenUtils = ScreenUtils()
        self.gameStates = []
        self.img = self.detectWindow()
        self.activate()

    def detectWindow(self):
        self.onFrameUpdate(0)
        p = self.screenUtils.captureAndSave('screenshots/screenshot_init.png', region=(self.x, self.y, self.width, self.height))
        x_mid = self.width / 2
        self.marginTop = 5
        color = p.getpixel((x_mid, self.marginTop))
        found = False
        while not found:
            self.marginTop = self.marginTop + 1
            color2 = p.getpixel((x_mid, self.marginTop))
            for i in [0,1,2]:
                diff = color[i] - color2[i]
                if abs(diff) > 5:
                    found = True
        self.marginBot = self.height - self.marginTop - VM_HEIGHT
        self.onFrameUpdate(0)
        p = self.screenUtils.captureAndSave('screenshots/screenshot_detect.png', region=(self.x, self.y, self.width, self.height))
        return p
        
    def activate(self):
        win_app = gw.getWindowsWithTitle(self.name)[0]
        win_app.activate()

    def onFrameUpdate(self, deltaTime):
        #print('VMController::onFrameUpdate', self.name)
        win_app = gw.getWindowsWithTitle(self.name)[0]
        w, h = win_app.size
        x, y = win_app.topleft
        x_mid = x + w / 2
        self.x = x_mid - VM_WIDTH / 2
        self.y = y + self.marginTop
        self.height = h - self.marginBot - self.marginTop
        self.img = self.screenUtils.capture(region=(self.x, self.y, self.width, self.height))
        if self.isSaving:
            self.isSaving = False
            t = round(time.time())
            path = 'screenshots/screenshot_{t}.png'.format(t=t)
            self.img.save(path)
        if len(self.gameStates) > 1:
            state = self.gameStates[0]
            state.onStop()
            self.gameStates.remove(state)
        elif len(self.gameStates) == 0:
            state = GameInit()
            state.setVM(self)
            self.gameStates.append(state)
        state = self.gameStates[0]
        state.onFrameUpdate(deltaTime, self.img)

    def onFrameRender(self):
        #print('VMController::onFrameRender', self.name)
        state = self.gameStates[0]
        state.onFrameRender(self.img)

    def pushState(self, state):
        state.setVM(self)
        self.gameStates.append(state)

    def pause(self):
        self.pushState(GameIdle())

    def battle(self):
        self.pushState(GameBattle())

    def home(self):
        self.pushState(GameHome())

    def onPercentChanged(self):
        for state in self.gameStates:
            state.onPercentChanged()

    def takeScreenshots(self):
        self.isSaving = True

    def convertGameToScreen(self, position):
        x = self.x + position[0]
        y = self.y + position[1]
        return x, y

    def getMiddleScreenPosition(self):
        x = self.x + self.width / 2
        y = self.y + self.height / 2
        return x, y