import constant
import screen_utils
import pyautogui

POS_TOP = 485, 650
COLOR_TOP = 80, 64, 41

POS_BOTTOM = 485, 688
COLOR_BOTTOM= 32, 16, 3

POS_LEFT = 465, 668
COLOR_LEFT = 51, 35, 17

POS_RIGHT = 503, 668
COLOR_RIGHT = 55, 43, 35

def isOnEnemy(img):
    pix = img.getpixel(POS_TOP)
    for i in 0,1,2:
        if abs(pix[i] - COLOR_TOP[i]) > 50:
            return True
    
    pix = img.getpixel(POS_BOTTOM)
    for i in 0,1,2:
        if abs(pix[i] - COLOR_BOTTOM[i]) > 50:
            return True

    pix = img.getpixel(POS_LEFT)
    for i in 0,1,2:
        if abs(pix[i] - COLOR_LEFT[i]) > 50:
            return True

    pix = img.getpixel(POS_RIGHT)
    for i in 0,1,2:
        if abs(pix[i] - COLOR_RIGHT[i]) > 50:
            return True

    return False