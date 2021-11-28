import pyautogui
import keyboard
import time

g_app = None

def setupKeyboard(app):
    global g_app
    g_app = app
    pyautogui.PAUSE = 0.1
    keyboard.add_hotkey('ctrl+0', quit, args=())

def pressKey(key, mess):
    print('pressKey', key, '==>', mess)
    pyautogui.keyDown(key)
    pyautogui.keyUp(key)
    time.sleep(0.1)

def quit():
    g_app.onQuitCommand()