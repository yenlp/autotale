from screen_utils import ScreenUtils
import pygetwindow as gw
from game_states.game_state import GameState

class VMController:
    def __init__(seft, name):
        seft.name = name
        seft.screenUtils = ScreenUtils()
        seft.img = None
        seft.gameState = GameState()

    def update(seft, deltaTime):
        win_app = gw.getWindowsWithTitle(seft.name)[0]
        w, h = win_app.size
        x, y = win_app.topleft
        seft.img = seft.screenUtils.capture(region=(x,y,w,h))
        print('VMController ', seft.name)