import time
from keyboard import key_to_scan_codes
import keyboard
import pyautogui
import image_processing
import auto_input
import app_state
import screen_utils

def update(img):
    pos_mouse = pyautogui.position()
    if not screen_utils.containPoint(pos_mouse):
        app_state.isPause = True
        app_state.battle_state = app_state.BATTLE_STATE_FIND_ENEMY
        if keyboard.is_pressed('left'):
            pyautogui.keyUp('left')
        return
    image_processing.process(img)
    auto_input.update(img)
    app_state.update(img)

def loop():
    FPS = 30
    FRAME_RATE = 1.0 / FPS
    last_ts = time.time()
    while app_state.isAlive:
        if not app_state.isPause:
            screen_utils.update('AutoBot')
            x, y = screen_utils.screen_topleft
            w, h = screen_utils.screen_size
            img = pyautogui.screenshot(region=(x, y, w, h))
            update(img)
        ts = time.time()
        time_spent = ts - last_ts
        last_ts = ts
        if time_spent < FRAME_RATE:
            time.sleep(FRAME_RATE - time_spent)
    print('Exit')


def main():
    pyautogui.PAUSE = 0.1
    screen_utils.init()
    image_processing.init()
    auto_input.init()
    print('Ready')
    print('Press Ctrl+B to start battle')
    print('Press Ctrl+H to control at home')
    print('Press Ctrl+P to pause')
    print('Press Ctrl+0 to exit')
    loop()

if __name__ == "__main__":
    main()