import keyboard
import pyautogui
from pyscreeze import USE_IMAGE_NOT_FOUND_EXCEPTION
import app_state
import ui_defines
from screen_utils import getPositionOnScreen

def init():
    keyboard.add_hotkey('ctrl+s', take_screenshot, args=())
    keyboard.add_hotkey('ctrl+p', pause, args=())
    keyboard.add_hotkey('ctrl+b', battle, args=())
    keyboard.add_hotkey('ctrl+h', home, args=())
    keyboard.add_hotkey('ctrl+0', quit, args=())

    keyboard.add_hotkey('ctrl+j', gotoSPBar, args=())
    keyboard.add_hotkey('ctrl+k', gotoHPBar, args=())
    keyboard.add_hotkey('ctrl+l', gotoMPBar, args=())

def pause():
    app_state.isPause = True
    if app_state.isPause:
        print('Paused')
    
def battle():
    app_state.isPause = False
    print('Start battle')
    app_state.battleMode()

def home():
    app_state.isPause = False
    app_state.state = app_state.STATE_HOME
    print('At home')

def quit():
    app_state.isAlive = False

def take_screenshot():
    pyautogui.screenshot('screen_capture.png')

def gotoHPBar():
    app_state.isPause = True
    pos = getPositionOnScreen(ui_defines.hp_bar_pos_low)
    pyautogui.moveTo(pos[0], pos[1], 0.2)

def gotoSPBar():
    app_state.isPause = True
    pos = getPositionOnScreen(ui_defines.sp_bar_pos_low)
    pyautogui.moveTo(pos[0], pos[1], 0.2)

def gotoMPBar():
    app_state.isPause = True
    pos = getPositionOnScreen(ui_defines.mp_bar_pos_low)
    pyautogui.moveTo(pos[0], pos[1], 0.2)

def update(img):
    if not app_state.isAlive:
        return