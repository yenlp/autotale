import math
import time
import pyautogui
import ui_defines
import screen_utils
import keyboard
import random
import attack_button

isAlive=True
isPause=True

STATE_NONE=0
STATE_HOME=1
STATE_BATTLE=2
state=STATE_NONE

isHPLow=False
isMPLow=False
isSPLow=False
isHPEmpty=False
isMPEmpty=False
isSPEmpty=False
isInventoryOpen=False

BATTLE_STATE_FIND_ENEMY = 0
BATTLE_STATE_COMBAT = 1
battle_state = BATTLE_STATE_FIND_ENEMY

def update(img):
    result = {
        STATE_HOME : onHome,
        STATE_BATTLE : onBattle
    }.get(state, doNothing)(img)


def doNothing(img):
    dnt = 1

def onHome(img):
    if isHPLow:
        print('HP is low')
    if isMPLow:
        print('MP is low')
    if isSPLow:
        print('SP is low')
    if isHPEmpty:
        print('HP is empty')
    if isMPEmpty:
        print('MP is empty')
    if isSPEmpty:
        print('SP is empty')

def onBattle(img):
    if isHPLow:
        if isHPEmpty:
            goHome()
        else:
            HP_recovery()
    if isMPLow:
        if not isMPEmpty:
            MP_recovery()
    if isSPLow:
        if not isSPEmpty:
            SP_recovery()
    
    result = {
        BATTLE_STATE_FIND_ENEMY : findEnemy,
        BATTLE_STATE_COMBAT : combat
    }.get(battle_state, doNothing)(img)

last_attack_ts = time.time()
findEnemyState = 0
last_color_enemy = 0,0,0
combat_r = 0
combat_angle = 0
combat_find_time = 0.0

def findEnemy(img):
    global findEnemyState
    global battle_state
    global last_color_enemy
    global last_attack_ts
    global combat_r
    global combat_find_time
    if findEnemyState == 0:
        r = 100
        x = screen_utils.position_mid[0] + random.randrange(-r, r, 50)
        y = screen_utils.position_mid[1] + random.randrange(-r, r, 50)
        pos = x, y
        pos_mouse = screen_utils.getPositionOnScreen(pos)
        pyautogui.moveTo(pos_mouse[0], pos_mouse[1])
        pyautogui.mouseDown()
        pyautogui.mouseUp()
        pyautogui.mouseDown()
        pyautogui.mouseUp()
        findEnemyState = 1
        time.sleep(0.3)
    elif findEnemyState == 1:
        found = attack_button.isOnEnemy(img)
        if found:
            battle_state = BATTLE_STATE_COMBAT
            last_attack_ts = time.time()
            combat_r = 50
            combat_find_time = 0.0
            findEnemyState = 0
            print('enemy found - Combat')
            return
        findEnemyState = 0
        pyautogui.mouseDown()
        pyautogui.mouseUp()
        time.sleep(0.3)           

def combat(img):
    global last_attack_ts
    global battle_state
    global combat_r
    global combat_angle
    global combat_find_time
    combat_angle = combat_angle + 1.0
    x = screen_utils.position_mid[0] + combat_r * math.sin(combat_angle)
    y = screen_utils.position_mid[1] + combat_r * math.cos(combat_angle)
    pos = x, y
    pos_mouse = screen_utils.getPositionOnScreen(pos)
    pyautogui.moveTo(pos_mouse[0], pos_mouse[1], 0.1)
    found = attack_button.isOnEnemy(img)
    t = time.time()
    if found:
        last_attack_ts = t
        combat_r = 50
    else:
        if t - last_attack_ts > 0.5:
            if combat_r > 300:
                combat_r = 50
                battle_state = BATTLE_STATE_FIND_ENEMY
                print('findEnemy')
            else:
                combat_r = combat_r + 40
                last_attack_ts = t

def battleMode():
    global state
    global battle_state
    state = STATE_BATTLE
    battle_state = BATTLE_STATE_FIND_ENEMY
    print('findEnemy')

def mouseRight(pos):
    pyautogui.moveTo(pos[0], pos[1])
    pyautogui.mouseDown(button='right')
    pyautogui.mouseUp(button='right')
    time.sleep(0.2)

def pressKey(key, mess):
    print(mess)
    pyautogui.keyDown(key)
    pyautogui.keyUp(key)
    time.sleep(0.3)

def SP_recovery():
    pressKey('1', 'SP_recovery')

def HP_recovery():
    pressKey('2', 'HP_recovery')

def MP_recovery():
    pressKey('3', 'MP_recovery')
    
def goHome():
    global isPause
    global state
    isPause = True
    state = STATE_HOME
    print('goHome')
    print('Pause')
    if keyboard.is_pressed('left'):
        pyautogui.keyUp('left')
    if not isInventoryOpen:
        pressKey('v', 'open equipment')
    mouseRight(screen_utils.slot_core)