from screen_utils import ScreenUtils
import pygetwindow as gw
import pyautogui
from game_states.game_idle import GameIdle

VM_WIDTH = 1024
VM_HEIGHT = 705

class VMController:
    def __init__(seft, name):
        seft.name = name
        seft.x = 0
        seft.y = 0
        seft.width = VM_WIDTH
        seft.height = VM_HEIGHT
        seft.marginTop = 0
        seft.marginBot = 0
        seft.screenUtils = ScreenUtils()
        seft.img = seft.detectWindow()
        seft.gameState = GameIdle()

    def detectWindow(seft):
        seft.update(0)
        p = seft.screenUtils.captureAndSave('screenshots/screenshot_init.png', region=(seft.x, seft.y, seft.width, seft.height))
        x_mid = seft.width / 2
        seft.marginTop = 5
        color = p.getpixel((x_mid, seft.marginTop))
        found = False
        while not found:
            seft.marginTop = seft.marginTop + 1
            color2 = p.getpixel((x_mid, seft.marginTop))
            for i in [0,1,2]:
                diff = color[i] - color2[i]
                if abs(diff) > 5:
                    found = True
        seft.marginBot = seft.height - seft.marginTop - VM_HEIGHT
        seft.update(0)
        p = seft.screenUtils.captureAndSave('screenshots/screenshot_detect.png', region=(seft.x, seft.y, seft.width, seft.height))
        return p

    def update(seft, deltaTime):
        win_app = gw.getWindowsWithTitle(seft.name)[0]
        w, h = win_app.size
        x, y = win_app.topleft
        x_mid = x + w / 2
        seft.x = x_mid - VM_WIDTH / 2
        seft.y = y + seft.marginTop
        seft.height = h - seft.marginBot - seft.marginTop
        seft.img = seft.screenUtils.capture(region=(seft.x, seft.y, seft.width, seft.height))
        print('VMController', seft.name)