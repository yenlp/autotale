import keyboard
import pyautogui
from pyscreeze import USE_IMAGE_NOT_FOUND_EXCEPTION
import app_state
import ui_defines
import screen_utils

def init():
    keyboard.add_hotkey('ctrl+s', take_screenshot, args=())
    keyboard.add_hotkey('ctrl+p', pause, args=())
    keyboard.add_hotkey('ctrl+b', battle, args=())
    keyboard.add_hotkey('ctrl+h', home, args=())
    keyboard.add_hotkey('ctrl+0', quit, args=())

    keyboard.add_hotkey('ctrl+j', gotoSPBar, args=())
    keyboard.add_hotkey('ctrl+k', gotoHPBar, args=())
    keyboard.add_hotkey('ctrl+l', gotoMPBar, args=())
    keyboard.add_hotkey('ctrl+t', switchAutoCombat, args=())
    keyboard.add_hotkey('ctrl+]', autoRotate, args=())
    keyboard.add_hotkey('ctrl+[', autoLoot, args=())

    keyboard.add_hotkey('ctrl+u', spThreshold, args=())
    keyboard.add_hotkey('ctrl+i', hpThreshold, args=())
    keyboard.add_hotkey('ctrl+o', mpThreshold, args=())
    keyboard.add_hotkey('ctrl+-', combat_duration_decrease, args=())
    keyboard.add_hotkey('ctrl+=', combat_duration_increase, args=())

def pause():
    app_state.isPause = True
    if app_state.isPause:
        print('Paused')
    
def battle():
    app_state.isPause = False
    print('Start battle')
    print('AutoCombat is ' + str(app_state.isAutoCombat))
    print('AutoLoot is ' + str(app_state.isAutoLoot))
    print('AutoRotate is ' + str(app_state.isAutoRotate))
    app_state.battleMode()

def home():
    app_state.isPause = False
    app_state.state = app_state.STATE_HOME
    print('At home')

def quit():
    app_state.isAlive = False

def take_screenshot():
    x, y = screen_utils.screen_topleft
    w, h = screen_utils.screen_size
    img = pyautogui.screenshot('screenshot.png', region=(x, y, w, h))

def gotoHPBar():
    app_state.isPause = True
    pos = screen_utils.getPositionOnScreen(ui_defines.hp_bar_pos_low)
    pyautogui.moveTo(pos[0], pos[1], 0.2)

def gotoSPBar():
    app_state.isPause = True
    pos = screen_utils.getPositionOnScreen(ui_defines.sp_bar_pos_low)
    pyautogui.moveTo(pos[0], pos[1], 0.2)

def gotoMPBar():
    app_state.isPause = True
    pos = screen_utils.getPositionOnScreen(ui_defines.mp_bar_pos_low)
    pyautogui.moveTo(pos[0], pos[1], 0.2)

def switchAutoCombat():
    app_state.isAutoCombat = not app_state.isAutoCombat
    print('AutoCombat is ' + str(app_state.isAutoCombat))
    app_state.battle_state = app_state.BATTLE_STATE_FIND_ENEMY

def autoLoot():
    app_state.isAutoLoot = not app_state.isAutoLoot
    print('AutoLoot is ' + str(app_state.isAutoLoot))

def hpThreshold():
    app_state.hpThreshold = app_state.hpThreshold + 0.1
    if app_state.hpThreshold > 1.0:
        app_state.hpThreshold = app_state.hpThreshold - 1.0
    if app_state.hpThreshold < 0.4:
        app_state.hpThreshold = 0.4
    print('hpThreshold is ' + str(app_state.hpThreshold))

def spThreshold():
    app_state.spThreshold = app_state.spThreshold + 0.1
    if app_state.spThreshold > 1.0:
        app_state.spThreshold = app_state.spThreshold - 1.0
    if app_state.spThreshold < 0.2:
        app_state.spThreshold = 0.2
    print('spThreshold is ' + str(app_state.spThreshold))

def mpThreshold():
    app_state.mpThreshold = app_state.mpThreshold + 0.1
    if app_state.mpThreshold > 1.0:
        app_state.mpThreshold = app_state.mpThreshold - 1.0
    if app_state.mpThreshold < 0.2:
        app_state.mpThreshold = 0.2
    print('mpThreshold is ' + str(app_state.mpThreshold))

def combat_duration_decrease():
    app_state.combat_duration = app_state.combat_duration - 1
    print('combat_duration is ' + str(app_state.combat_duration))

def combat_duration_increase():
    app_state.combat_duration = app_state.combat_duration + 1
    print('combat_duration is ' + str(app_state.combat_duration))

def autoRotate():
    app_state.isAutoRotate = not app_state.isAutoRotate
    print('AutoRotate is ' + str(app_state.isAutoRotate))

def update(img):
    if not app_state.isAlive:
        return