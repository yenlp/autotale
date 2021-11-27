import pyautogui

class ScreenUtils:
    def __init__(seft):
        seft.img = None

    def capture(seft, region):
        seft.img = pyautogui.screenshot('screenshots/v2.png', region)
        return seft.img