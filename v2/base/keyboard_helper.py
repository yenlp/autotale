import pyautogui
import keyboard
import time
import settings

g_app = None

def setupKeyboard(app):
    global g_app
    g_app = app
    pyautogui.PAUSE = 0.1
    keyboard.add_hotkey('ctrl+0', quit, args=())
    keyboard.add_hotkey('ctrl+p', pause, args=())
    keyboard.add_hotkey('ctrl+b', battle, args=())
    keyboard.add_hotkey('ctrl+t', autoCombatSwitch, args=())
    keyboard.add_hotkey('ctrl+[', autoLootSwitch, args=())
    keyboard.add_hotkey('ctrl+]', autoRotateSwitch, args=())
    keyboard.add_hotkey('ctrl+-', combatDurationDecrease, args=())
    keyboard.add_hotkey('ctrl+=', combatDurationIncrease, args=())

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

def pause():
    g_app.onPauseCommand()

def battle():
    g_app.onBattleCommand()

def autoCombatSwitch():
    settings.isAutoCombat = not settings.isAutoCombat
    print('Auto Combat', str(settings.isAutoCombat))

def autoLootSwitch():
    settings.isAutoLoot = not settings.isAutoLoot
    print('Auto Loot', str(settings.isAutoLoot))

def autoRotateSwitch():
    settings.isAutoRotate = not settings.isAutoRotate
    print('Auto Rotate', str(settings.isAutoRotate))

def combatDurationDecrease():
    settings.combatDuration = max(1, settings.combatDuration - 1)
    print('Combat Duration', str(settings.combatDuration))

def combatDurationIncrease():
    settings.combatDuration = max(1, settings.combatDuration + 1)
    print('Combat Duration', str(settings.combatDuration))
