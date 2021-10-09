import pyautogui
import app_state

def update(img):
    if not app_state.isAlive:
        return