import pyautogui
import keyboard
import time
import settings
import base.math as bmath

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
    keyboard.add_hotkey('ctrl+u', percentSPChanged, args=())
    keyboard.add_hotkey('ctrl+i', percentHPChanged, args=())
    keyboard.add_hotkey('ctrl+o', percentMPChanged, args=())

def pressKey(key, sleepTime = 0.0, mess = None):
    if mess != None:
        print(mess)
    pyautogui.keyDown(key)
    pyautogui.keyUp(key)
    time.sleep(sleepTime)

def keyDown(key, sleepTime = 0.0, mess = None):
    if mess != None:
        print(mess)
    pyautogui.keyDown(key)
    time.sleep(sleepTime)

def keyUp(key, sleepTime = 0.0, mess = None):
    if mess != None:
        print(mess)
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

def percentSPChanged():
    vmin = 0.1
    settings.percentSP = max(settings.percentSP + 0.1, vmin)
    if settings.percentSP >= 1.0:
        settings.percentSP = vmin
    print('percentSP', str(settings.percentSP))
    g_app.onPercentChanged()

def percentHPChanged():
    vmin = 0.3
    settings.percentHP = max(settings.percentHP + 0.1, vmin)
    if settings.percentHP >= 1.0:
        settings.percentHP = vmin
    print('percentHP', str(settings.percentHP))
    g_app.onPercentChanged()

def percentMPChanged():
    vmin = 0.1
    settings.percentMP = max(settings.percentMP + 0.1, vmin)
    if settings.percentMP >= 1.0:
        settings.percentMP = vmin
    print('percentMP', str(settings.percentMP))
    g_app.onPercentChanged()
