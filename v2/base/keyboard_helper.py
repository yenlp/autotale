import pyautogui
import keyboard

g_app = None

def setupKeyboard(app):
    global g_app
    g_app = app
    pyautogui.PAUSE = 0.1
    keyboard.add_hotkey('ctrl+0', quit, args=())

def pressKey(key):
    print('pressKey', key)
    pyautogui.keyDown(key)
    pyautogui.keyUp(key)

def quit():
    g_app.onQuitCommand()