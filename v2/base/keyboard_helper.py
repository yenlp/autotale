import pyautogui
import keyboard
import time

g_app = None

def setupKeyboard(app):
    global g_app
    g_app = app
    pyautogui.PAUSE = 0.1
    keyboard.add_hotkey('ctrl+0', quit, args=())

def pressKey(key, sleepTime = 0.0, mess = None):
    if mess != None:
        print('pressKey', key, '==>', mess)
    pyautogui.keyDown(key)
    pyautogui.keyUp(key)
    time.sleep(sleepTime)

def keyDown(key, sleepTime = 0.0, mess = None):
    if mess != None:
        print('keyDown', key, '==>', mess)
    pyautogui.keyDown(key)
    time.sleep(sleepTime)

def keyUp(key, sleepTime = 0.0, mess = None):
    if mess != None:
        print('keyUp', key, '==>', mess)
    pyautogui.keyUp(key)
    time.sleep(sleepTime)

def quit():
    g_app.onQuitCommand()