import screen_utils
import pyautogui
import time
import app_state
import ui_defines

def init():
    print('IMG init')

def process(img):
    app_state.isHPLow = check_HP(img)
    app_state.isSPLow = check_SP(img)
    app_state.isMPLow = check_MP(img)
    app_state.isHPEmpty = isHPEmpty(img)
    app_state.isMPEmpty = isMPEmpty(img)
    app_state.isSPEmpty = isSPEmpty(img)
    app_state.isInventoryOpen = isInventoryOpen(img)

def check_SP(img):
    pix = img.getpixel(screen_utils.position_sp)
    idx = ui_defines.sp_bar_color[0]
    color = ui_defines.sp_bar_color[1]
    return pix[idx] < color

def check_HP(img):
    pix = img.getpixel(screen_utils.position_hp)
    idx = ui_defines.hp_bar_color[0]
    color = ui_defines.hp_bar_color[1]
    return pix[idx] < color

def check_MP(img):
    pix = img.getpixel(screen_utils.position_mp)
    idx = ui_defines.mp_bar_color[0]
    color = ui_defines.mp_bar_color[1]
    return pix[idx] < color

def isSPEmpty(img):
    pix = img.getpixel(screen_utils.slot_sp)
    idx = ui_defines.slot1_color[0]
    color = ui_defines.slot1_color[1]
    return pix[idx] < color
    
def isHPEmpty(img):
    pix = img.getpixel(screen_utils.slot_hp)
    idx = ui_defines.slot2_color[0]
    color = ui_defines.slot2_color[1]
    return pix[idx] < color

def isMPEmpty(img):
    pix = img.getpixel(screen_utils.slot_mp)
    idx = ui_defines.slot3_color[0]
    color = ui_defines.slot3_color[1]
    return pix[idx] < color

def isInventoryOpen(img):
    for x in 420, 430, 440, 450, 490, 500, 510:
        y = 585
        pix = img.getpixel((x, y))
        if pix[0] < 100 or pix[2] > 100:
            return False
    return True