import keyboard
import pyautogui
import app_state

def init():
    keyboard.add_hotkey('ctrl+s', take_screenshot, args=())
    keyboard.add_hotkey('ctrl+p', pause, args=())
    keyboard.add_hotkey('ctrl+b', battle, args=())
    keyboard.add_hotkey('ctrl+h', home, args=())
    keyboard.add_hotkey('ctrl+0', quit, args=())

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

def update(img):
    if not app_state.isAlive:
        return