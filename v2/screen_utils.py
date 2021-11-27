import pyautogui

class ScreenUtils:
    def __init__(seft):
        seft.img = None

    def capture(seft, region):
        seft.img = pyautogui.screenshot(region=region)
        return seft.img

    def captureAndSave(seft, filepath, region):
        seft.img = pyautogui.screenshot(filepath, region)
        return seft.img