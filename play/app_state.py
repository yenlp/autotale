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
isAutoCombat=False

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
BATTLE_STATE_LOOT = 2
battle_state = BATTLE_STATE_FIND_ENEMY
loot_state = 0

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

time_battle = 0.0

def onBattle(img):
    global battle_state
    global time_battle
    global loot_state
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
    if isHPEmpty:
        HP_more()
    if isMPEmpty:
        MP_more()
    if isSPEmpty:
        SP_more()

    if isAutoCombat:
        if battle_state == BATTLE_STATE_LOOT:
            if time.time() - time_battle > 10:
                time_battle = time.time()
                battle_state = BATTLE_STATE_FIND_ENEMY
                loot_state = 0
                pressKey('a', 'stop loot')
        else:
            if time.time() - time_battle > 200:
                time_battle = time.time()
                battle_state = BATTLE_STATE_LOOT
                loot_state = 0
        result = {
            BATTLE_STATE_FIND_ENEMY : findEnemy,
            BATTLE_STATE_COMBAT : combat,
            BATTLE_STATE_LOOT: loot
        }.get(battle_state, doNothing)(img)

last_attack_ts = time.time()
findEnemyState = 0
last_color_enemy = 0,0,0
combat_r_default = 200
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
        r = 50
        x = screen_utils.position_mid[0] + random.randrange(-r, r, 1)
        y = screen_utils.position_mid[1] + random.randrange(-r, r, 1)
        pos = x, y
        pos_mouse = screen_utils.getPositionOnScreen(pos)
        pyautogui.moveTo(pos_mouse[0], pos_mouse[1])
        pyautogui.keyDown('shift')
        time.sleep(0.3)   
        pyautogui.mouseDown()
        pyautogui.mouseUp()
        time.sleep(0.3)   
        pyautogui.keyUp('shift')
        findEnemyState = 1
        time.sleep(0.3)
    elif findEnemyState == 1:
        found = attack_button.isOnEnemy(img)
        if found:
            battle_state = BATTLE_STATE_COMBAT
            last_attack_ts = time.time()
            combat_r = combat_r_default
            combat_find_time = 0.0
            findEnemyState = 0
            r = combat_r_default
            x = screen_utils.position_mid[0] + random.randrange(-r, r, 1)
            y = screen_utils.position_mid[1] + random.randrange(-r, r, 1)
            pos = x, y
            pos_mouse = screen_utils.getPositionOnScreen(pos)
            pyautogui.moveTo(pos_mouse[0], pos_mouse[1])
            print('enemy found - Combat')
            return
        findEnemyState = 0
        time.sleep(0.3)           

def combat(img):
    global last_attack_ts
    global battle_state
    global combat_r
    global combat_angle
    global combat_find_time
    found = attack_button.isOnEnemy(img)
    t = time.time()
    if found:
        last_attack_ts = t
        combat_r = combat_r_default
    else:
        combat_angle = combat_angle + 2
        x = screen_utils.position_mid[0] + combat_r * math.sin(combat_angle)
        y = screen_utils.position_mid[1] + combat_r * math.cos(combat_angle) * 0.6
        pos = x, y
        pos_mouse = screen_utils.getPositionOnScreen(pos)
        pyautogui.moveTo(pos_mouse[0], pos_mouse[1], 0.1)
        if t - last_attack_ts > 0.5:
            if combat_r > 400:
                combat_r = combat_r_default
                battle_state = BATTLE_STATE_FIND_ENEMY
                print('findEnemy')
            else:
                combat_r = combat_r + 10
                last_attack_ts = t    
def loot(img):
    global loot_state
    global combat_angle
    if loot_state == 0:
        pyautogui.PAUSE = 0.0
        pyautogui.keyDown('a')
        #time.sleep(0.05)
        pyautogui.keyUp('a')
        time.sleep(0.05)
        pyautogui.keyDown('a')
        #time.sleep(0.05)
        pyautogui.keyUp('a')
        time.sleep(0.05)
        print('loot')
        pyautogui.PAUSE = 0.1
        loot_state = 1
    else:
        r = 20
        combat_angle = combat_angle + 20
        x = screen_utils.position_mid[0] + r * math.sin(combat_angle)
        y = screen_utils.position_mid[1] + r * math.cos(combat_angle) * 0.6
        pos = x, y
        pos_mouse = screen_utils.getPositionOnScreen(pos)
        pyautogui.moveTo(pos_mouse[0], pos_mouse[1])
        pyautogui.mouseDown()
        pyautogui.mouseUp()
        time.sleep(0.1)

def battleMode():
    global state
    global battle_state
    global time_battle
    state = STATE_BATTLE
    battle_state = BATTLE_STATE_FIND_ENEMY
    time_battle = time.time()
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

def HP_more():
    pos = screen_utils.slot_hp_more
    do_key_more_potion(pos, '2')

def SP_more():
    pos = screen_utils.slot_sp_more
    do_key_more_potion(pos, '1')

def MP_more():
    pos = screen_utils.slot_mp_more
    do_key_more_potion(pos, '3')

def do_key_more_potion(pos, key):
    print('more Potion ' + key)   
    mouse_pos = pyautogui.position() 
    if not isInventoryOpen:
        pressKey('v', 'open equipment')
    pyautogui.moveTo(pos[0], pos[1])
    pyautogui.keyDown('shift')
    pyautogui.keyDown(key)
    time.sleep(0.1)
    pyautogui.keyUp(key)
    pyautogui.keyUp('shift')
    time.sleep(0.1)
    pressKey('v', 'close equipment')   
    pyautogui.moveTo(mouse_pos, 0.1)

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