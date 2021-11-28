import pyautogui

def setupKeyboard():
    pyautogui.PAUSE = 0.1

def pressKey(key):
    print('pressKey', key)
    pyautogui.keyDown(key)
    pyautogui.keyUp(key)