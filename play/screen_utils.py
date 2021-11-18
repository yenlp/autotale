import app_defines
import ui_defines
import time
import pyautogui
import pygetwindow as gw


VM_WIDTH = 1024
VM_HEIGHT = 705

margin_top = 0
margin_bot = 0
screen_size = 0, 0
screen_topleft = 0, 0

position_mid = 0, 0
position_sp = 0, 0
position_hp = 0, 0
position_mp = 0, 0

slot_sp = 0, 0
slot_hp = 0, 0
slot_mp = 0, 0
slot_core = 0, 0

slot_sp_more = 0,0
slot_hp_more = 0,0
slot_mp_more = 0,0

position_enemy_hp = 0, 0

def getPositionByRatio(win_app, r):
    return win_app.left + win_app.width * r[0],  win_app.top + win_app.height * r[1]

def getPositionOnScreen(designPos):
    x = screen_topleft[0] + designPos[0]
    y = screen_topleft[1] + designPos[1]
    return x, y

def getPositionOnWindow(low, high, minPercent):
    x = low[0] * (1.0 - minPercent) + high[0] * minPercent
    y = low[1] * (1.0 - minPercent) + high[1] * minPercent
    return x, y
    
def update(title):
    global screen_size
    global screen_topleft
    global position_mid
    global position_sp
    global position_hp
    global position_mp
    global slot_hp
    global slot_sp
    global slot_mp
    global slot_core
    global slot_sp_more
    global slot_hp_more
    global slot_mp_more
    global position_enemy_hp
    win_app = gw.getWindowsWithTitle(title)[0]
    screen_size = win_app.size
    screen_topleft = win_app.topleft
    x_mid = screen_topleft[0] + screen_size[0] / 2
    screen_topleft = x_mid - VM_WIDTH / 2, screen_topleft[1] + margin_top
    screen_size = VM_WIDTH, screen_size[1] - margin_top - margin_bot
    position_mid = VM_WIDTH / 2, VM_HEIGHT / 2
    position_sp = getPositionOnWindow(ui_defines.sp_bar_pos_low, ui_defines.sp_bar_pos_high, 0.2)
    position_hp = getPositionOnWindow(ui_defines.hp_bar_pos_low, ui_defines.hp_bar_pos_high, 0.5)
    position_mp = getPositionOnWindow(ui_defines.mp_bar_pos_low, ui_defines.mp_bar_pos_high, 0.1)
    slot_hp = ui_defines.slot2_pos
    slot_sp = ui_defines.slot1_pos
    slot_mp = ui_defines.slot3_pos
    slot_core =  getPositionOnScreen(ui_defines.v_core_pos)
    slot_sp_more = getPositionOnScreen(ui_defines.v_sp_pos)
    slot_hp_more = getPositionOnScreen(ui_defines.v_hp_pos)
    slot_mp_more = getPositionOnScreen(ui_defines.v_mp_pos)
    position_enemy_hp = getPositionByRatio(win_app, app_defines.r_enemy_hp)


def init():
    global screen_topleft
    global screen_size
    global margin_bot
    global margin_top
    margin_top = 0
    margin_bot = 0
    update('AutoBot')
    x, y = screen_topleft
    w, h = screen_size
    p = pyautogui.screenshot('screenshot_init.png', region=(x, y, w, h))
    x_mid = w / 2
    margin_top = 5
    color = p.getpixel((x_mid, margin_top))
    found = False
    while not found:
        margin_top = margin_top + 1
        color2 = p.getpixel((x_mid, margin_top))
        for i in [0,1,2]:
            diff = color[i] - color2[i]
            if abs(diff) > 5:
                found = True
    margin_bot = screen_size[1] - margin_top - VM_HEIGHT
    update('AutoBot')
    time.sleep(1)

def containPoint(point):
    return containXY(point[0], point[1])

def containXY(x, y):
    if screen_topleft[0] > x or x > screen_topleft[0] + screen_size[0]:
        return False
    if screen_topleft[1] > y or y > screen_topleft[1] + screen_size[1]:
        return False
    return True